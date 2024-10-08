# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CninfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Transaction_date = scrapy.Field()  # 交易日期
    market = scrapy.Field()  # 交易所
    minimum_price = scrapy.Field()  # 最低价
    currency = scrapy.Field()  # 币种
    ups_downs = scrapy.Field() #涨跌
    Highest_price = scrapy.Field()  # 最高价
    Securities_abbreviation = scrapy.Field()  # 证券简称
    Opening_price = scrapy.Field()  # 开盘价
    price_limit = scrapy.Field()  # 涨跌幅
    trading_volume = scrapy.Field() #成交金额
    Securities_code = scrapy.Field()  # 证券代码
    Number_of_transactions = scrapy.Field()  # 成交数量
    Closing_price = scrapy.Field()  # 收盘价
    Last_Modified = scrapy.Field() #网页修改时间

    pass
