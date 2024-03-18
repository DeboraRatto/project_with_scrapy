from flask import Flask, request, jsonify
from google.cloud import bigquery
import os
from google.oauth2 import service_account

"""
Esta API foi desenvolvida usando a biblioteca Flask para criar um serviço web que permite realizar 
consultas por palavra-chave em uma tabela do BigQuery.

Características:
- A API oferece uma rota "/search" que aceita solicitações GET.
- Os usuários podem enviar uma palavra-chave como parâmetro na solicitação GET para buscar 
artigos correspondentes na tabela do BigQuery.
- A API executa uma consulta SQL na tabela do BigQuery, buscando artigos cujos títulos, 
subtítulos ou categorias contenham a palavra-chave fornecida.
- Os resultados da consulta são retornados no formato JSON.

Pré-requisitos:
- As credenciais de autenticação do BigQuery devem ser fornecidas por meio de um arquivo JSON 
localizado em um diretório específico (geralmente especificado no código).

Uso:
- Execute o script para iniciar o servidor Flask.
- Envie solicitações GET para a rota "/search", incluindo a palavra-chave desejada como um 
parâmetro na URL.
- A API retornará uma resposta JSON contendo os artigos correspondentes encontrados na tabela do 
BigQuery.

Observação:
- Certifique-se de que o serviço do BigQuery esteja configurado corretamente e que a tabela de 
destino contenha os dados necessários para consulta.

"""

app = Flask(__name__)

#Credenciais do BQ
dir_atual = os.path.dirname(__file__)
credential_path = os.path.join(dir_atual, '..', 'Credentials', 'credentials_bigquery.json')
credentials= service_account.Credentials.from_service_account_file(credential_path)

# Configurar o cliente BQ
client = bigquery.Client(credentials= credentials)

@app.route('/search', methods=['GET'])
def search_articles():
    # Obter o parâmetro da palavra-chave da solicitação
    keyword = request.args.get('keyword')
    if not keyword:
        return jsonify({'error': 'Palavra-chave não especificada'}), 400

    # Consulta para pesquisar artigos por palavra-chave na tabela BigQuery
    query = f"""
    SELECT * 
    FROM `smart-rope-417322.g1_news.News` 
    WHERE title like '%{keyword}%' 
    OR subtitle like '%{keyword}%' 
    OR category like '%{keyword}%'
    """

    # Executar a consulta no BigQuery
    results = client.query(query)

    # Converter os resultados em um formato JSON
    articles = [dict(row) for row in results]

    return jsonify({'articles': articles})

if __name__ == '__main__':
    app.run(debug=True)
