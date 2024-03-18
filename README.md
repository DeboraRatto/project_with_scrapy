## Web scraping com Scrapy

Este projeto consiste em um web scraping desenvolvido em Python usando o framework Scrapy, que extrai informações do site do G1 (g1.globo.com) e as carrega em uma tabela no Google BigQuery.

## Funcionalidades

- O web scraper busca notícias do site do G1 em várias seções, como Tecnologia, Política, Economia, entre outras. (código que executa essa parte está em Pipeline/extract/g1news/spiders/news.py)
- As informações coletadas incluem título, data de publicação, autor, conteúdo e categoria da notícia.
- Os dados extraídos são armazenados em um arquivo JSON.(arquivo dentro da pasta Pipeline/extract)
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

## API

Este projeto também inclui uma API que permite pesquisar artigos extraídos no BigQuery por palavra-chave. A API foi desenvolvida usando Flask e permite que os usuários realizem consultas para buscar artigos específicos.

Para usar a API, siga estas etapas:

1. Certifique-se de que os pré-requisitos mencionados acima estejam instalados e configurados corretamente.
2. Inicie o servidor Flask executando o arquivo `create_api.py`.
3. Envie solicitações GET para a rota `/search` com a palavra-chave desejada como parâmetro na URL.
4. A API retornará uma resposta JSON contendo os artigos correspondentes encontrados na tabela do BigQuery.

Observação: Certifique-se de que o serviço do BigQuery esteja configurado corretamente e que a tabela de destino contenha os dados necessários para consulta.


