from simulador_dos_webhooks import database, login_manager
from datetime import datetime
from flask_login import UserMixin
from pytz import timezone


@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))


def get_current_datetime():
    tz = timezone('America/Sao_Paulo')
    data = datetime.now(tz)
    return data.strftime("%d-%m-%Y %H:%M:%S")


class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    password = database.Column(database.String, nullable=False)
    token = database.Column(database.String, nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.username


class Webhook(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String, default='-')
    email = database.Column(database.String, default='-')
    status = database.Column(database.String, default='-')
    valor = database.Column(database.Integer, default='-')
    forma_pagamento = database.Column(database.String, default='-')
    parcelas = database.Column(database.Integer, default='-')
    data = database.Column(database.String, default=get_current_datetime)
    tratativa = database.Column(database.String, default='-')
