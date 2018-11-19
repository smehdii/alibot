# -*- coding: utf-8 -*-
import scrapy


class SainsburysSpider(scrapy.Spider):
    name = 'basic'

    start_urls = [
        'https://www.sainsburys.co.uk/shop/gb/groceries/meat-fish/']

    def parse(self, response):
        urls = response.xpath(
            '//ul[@class="categories departments"]/li/a/@href').extract()
        for url in urls:
            yield response.follow(url, callback=self.parse_department_pages)
            print(url)

    def parse_department_pages(self, response):
        product_grid = response.xpath('//ul[@class=""productLister gridView]')

        if product_grid:
            for product in self.handle_product_listings(response):
                yield product
        # continue
        # pages = response.xpath('// ul[@class="categories shelf"]/li/a')
        # if not pages:
        #     pages = response.xpath('// ul[@class="categories aisles"]/li/a')

        # if not pages:
        #     # here is something fishy
        #     return
        # for url in pages:
        #     yield response.follow(url, callback=self.parse_department_pages)

    def handle_product_listings(self, response):
        urls = response.xpath(
            '//ul[@class="productLister gridView"]//li[@class="gridItem"]//h3/a')
        for url in urls:
            yield
