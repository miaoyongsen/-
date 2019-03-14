import scrapy
from wangzhan.items import WangzhanItem
import re


class HttpbinSpider(scrapy.Spider):
    name = 'wang'
    allowed_domains = ['eco-city.gov.cn']
    start_urls = ['https://www.eco-city.gov.cn/index.html']  # 一级网址

    def parse(self, response):
        item = WangzhanItem()  # 倒入item
        url_st = response.xpath('//*/@href').extract()
        name_a = response.xpath('//*/text()').extract()  # 一级网址的所有文字
        names_a = [x.strip() for x in name_a]
        names_as = [x.strip() for x in names_a if x.strip() != '']
        a = ''.join(names_as)
        item['name'] = a
        #输出 一级网址所有文字

        url_new = []  # 所有二级网址
        while '' in url_st:
            url_st.remove('')
        for i in url_st:
            if i[0:4] != 'http':
                i = 'https://www.eco-city.gov.cn/' + i
            url_new.append(i)
        for url_two in url_new:
            yield scrapy.Request(url_two, callback=self.two_parse)
        yield item


    def two_parse(self, response):
        item = WangzhanItem()
        url_san = response.xpath('//*/@href').extract()
        name_b = response.xpath('//*/text()').extract()  # 二级所有文字
        names_b = [x.strip() for x in name_b]
        names_bs = [x.strip() for x in names_b if x.strip() != '']
        b = ''.join(names_bs)
        item['name'] = b
        #输出二级网址文字

        url_new_s = []  # 三级所有网址
        while '' in url_san:
            url_san.remove('')
        for i in url_san:
            if i[0:4] != 'http':
                i = 'https://www.eco-city.gov.cn/' + i
            url_new_s.append(i)
        for url_zuihou in url_new_s:
            yield scrapy.Request(url_zuihou, callback=self.san_parse)
        yield item



    def san_parse(self, response):
        item = WangzhanItem()

        name = response.xpath('//*/text()').extract()  # 三级所有文字
        name_c = [x.strip() for x in name]
        names_c = [x.strip() for x in name_c if x.strip() != '']
        c = ''.join(names_c)
        '''ci = ['VPN', '翻墙', '毒针', '毒箭', '氰化钾', '氯化琥珀胆碱', '异烟肼打狗', '毒针', '打狗', '药箭', '捕狗', '毒针', '药箭', '毒镖',
              '药', '麻醉箭', '神器', '吹针', '三步倒', '麻醉', '弩', '狗', '弓', '氰化钾', '琥珀胆碱', '买', '卖', '狗药', '毒', '镖', '氰化钠', '铊',
              '异烟肼']
        for ci_c in ci:
            shen_c = re.findall(ci_c, c)
            if shen_c != []:'''
        item['name'] = c

        yield item

