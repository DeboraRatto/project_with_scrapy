## Web scraping com Scrapy

Este projeto consiste em um web scraping desenvolvido em Python usando o framework Scrapy, que extrai informações do site do G1 (g1.globo.com) e as carrega em uma tabela no Google BigQuery.

## Funcionalidades

- O web scraper busca notícias do site do G1 em várias seções, como Tecnologia, Política, Economia, entre outras.
- As informações coletadas incluem título, data de publicação, autor, conteúdo e categoria da notícia.
- Os dados extraídos são armazenados em um arquivo JSON.
- Um script carrega o arquivo JSON para uma tabela no BigQuery para análise posterior.

## Requisitos

Antes de executar o projeto, você precisará instalar os seguintes itens:

- python = 3.12.1
- scrapy = 2.11.1
- scrapy-splash = 0.9.0
- google-cloud-bigquery = 3.19.0
- pandas = 2.2.1
- pandas-gbq = 0.22.0

Além disso, é necessário configurar o ambiente para autenticar com o Google Cloud Platform e configurar um projeto no BigQuery.


