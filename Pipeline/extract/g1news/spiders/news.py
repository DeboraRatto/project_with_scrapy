import scrapy
from scrapy_splash import SplashRequest

class NewsSpider(scrapy.Spider):
    name = "g1news"
    start_urls = ["https://g1.globo.com/politica/noticia/2024/03/16/principais-pontos-quatro-depoimentos-bolsonaro-tentativa-golpe.ghtml",
                  "https://g1.globo.com/economia/imposto-de-renda/noticia/2024/03/16/imposto-de-renda-2024-receita-recebe-mais-de-1-milhao-de-declaracoes-no-primeiro-dia.ghtml",
                  "https://g1.globo.com/tecnologia/noticia/2024/03/16/tiktok-sob-pressao-quem-e-o-dono-do-app-e-por-que-a-rede-desperta-desconfianca-de-politicos-nos-eua.ghtml",
                  "https://g1.globo.com/sp/sao-paulo/noticia/2024/03/16/salario-de-r-1500-e-meta-de-30-cortes-de-energia-por-dia-a-rotina-dos-terceirizados-da-enel-que-sao-constantemente-ameacados-em-sp.ghtml",
                  "https://g1.globo.com/economia/noticia/2024/03/16/consumidor-ficou-em-media-104-horas-sem-energia-em-2023-veja-ranking-de-distribuidoras-com-melhores-e-piores-desempenhos.ghtml",
                  "https://g1.globo.com/economia/negocios/noticia/2024/03/16/entenda-por-que-o-governo-nao-quis-que-a-petrobras-distribuisse-os-dividendos-extraordinarios.ghtml",
                  "https://g1.globo.com/meio-ambiente/noticia/2024/03/16/onda-de-calor-ultimo-fim-de-semana-do-verao-tem-temperaturas-elevadas-em-boa-parte-do-pais.ghtml",
                  "https://g1.globo.com/sp/noticia/2024/03/16/datafolha-84percent-dos-moradores-de-sp-reclamam-de-buracos-no-asfalto.ghtml",
                  "https://g1.globo.com/mundo/noticia/2024/03/14/mais-de-4-mil-ogivas-armazenadas-e-maleta-que-fica-com-putin-russia-tem-arsenal-nuclear-capaz-de-destruir-o-mundo-varias-vezes.ghtml",
                  "https://g1.globo.com/economia/imposto-de-renda/noticia/2024/03/06/imposto-de-renda-2024-receita-divulga-as-regras-veja-quem-e-obrigado-a-declarar.ghtml"]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse,
                args={
                    'wait': 10,
                })  
    
    def parse(self, response):
        yield{
            'title': response.css('.content-head__title::text').get(),
            'url': response.css('link[itemprop="mainEntityOfPage"]::attr(href)').get(),
            'subtitle': response.css('.content-head__subtitle::text').get(),
            'author': response.css('.content-publication-data__from::attr(title)').get(),
            'publication_date': response.css('.content-publication-data__updated > time::attr(datetime)').get(),
            'category': response.css('.header-editoria--link::text').get()
        }
