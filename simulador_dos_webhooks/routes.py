from flask import render_template, redirect, url_for, flash, request, abort, make_response
from simulador_dos_webhooks import app, database, bcrypt
from simulador_dos_webhooks.forms import FormLogin, FormCriarConta, FormEditarPerfil
from simulador_dos_webhooks.models import Usuario, Webhook
from flask_login import login_user, logout_user, current_user, login_required
import json
import pandas as pd
import csv
import io


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/webhook')
@login_required
def webhook():
    webhook_list = Webhook.query.all()
    webhook_list.reverse()

    return render_template('webhook.html', webhook_list=webhook_list)


@app.route('/filter-webhooks', methods=['GET'])
@login_required
def filter_webhooks():
    column = request.args.get('column')
    value = request.args.get('value')
    value = str(value).strip()
    
    if column and value:
        webhooks = Webhook.query.filter(getattr(Webhook, column).ilike(f'%{value}%')).all()
    else:
        webhooks = Webhook.query.all()

    webhooks.reverse()
    return render_template('webhook.html', webhook_list=webhooks, filter_data=True)


@app.route('/download-webhooks')
@login_required
def download_webhooks():
    webhook_list = Webhook.query.all()
    webhook_list.reverse()

    df = pd.DataFrame([wh.__dict__ for wh in webhook_list])
    df = df.reset_index(drop=True)

    if "_sa_instance_state" in list(df.columns):
        df = df.drop(columns=["_sa_instance_state"])

    csv_stream = io.StringIO()

    df.to_csv(csv_stream, encoding="utf-8-sig", index=False, sep=";", quoting=csv.QUOTE_NONNUMERIC)

    response = make_response(csv_stream.getvalue())
    response.headers["Content-Disposition"] = "attachment; filename=webhooks.csv"
    response.headers["Content-type"] = "text/csv"
    return response


@app.route('/iwpdosyoakwccrwfcdakpfuyrobpxeucqbvhorrdorsrrjvefy', methods=['POST'])
def webhook_receptor():
    if request.method == 'POST':
        response = request.data

        decoded_response = json.loads(response.decode('utf-8'))
        nome, email, status, valor, forma_pagamento, parcelas = decoded_response.values()

        if status == "aprovado":
            print(f">> liberar acesso ao curso para o e-mail: {decoded_response['email']}")
            tratativa = "Liberou o acesso ao curso e notificou o cliente"

        elif status == "recusado":
            print(f">> enviar mensagem de pagamento recusado para o e-mail: {decoded_response['email']}")
            tratativa = "Bloqueou o acesso ao curso e notificou o cliente"

        elif status == "reembolsado":
            print(f">> remover acesso ao curso do e-mail: {decoded_response['email']}")
            tratativa = "Removeu o acesso ao curso e notificou o cliente"

        else:
            print(f">> enviar mensagem de pagamento desaprovado para o e-mail: {decoded_response['email']}")
            tratativa = "Bloqueou o acesso ao curso e notificou o cliente"

        webhook_response = Webhook(
            nome=nome, email=email,
            status=status, valor=valor,
            forma_pagamento=forma_pagamento, parcelas=parcelas,
            tratativa=tratativa
        )
        database.session.add(webhook_response)
        database.session.commit()

        return 'success', 200
    else:
        abort(400)


@app.route('/criar-conta', methods=['GET', 'POST'])
def create_account():
    form_criarconta = FormCriarConta()

    if form_criarconta.validate_on_submit() and 'button_submit_create_acount' in request.form:
        pass_cript = bcrypt.generate_password_hash(form_criarconta.password.data)
        usuario = Usuario(
            username=form_criarconta.username.data, email=form_criarconta.email.data,
            password=pass_cript, token=form_criarconta.token.data)
        database.session.add(usuario)
        database.session.commit()
        flash(f'Conta criada para o e-mail: {form_criarconta.email.data}', 'alert-success')
        return redirect(url_for('login'))
    return render_template('criarconta.html', form_criarconta=form_criarconta)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    if form_login.validate_on_submit() and 'button_submit_login' in request.form:
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.password, form_login.password.data):
            login_user(usuario, remember=form_login.remember_info.data)
            flash(f'Login feito com sucesso no e-mail: {form_login.email.data}', 'alert-success')
            par_next = request.args.get('next')
            if par_next:
                return redirect(par_next)
            else:
                return redirect(url_for('webhook'))
        else:
            flash(f'Falha no Login. E-mail ou Senha Incorretos', 'alert-danger')
    return render_template('login.html', form_login=form_login)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/perfil', methods=['GET', 'POST'])
@login_required
def perfil():
    form_editar_perfil = FormEditarPerfil()

    if form_editar_perfil.validate_on_submit():
        print(current_user.email)
        print(current_user.username)

        current_user.email = form_editar_perfil.email.data
        current_user.username = form_editar_perfil.username.data
        database.session.commit()
        flash('Seu perfil foi atualizado com Sucesso', 'alert-success')

        return redirect(url_for('perfil'))

    elif request.method == "GET":
        form_editar_perfil.email.data = current_user.email
        form_editar_perfil.username.data = current_user.username

    return render_template('perfil.html', form_editar_perfil=form_editar_perfil)
