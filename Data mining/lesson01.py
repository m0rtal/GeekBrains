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


def get_save_path(dir_name: str) -> Path:
    save_path = Path(__file__).parent.joinpath(dir_name)
    if not save_path.exists():
        save_path.mkdir()
    return save_path


class Parse5ka:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"
        }
        self.params = {
            "store": "363H",
        }

    def get_response(self, url, category=None):
        if category:
            self.params["categories"] = category
        while True:
            response = requests.get(url, headers=self.headers, params=self.params)
            if response.status_code == 200:
                return response
            time.sleep(random.randint(1, 3))

    def parse_response(self, url, category):
        while url:
            response = self.get_response(url, category)
            data: dict = response.json()
            url = data["next"]
            for item in data["results"]:
                yield item

    def run(self, url: str, categories: list, save_path: Path):
        for category in categories:
            for item in self.parse_response(url, category["parent_group_code"]):
                file_path = save_path.joinpath(f"{item['id']}.json")
                self._save(item, category, file_path)

    @staticmethod
    def _save(data: dict, category: dict, file_path: Path):
        cat_num = category["parent_group_code"]
        cat_name = category["parent_group_name"]
        new_file_path = file_path.parent.joinpath(f"{cat_num}.json")
        payload = {
            "name": cat_name,
            "code": cat_num,
            "products": [data, ]
        }
        if not new_file_path.exists():
            new_file_path.write_text(json.dumps(payload, ensure_ascii=False, indent=4))
        else:
            existing_data = json.loads(new_file_path.read_text())
            existing_data["products"].append(data)
            new_file_path.write_text(json.dumps(existing_data, ensure_ascii=False, indent=4))


special_offers = "special_offers/"
categories = "categories/"
url = "https://5ka.ru/api/v2/"

save_path = get_save_path("categories")

if __name__ == "__main__":
    parser = Parse5ka()
    categories = parser.get_response(url + categories).json()
    parser.run(url+special_offers, categories, save_path)
