# -*- coding: utf-8 -*-
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from scrapy_redis.spiders import RedisCrawlSpider

import re
import time
import scrapy
from lxml import etree
from scrapy_redis.spiders import RedisSpider
from mycrawl.redispool import redis_conn

fensipage1='''https://weibo.com/p/1005051879601851/follow?
relate=fans&from=100505&wvr=6&
mod=headfans&current=fans&ajaxpagelet=1&ajaxpagelet_v6=1&__ref=%2Fu%2F1879601851%3Frefer_flag%3D1005050008_%26is_hot%3D1&_t=FM_156734379264022'''

pageurl1 = '''https://weibo.com/p/100505{0}/follow?from=page_100505&wvr=6&mod=headfollow&ajaxpagelet=1&ajaxpagelet_v6=1
__ref=%2Fp%2F100505{0}%2Fhome%3Ffrom%3Dpage_100505%26mod%3DTAB%26is_hot%3D1%23place&_t=FM_{1}'''
pageurlN = '''https://weibo.com/p/100505{0}/follow?pids=Pl_Official_HisRelation__59&
page={2}&ajaxpagelet=1&ajaxpagelet_v6=1&
__ref=%2Fp%2F100505{0}%2Ffollow%3Ffrom%3Dpage_100505%26wvr%3D6%26mod%3Dheadfollow%23place&
_t=FM_{1}'''
userinfourl = '''https://weibo.com/p/100505{0}/info?mod=pedit_more
&ajaxpagelet=1&ajaxpagelet_v6=1
&__ref=%2Fu%2F{0}%3Frefer_flag%3D1005050006_%26is_hot%3D1&_t=FM_{1}'''
usermainurl='''https://weibo.com/u/{0}?refer_flag=1005050008_&is_hot=1'''
parttern_mainurl = re.compile('https://weibo\.com/u/([0-9]+)')
parttern_1 = re.compile('<script>parent.FM.view\\((.*?)\\)</script>', flags=re.S)
parttern_2=re.compile('"html":(.*?)}', flags=re.S)
parttern_3 = re.compile('uid=([0-9]+)&')

class MySpider(RedisSpider):
    name = 'weibomaster'
    redis_key = 'weibocrawler:start_urls'
    allowed_domains = ['weibo.com']

    def parse(self, response):
        parttern = parttern_mainurl
        oid = parttern.findall(response.url)[0]
        # 构造  异步请求

        # 个人信息
        url=userinfourl.format(oid, int(time.time() * 100000))
        redis_conn.lpush("weibomaster:infourl", url)


        # 关注列表
        for page in range(1, 6):#写死了，不一定有5页,这里感觉用粉丝更好不该用关注找
            if page == 1:
                yield scrapy.Request(url=pageurl1.format(oid, int(time.time() * 100000)),callback=self.userlinkparsepage1)
            else:
                yield scrapy.Request(url=pageurlN.format(oid, int(time.time() * 100000), page),
                                     callback=self.userlinkparsepageN)

    def userlinkparsepage1(self, response):
        ret = parttern_1.findall(response.text)
        for item in ret:
            html2 = parttern_2.findall(item)
            if html2:
                html2=html2[0]
                dom_tree = etree.HTML(html2.replace("\\", ""))
                userlink = dom_tree.xpath("//li[@class='follow_item S_line2']/@action-data")
                if userlink:
                    for i in userlink:
                        uid = parttern_3.match(i)
                        if uid:
                            uid = uid.group(1)
                            yield scrapy.Request(url=usermainurl.format(uid))


    def userlinkparsepageN(self, response):
        ret = parttern_1.findall(response.text)[0]
        html = parttern_2.findall(ret)[0]
        dom_tree = etree.HTML(html.replace("\\", ""))
        userlink = dom_tree.xpath("//li[@class='follow_item S_line2']/@action-data")
        for i in userlink:
            uid = parttern_3.match(i)
            if uid:#个别非数字id
                uid=uid.group(1)
                yield scrapy.Request(url=usermainurl.format(uid))




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
