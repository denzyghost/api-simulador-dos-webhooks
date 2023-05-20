from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from simulador_dos_webhooks.models import Usuario
from flask_login import current_user


class FormCriarConta(FlaskForm):
    username = StringField('Nome de usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    password_confirmation = PasswordField('Confirmação da Senha', validators=[DataRequired(), EqualTo('password')])
    token = StringField('Token de acesso', validators=[DataRequired()])
    button_submit_create_acount = SubmitField('Criar conta')

    @staticmethod
    def validar_email(email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('E-mail já cadastrado. Cadastre-se com outro e-mail ou faça login para continuar.')

    @staticmethod
    def validar_token(token):
        if token.data != "uhdfaAADF123":
            raise ValidationError('Token inserido inválido!')


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    token = StringField('Token de acesso', validators=[DataRequired()])
    remember_info = BooleanField('Lembrar Dados de Acesso')
    button_submit_login = SubmitField('Fazer login')


class FormEditarPerfil(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    button_submit_edit_profile = SubmitField('Confirmar modificações')

    def validar_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError('E-mail já cadastrado. Cadastre-se com outro e-mail ou faça login para continuar.')
