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
- flask = 3.0.2

Além disso, é necessário configurar o ambiente para autenticar com o Google Cloud Platform e configurar um projeto no BigQuery.

## API

Este projeto também inclui uma API que permite pesquisar artigos extraídos no BigQuery por palavra-chave. A API foi desenvolvida usando Flask e permite que os usuários realizem consultas para buscar artigos específicos.

Para usar a API, siga estas etapas:

1. Certifique-se de que os pré-requisitos mencionados acima estejam instalados e configurados corretamente.
2. Inicie o servidor Flask executando o arquivo `create_api.py`.
3. Envie solicitações GET para a rota `/search` com a palavra-chave desejada como parâmetro na URL.
4. A API retornará uma resposta JSON contendo os artigos correspondentes encontrados na tabela do BigQuery.

Observação: Certifique-se de que o serviço do BigQuery esteja configurado corretamente e que a tabela de destino contenha os dados necessários para consulta.

## Instalação e Configuração
1. Clone o repositório:

~~~bash
git clone https://github.com/DeboraRatto/project_with_scrapy.git
cd project_with_scrapy
~~~

2. Configure a versão correta do python com pyenv:

~~~bash
pyenv install 3.12.1
pyenv local 3.12.1
~~~

3. Configure o poetry para versão do python acima e ative o ambiente virtual:

~~~bash
poetry env use 3.12.1
poetry shell
~~~

4. Instale as dependencias do projeto:

~~~bash
poetry install
~~~

5. Abra a pasta project_with_scrapy que acabou de copiar na sua IDE de preferencia e sega os próximos passos. 

6. Crie um projeto no Google BigQuery e uma tabela para armazenar as informações do arquivo json criado. 

7. Faça o download das credenciais do projeto criado no Google BigQuery, crie uma nova pasta dentro de project_with_scrapy e coloque esse arquivo das credenciais dentro dessa nova pasta criada: (arquivo de credenciais precisa ser json)

~~~bash
mkdir Credentials
~~~

8. Dentro do arquivo load.py, altere as informações de project_id, data_set_id e table_name de acordo com os nomes criados no seu projeto do BQ.

9. Se precisar, altere o nome do arquivo de credentials do BQ para o nome que você colocou no seu arquivo.

10. Execute o arquivo load.py

11. Verifique as informações na sua tabela do BQ. 

#### Configuração API:
12. Dentro do diretório API tem o arquivo create_api.py. Substitua o nome do arquivo de credenciais para autenticação correta e substitua a query para uma query que faça referencia a sua tabela do BQ. 

13. Execute o arquivo create_api.py, isso ativará o flask.

14. Faça uma consulta teste da API com a ferramenta que quiser, sugiro utilizar o postman, exemplo de endpoint:

~~~bash
http://localhost:5000/search?keyword=Tecnologia
~~~

