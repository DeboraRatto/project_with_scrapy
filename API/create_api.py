from flask import Flask, request, jsonify
from google.cloud import bigquery
import os
from google.oauth2 import service_account

app = Flask(__name__)

dir_atual = os.path.dirname(__file__)
credential_path = os.path.join(dir_atual, '..', 'Credentials', 'credentials_bigquery.json')
credentials= service_account.Credentials.from_service_account_file(credential_path)

# Configurar o cliente BigQuery
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
