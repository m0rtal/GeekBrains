import scrapy
import pymongo


class AutoyoulaSpider(scrapy.Spider):
    name = 'autoyoula'
    allowed_domains = ['auto.youla.ru']
    start_urls = ['https://auto.youla.ru/']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_db = pymongo.MongoClient()
        self.db = self.client_db["gb_parse"]

    def _get_follow(self, response, selector_str, callback):
        for a_link in response.css(selector_str):
            url = a_link.attrib.get("href")
            yield response.follow(url, callback=callback)

    def parse(self, response):
        yield from self._get_follow(response,
                                    '.TransportMainFilters_brandsList__2tIkv a.blackLink',
                                    self.parse_brand
                                    )

    def parse_brand(self, response):
        yield from self._get_follow(response,
                                    ".Paginator_block__2XAPy a.Paginator_button__u1e7D",
                                    self.parse_brand
                                    )
        yield from self._get_follow(response,
                                    "a.SerpSnippet_name__3F7Yu",
                                    self.parse_car
                                    )

    def parse_car(self, response):
        title = response.css(".AdvertCard_advertTitle__1S1Ak::text").extract_first()
        images = [image.attrib.get("src") for image in response.css(".PhotoGallery_photoImage__2mHGn")]
        characteristics = [{
            "type": characteristic.css(".AdvertSpecs_label__2JHnS::text").extract_first(),
            "value": characteristic.css(".AdvertSpecs_data__xK2Qx::text").extract_first()
            }
            for characteristic in response.css(".AdvertSpecs_row__ljPcX")]
        description = response.css(".AdvertCard_descriptionInner__KnuRi::text").extract_first()
        author_href = response.css("a.SellerInfo_name__3Iz2N").attrib.get("href")

        payload = {"title": title,
                   "images": images,
                   "characteristics": characteristics,
                   "description": description,
                   "author_href": author_href
                   }

        self.db["youla"].insert_one(payload)
