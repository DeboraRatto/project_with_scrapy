import pandas as pd
import os
from google.cloud import bigquery
from google.oauth2 import service_account

"""
função que Autentica no Google BigQuery utilizando as credenciais fornecidas no arquivo JSON.
Args: credential_path (str): O caminho para o arquivo JSON
Return: As credenciais autenticadas do Google BigQuery.
"""
def authenticate_bigquery(credential_path):
    return service_account.Credentials.from_service_account_file(credential_path)

"""
função que carrega um arquivo JSON em um DataFrame do Pandas.
Args:extract_json_path (str): O caminho para o arquivo JSON a ser carregado.
Return: O DataFrame carregado a partir do arquivo JSON.
"""

def load_dataframe(extract_json_path):
    return pd.read_json(extract_json_path)

"""
função que carrega um DataFrame do Pandas em uma tabela do Google BigQuery.
Args:
        df (pandas.DataFrame): O DataFrame a ser carregado no BigQuery.
        project_id (str): O ID do projeto do Google Cloud.
        data_set_id (str): O ID do conjunto de dados do BigQuery.
        table_name (str): O nome da tabela do BigQuery.
        credentials (google.auth.credentials.Credentials): As credenciais autenticadas do Google BigQuery.

Return: O objeto representando o trabalho de carregamento no BigQuery.
"""

def load_data_bigquery(df, project_id, data_set_id, table_name, credentials):
    load_bq= df.to_gbq(destination_table=f'{project_id}.{data_set_id}.{table_name}',
                    project_id=project_id,
                    credentials=credentials,
                    if_exists='replace')  # Substituir a tabela se ela já existir
    return load_bq


if __name__ == '__main__':
    # Obtem o diretório atual do script, o caminho do json extract e caminho das credenciais
    dir_atual = os.path.dirname(__file__)
    json_path_news = os.path.join(dir_atual, 'extract', 'g1news.json')
    if not os.path.exists(json_path_news): #verifica a existencia
        raise FileNotFoundError(f'O arquivo JSON {json_path_news} não foi encontrado.')

    credential_path = os.path.join(dir_atual, '..', 'Credentials', 'credentials_bigquery.json')

    # Define as informações da tabela do BigQuery
    project_id = 'smart-rope-417322'
    data_set_id = 'g1_news'
    table_name = 'News'

    Credentials= authenticate_bigquery(credential_path)

    df= load_dataframe(json_path_news)

    load_data_bigquery(df, project_id, data_set_id, table_name,Credentials)