import pandas as pd
import os
from google.cloud import bigquery
from google.oauth2 import service_account


# Obtendo o diretório atual do script
dir_atual = os.path.dirname(__file__)
# Construindo o caminho completo para o arquivo JSON
caminho_json_news = os.path.join(dir_atual, 'extract', 'g1news.json')

# Autenticando com as credenciais do Google Cloud
credentials = service_account.Credentials.from_service_account_file('Credentials\credentials_bigquery.json')

# Definindo as informações da tabela do BigQuery
projeto_id = 'smart-rope-417322'
conjunto_de_dados_id = 'g1_news'
nome_tabela = 'News'

# Carregando o DataFrame do pandas
df = pd.read_json(caminho_json_news)

# Carregando o DataFrame na tabela do BigQuery
df.to_gbq(destination_table=f'{projeto_id}.{conjunto_de_dados_id}.{nome_tabela}',
          project_id=projeto_id,
          credentials=credentials,
          if_exists='replace')  # Substituir a tabela se ela já existir


