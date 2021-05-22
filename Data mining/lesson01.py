import json
import random
import time
from pathlib import Path

import requests

"""
Источник: https://5ka.ru/special_offers/
Задача организовать сбор данных,
необходимо иметь метод сохранения данных в .json файлы
результат: Данные скачиваются с источника, при вызове метода/функции сохранения в файл скачанные данные сохраняются в 
Json файлы, для каждой категории товаров должен быть создан отдельный файл и содержать товары исключительно 
соответсвующие данной категории.

пример структуры данных для файла:
нейминг ключей можно делать отличным от примера
{
    "name": "имя категории",
    "code": "Код соответсвующий категории (используется в запросах)",
    "products": [{PRODUCT}, {PRODUCT}........] # список словарей товаров соответсвующих данной категории
}
"""


class Parse5ka:
    def __init__(self, start_url: str, save_path: Path):
        self.save_path = save_path
        self.start_url = start_url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"
        }
        self.special_offers = "special_offers/"
        self.categories = "categories/"
        self.params = {
            "store": "363H",
        }

    def run(self):
        for product in self._parse_response(self.start_url + self.special_offers):
            file_path = self.save_path.joinpath(f"{product['id']}.json")
            self._save(product, file_path)

    def _parse_response(self, url):
        while url:
            response = self._get_response(url)
            data: dict = response.json()
            url = data["next"]
            for item in data["results"]:
                yield item

    def _get_response(self, url):
        while True:
            response = requests.get(url, headers=self.headers, params=self.params)
            if response.status_code == 200:
                return response
            time.sleep(random.randint(1, 3))

    def _save(self, data: dict, file_path: Path):
        if self.__class__.__name__ == "Parse5ka":
            file_path.write_text(json.dumps(data, ensure_ascii=False, indent=4))
        if self.__class__.__name__ == "ParseCategories":
            category = self.params["categories"]
            category_name = self.params["category_name"]
            new_file_path = file_path.parent.joinpath(f"{category}.json")
            payload = {
                "name": category_name,
                "code": category,
                "products": [data["id"], ]
            }
            if not new_file_path.exists():
                new_file_path.write_text(json.dumps(payload, ensure_ascii=False, indent=4))
            else:
                existing_data = json.loads(new_file_path.read_text())
                existing_data["products"].append(data["id"])
                new_file_path.write_text(json.dumps(existing_data, ensure_ascii=False, indent=4))


class ParseCategories(Parse5ka):
    def run(self):
        for category_code, category_name in self._parse_categories(self.start_url + self.categories):
            self.params["categories"] = category_code
            self.params["category_name"] = category_name
            super().run()

    def _parse_categories(self, url):
        response = self._get_response(url)
        data: dict = response.json()
        for item in data:
            yield item["parent_group_code"], item["parent_group_name"]


def get_save_path(dir_name: str) -> Path:
    save_path = Path(__file__).parent.joinpath(dir_name)
    if not save_path.exists():
        save_path.mkdir()
    return save_path


if __name__ == "__main__":
    product_path = get_save_path("categories")

    parser = ParseCategories("https://5ka.ru/api/v2/", product_path)
    parser.run()
