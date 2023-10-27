<h1 align="center">API Simulador de Webhooks</h1>

<p align="center">
  <img src="https://user-images.githubusercontent.com/108025321/239703028-0c14b0b7-5ed8-408b-810b-b385a56c7e94.jpg" alt="Project Logo" width="550" height="350">
</p>

Sistema receptor de webhooks<br />
url: https://simulador-dos-webhooks.up.railway.app/

## Finalidade do Projeto

Este sistema tem o propósito de receber webhooks de outro sistema, registrar esses webhooks recebidos, também registrando a hora exata do recebimento (em timezone America/Sao_Paulo) e realizar alguma ação dependendo do status de cada webhook.

O sistema é protegido por autenticação e exige um token de acesso. Primordialmente, o sistema contém uma página principal de exibição de todos os webhooks e o tratamento realizado para cada um desses webhooks. Além disso, o sistema faz um print internamente simulando o que deverá ser feito com cada usuário mediate ao status recebido por meio do webhook.

Na página principal de exibição, foi desenvolvido um filtro para todas as colunas, basta selecionar a coluna e digitar um valor. E complementarmente, desenvolvi uma funcionalidade de download de todos os webhooks registrados pelo sistema, em um arquivo CSV já codificado em utf-8, para a fácil importação desses dados em outros sistemas, ou para que seja possível realizar análises nos dados por meio do Excel.

## Tecnologias Utilizadas

- Python 3.11.2
- Micro-framework Flask 2.3.2
- HTML, CSS e JavaScript

## Servidor

O projeto está hospedado na plataforma Railway, disponível em [https://railway.app/](https://railway.app/).

## Banco de Dados

Utilizei o banco de dados Postgres para armazenar os webhooks registrados.

## Imagens

Aqui estão algumas imagens do projeto:

![api-simulador-dos-webhooks-results](https://github.com/Dhytm/api-simulador-dos-webhooks/assets/108025321/fd48c6de-2aca-4e54-8943-3e0224d0a38f)
![api-simulador-dos-webhooks-server](https://github.com/Dhytm/api-simulador-dos-webhooks/assets/108025321/f71429bd-7cb4-42e3-86c7-143597839b05)
![api-simulador-dos-webhooks-login](https://github.com/Dhytm/api-simulador-dos-webhooks/assets/108025321/20270744-8d17-4bce-af72-9489407af679)
![api-simulador-dos-webhooks-csv](https://github.com/Dhytm/api-simulador-dos-webhooks/assets/108025321/de614ba4-0b46-4666-ab32-86117fdbe219)
![api-simulador-dos-webhooks-filter](https://github.com/Dhytm/api-simulador-dos-webhooks/assets/108025321/e9afa934-735b-4168-9da5-9ceef02a9666)
</details>
