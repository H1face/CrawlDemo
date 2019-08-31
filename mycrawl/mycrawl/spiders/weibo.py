# -*- coding: utf-8 -*-
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from scrapy_redis.spiders import RedisCrawlSpider

import scrapy
from scrapy_redis.spiders import RedisSpider
import re
import time
from lxml import etree
from mycrawl.items import MycrawlItem

pageurl1 = '''https://weibo.com/p/100505{0}/follow?from=page_100505&wvr=6&mod=headfollow&ajaxpagelet=1&ajaxpagelet_v6=1
__ref=%2Fp%2F100505{0}%2Fhome%3Ffrom%3Dpage_100505%26mod%3DTAB%26is_hot%3D1%23place&_t=FM_{1}'''

pageurlN = '''https://weibo.com/p/100505{0}/follow?pids=Pl_Official_HisRelation__59&
page={2}&ajaxpagelet=1&ajaxpagelet_v6=1&
__ref=%2Fp%2F100505{0}%2Ffollow%3Ffrom%3Dpage_100505%26wvr%3D6%26mod%3Dheadfollow%23place&
_t=FM_{1}'''

userinfourl = '''https://weibo.com/p/100505{0}/info?mod=pedit_more
&ajaxpagelet=1&ajaxpagelet_v6=1
&__ref=%2Fu%2F{0}%3Frefer_flag%3D1005050006_%26is_hot%3D1&_t=FM_{1}'''


class MySpider(RedisSpider):
    name = 'weibomaster'
    redis_key = 'weibocrawler:start_urls'

    # allowed_domains = ['weibo.com']

    def parse(self, response):
        parttern = re.compile('https://weibo\.com/u/([0-9]+)')
        oid = parttern.findall(response.url)[0]
        # 构造  异步请求

        # 个人信息
        yield scrapy.Request(url=userinfourl.format(oid, int(time.time() * 100000)),meta={'url':response.url}, callback=self.userinfoparse)

        # 关注列表
        # for page in range(1, 6):
        #     if page == 1:
        #         yield scrapy.Request(url=pageurl1.format(oid, int(time.time() * 100000)),callback=self.userlinkparse)
        #     else:
        #         yield scrapy.Request(url=pageurlN.format(oid, page, int(time.time() * 100000)),
        #                              callback=self.userlinkparse)

    def userlinkparse(self, response):
        pass

    def userinfoparse(self, response):
        parttern = re.compile('<script>parent.FM.view\\((.*?)\\)</script>', flags=re.S)
        parttern1 = re.compile('"html":(.*?)}', flags=re.S)
        ret = parttern.findall(response.text)
        gfwlist=[]
        infodict={}
        for i in ret:
            html = parttern1.findall(i)
            if html:
                html = html[0]
                dom_tree = etree.HTML(html.replace("\\", ""))
                baseinfo = dom_tree.xpath("//div[@class='PCD_text_b PCD_text_b2']")  # 个人信息 浮动
                gfwinfo = dom_tree.xpath("//div[@class='PCD_counter']//strong")  # 关注,粉丝,微博数
                if gfwinfo:
                    for gfw in gfwinfo:
                        gfwlist.append(gfw.xpath("./text()")[0])
                if baseinfo:
                    for titlepattern in baseinfo:
                        title = titlepattern.xpath('.//h2/text()')[0]
                        info = titlepattern.xpath('string(.//ul)').replace(" ", "").replace('\n', "").replace('\r',
                                                                                                             "").replace(
                            'rn', '')
                        infodict[title]=info


        obj = MycrawlItem(guanzhu=gfwlist[0], fensi=gfwlist[1], weiboshu=gfwlist[2], link=response.meta['url'],
                          jibeninfo=infodict.get('基本信息','null'),lianxiinfo=infodict.get('联系信息','null'),
                          taginfo=infodict.get('标签信息', 'null'),jobinfo=infodict.get('工作信息', 'null'),
                          jyinfo=infodict.get('教育信息', 'null'),

                          )
        print(obj)
        yield obj


# 起始url

# 疯狗模式
# class MyCrawler(RedisCrawlSpider):
#     """Spider that reads urls from redis queue (myspider:start_urls)."""
#     name = 'weibo_master'
#     redis_key = 'webocrawler:start_urls'
#     # allowed_domains = ['weibo.com']
#
#     rules = (
#         # 用户主页面
#         Rule(LinkExtractor(), callback='parse_userlink', follow=True),
#         # Rule(LinkExtractor(allow=r'https://weibo.com/p/.*?/follow.*?'), callback='parse_page', follow=True),
#     )
#
#
#     def parse_userlink(self, response):
#         print(response.url)
