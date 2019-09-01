# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

mycookie='SINAGLOBAL=3421616684015.8022.1553341957702; YF-V5-G0=27518b2dd3c605fe277ffc0b4f0575b3; _s_tentry=-; Apache=7384080538721.845.1560491267723; ULV=1560491268670:2:1:1:7384080538721.845.1560491267723:1553341957713; Ugrow-G0=5c7144e56a57a456abed1d1511ad79e8; TC-Page-G0=c4376343b8c98031e29230e0923842a5|1563515423|1563515423; TC-V5-G0=4e714161a27175839f5a8e7411c8b98c; login_sid_t=b8c891f44a7796ade4811399a8931ea3; cross_origin_proto=SSL; WBtopGlobal_register_version=307744aa77dd5677; SSOLoginState=1567148492; un=15606907698; UOR=,,www.guofenchaxun.com; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFf1rjr6QrnVVwMgQP9Dg9f5JpX5K-hUgL.Fo-Neoe7eoq0eKn2dJLoIE2LxKML1-BLBK2LxKnLBo-LBoMLxK-L1KMLBKykSK-feKBt; ALF=1598771763; wvr=6; wb_view_log_5723026318=1920*10801; wb_view_log=1920*10801; SCF=Ap2R5FUd7cMhzjpENYwuxB1rp5-YfOf0E-VWPgO0qXJRbHzTlTdDMEX_4RyFfb7vLw6xIEBOzyYE5wjsA2AktI4.; SUB=_2A25wbu9WDeRhGeNJ6VER8ijPyjSIHXVTGkeerDV8PUJbmtBeLWTMkW9NS_yBOyGyQzG2hU5xeV6_TeaQAQBPt2sD; SUHB=09P9eXkbagqtc8; YF-Page-G0=761bd8cde5c9cef594414e10263abf81|1567268614|1567268484; webim_unReadCount=%7B%22time%22%3A1567268634923%2C%22dm_pub_total%22%3A1%2C%22chat_group_client%22%3A0%2C%22allcountNum%22%3A13%2C%22msgbox%22%3A0%7D'
mycookie1='Ugrow-G0=1ac418838b431e81ff2d99457147068c; login_sid_t=ba5d79eb633971cbe2a3069b1dfd44ce; cross_origin_proto=SSL; YF-V5-G0=8c4aa275e8793f05bfb8641c780e617b; WBStorage=f54cf4e4362237da|undefined; _s_tentry=passport.weibo.com; wb_view_log=1920*10801; Apache=4931562183850.195.1567342025473; SINAGLOBAL=4931562183850.195.1567342025473; ULV=1567342025481:1:1:1:4931562183850.195.1567342025473:; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh8-1bMv9ayDxQKB0xKO.ni5JpX5K2hUgL.Fo-Eeo.EShMfe0z2dJLoI0qLxKBLBonL12BLxKnLB.qLBoMLxK.L1h5L1KBLxKML1-2L1hBLxKMLB.-L122LxKMLB.-L1KBt; ALF=1598878040; SSOLoginState=1567342041; SCF=AiqaUs1khBXFk4bZwhUGDW53Au4brdyKDB1eZJBX4tXCV2UfHZpQj6RH45Y5BP_NisFjWnYILzv0bYKiP4YTeso.; SUB=_2A25wb82JDeRhGeNM6VsT9CnJyD6IHXVTHLhBrDV8PUNbmtBeLWbGkW9NTiROLo3-lJ8YfQxGxCkHwzJUpCm-sYVh; SUHB=04WeumiqU9GmqO; un=13735357017; wvr=6; wb_view_log_5229247532=1920*10801; YF-Page-G0=112e41ab9e0875e1b6850404cae8fa0e|1567342068|1567342043; webim_unReadCount=%7B%22time%22%3A1567342080686%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22allcountNum%22%3A3%2C%22msgbox%22%3A0%7D'
def cookieserialize(cookie):
    dict_ = {}
    ret = cookie.split(';')

    for item in ret:
        try:
            key, value = item.split('=')
            dict_[key.strip()] = value.strip()
        except ValueError:
            key, value = item.split('=', 1)
            dict_[key.strip()] = value.strip()
    return dict_

# ret = cookieserialize(mycookie)

import random

class Proxyuser():
    userpool=[
        cookieserialize(mycookie),cookieserialize(mycookie1)
           ]
    def __getattr__(self, name):
        return Proxyuser.name[random.randint(0,1)]

pool=Proxyuser()

from scrapy import signals


class MycrawlSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class MycrawlDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        request.cookies=pool.userpool[0]


        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
