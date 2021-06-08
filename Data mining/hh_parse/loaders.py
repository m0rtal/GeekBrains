from urllib.parse import urljoin

from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, Join, MapCompose


def clear_salary(salary: str) -> str:
    try:
        result = salary.replace("\xa0", " ")
    except Exception as err:
        print(err)
        result = None
    return result


def make_author_link(author_href: str) -> str:
    return urljoin("https://hh.ru/", author_href) if author_href else None


def split_areas(areas: str) -> list:
    return areas.split(sep=", ")


class HhLoader(ItemLoader):
    default_item_class = dict
    title_out = TakeFirst()
    salary_in = MapCompose(clear_salary)
    salary_out = Join()
    description_out = Join()
    author_href_in = MapCompose(make_author_link)
    author_href_out = TakeFirst()


class HhAuthorLoader(ItemLoader):
    default_item_class = dict
    name_out = TakeFirst()
    author_url_out = TakeFirst()
    areas_in = MapCompose(split_areas)
    author_description_out = Join()
