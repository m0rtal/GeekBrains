import scrapy
from .xpath_selectors import PAGINATION, JOBS, JOB_DATA, AUTHOR, AUTHOR_DATA
from ..loaders import HhLoader, HhAuthorLoader


class HhSpider(scrapy.Spider):
    name = 'hh'
    allowed_domains = ['hh.ru']
    start_urls = ['https://hh.ru/search/vacancy?schedule=remote&L_profession_id=0&area=113']

    def _get_follow(self, response, selector_string, callback):
        for a_link in response.xpath(selector_string):
            yield response.follow(a_link, callback=callback)

    # пагинация
    def parse(self, response):
        yield from self._get_follow(
            response,
            PAGINATION["selector"],
            getattr(self, PAGINATION["callback"]))

    def parse_jobs(self, response):
        # сбор ссылок на вакансии
        yield from self._get_follow(
            response,
            JOBS["selector"],
            getattr(self, JOBS["callback"])
        )

    def parse_job(self, response):
        # парсинг вакансии
        loader = HhLoader(response=response)
        for key, value in JOB_DATA.items():
            loader.add_xpath(key, value)
        yield loader.load_item()
        yield response.follow(loader.load_item()['author_href'], callback=self.parse_author)

    def parse_author(self, response):
        # сбор информации об авторе
        loader = HhAuthorLoader(response=response)
        for key, value in AUTHOR_DATA.items():
            loader.add_xpath(key, value)
        yield loader.load_item()

        # сбор ссылок на вакансии у авторов
        yield from self._get_follow(
            response,
            AUTHOR["selector"],
            getattr(self, AUTHOR["callback"])
        )
