# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

mycookie='SINAGLOBAL=3421616684015.8022.1553341957702; YF-V5-G0=27518b2dd3c605fe277ffc0b4f0575b3; _s_tentry=-; Apache=7384080538721.845.1560491267723; ULV=1560491268670:2:1:1:7384080538721.845.1560491267723:1553341957713; Ugrow-G0=5c7144e56a57a456abed1d1511ad79e8; TC-Page-G0=c4376343b8c98031e29230e0923842a5|1563515423|1563515423; TC-V5-G0=4e714161a27175839f5a8e7411c8b98c; login_sid_t=b8c891f44a7796ade4811399a8931ea3; cross_origin_proto=SSL; WBtopGlobal_register_version=307744aa77dd5677; wb_view_log=1920*10801; UOR=,,graph.qq.com; SCF=Ap2R5FUd7cMhzjpENYwuxB1rp5-YfOf0E-VWPgO0qXJRUVA8x6Fvxe-QkqJGrWJcPtz7jfiH6IlqzvY61phdlGE.; SUB=_2A25wbLmcDeRhGeNJ6VER8ijPyjSIHXVTG6xUrDV8PUNbmtBeLXTYkW9NS_yBOzkJhCiATvVeHwhE5Ubh0pQ8tUn6; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFf1rjr6QrnVVwMgQP9Dg9f5JpX5K2hUgL.Fo-Neoe7eoq0eKn2dJLoIE2LxKML1-BLBK2LxKnLBo-LBoMLxK-L1KMLBKykSK-feKBt; SUHB=0wn1psQVQyAacV; ALF=1567753291; SSOLoginState=1567148492; un=15606907698; wb_view_log_5723026318=1920*10801; YF-Page-G0=aac25801fada32565f5c5e59c7bd227b|1567150693|1567150641; webim_unReadCount=%7B%22time%22%3A1567151129933%2C%22dm_pub_total%22%3A1%2C%22chat_group_client%22%3A0%2C%22allcountNum%22%3A8%2C%22msgbox%22%3A0%7D'
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

ret = cookieserialize(mycookie)

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
        request.cookies=ret
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
