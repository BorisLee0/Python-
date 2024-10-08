import scrapy
from cninfo.items import CninfoItem

class SpiderSpider(scrapy.Spider):
    name = "spider"
    allowed_domains = ["cninfo.com.cn"]
    start_urls = ["http://cninfo.com.cn/"]

    def start_requests(self):
        data = {
            'tdate': '2024-09-30',
            'market': 'SZE',
        }
        url = 'http://webapi.cninfo.com.cn/api/sysapi/p_sysapi1007'
        yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse)

    def parse(self, response):
        p = response.json()
        if p != None:
            data = p.get('records')
            for i in data:
                item = CninfoItem()
                item['Transaction_date'] = i.get('交易日期')
                item['market'] = i.get('交易所')
                item['minimum_price'] = i.get('最低价')
                item['currency'] = i.get('币种')
                item['ups_downs'] = i.get('涨跌')
                item['Highest_price'] = i.get('最高价')
                item['Securities_abbreviation'] = i.get('证券简称')
                item['Opening_price'] = i.get('开盘价')
                item['price_limit'] = i.get('涨跌幅')
                item['trading_volume'] = i.get('成交金额')
                item['Securities_code'] = i.get('证券代码')
                item['Number_of_transactions'] = i.get('成交数量')
                item['Closing_price'] = i.get('收盘价')
                item['Last_Modified'] = "Sun, 06 Oct 2024 01:12:57 GMT"
                yield item

