import requests
import json

webhook_url = 'http://127.0.0.1:5000/iwpdosyoakwccrwfcdakpfuyrobpxeucqbvhorrdorsrrjvefy'

data = {
    "nome": "Verkeh",
    "email": "verkeh@corp.com",
    "status": "aprovado",
    "valor": 870,
    "forma_pagamento": "paypal",
    "parcelas": 5,
}

r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
