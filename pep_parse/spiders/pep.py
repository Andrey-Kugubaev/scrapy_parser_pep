import re
import scrapy

from pep_parse.items import PepParseItem

pattern = r'(PEP \d+)'


class PepSpider(scrapy.Spider):

    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        pep_common_list = response.xpath('//*[@id="numerical-index"]')
        pep_links = pep_common_list.css(
            'a.pep.reference.internal::attr(href)'
        ).getall()
        for pep_link in pep_links:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        data = {
            'number': re.search(
                pattern,
                response.css('h1.page-title::text').get()
            ).groups(),
            'name': response.css('h1.page-title::text').get(),
            'status': response.css(
                'dt:contains("Status") + dd abbr::text'
            ).get()
        }
        yield PepParseItem(data)
