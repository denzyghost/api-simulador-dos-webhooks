<h1 align="center">API Simulador dos Webhooks</h1>

<p align="center">
  <img src="https://example.com/project-logo.png" alt="Project Logo" width="200" height="200">
</p>

Sistema receptor de webhooks<br />
url: https://simulador-dos-webhooks.up.railway.app/

## Finalidade do Projeto

Este sistema tem o propósito de receber webhooks de outro sistema, registrar esses webhooks recebidos, também registrando a hora exata do recebimento (em formato pt-br/São_Paulo, Brasil) e realizar alguma ação dependendo do status de cada webhook.

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

## Screenshots

Aqui estão algumas imagens do projeto:

![Screenshot 1](https://example.com/screenshot-1.png)
![Screenshot 2](https://example.com/screenshot-2.png)
![Screenshot 3](https://example.com/screenshot-3.png)

</details>
