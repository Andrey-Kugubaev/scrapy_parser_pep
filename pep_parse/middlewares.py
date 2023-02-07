from scrapy import signals


class PepParseSpiderMiddleware:
    @classmethod
    def from_crawler(cls, crawler):
        project_spider = cls()
        crawler.signals.connect(project_spider.spider_opened, signal=signals.spider_opened)
        return project_spider

    def process_spider_input(self, response, spider):
        return None

    def process_spider_output(self, response, result, spider):
        for iterable_request in result:
            yield iterable_request

    def process_spider_exception(self, response, exception, spider):
        pass

    def process_start_requests(self, start_requests, spider):
        for one_request in start_requests:
            yield one_request

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class PepParseDownloaderMiddleware:
    @classmethod
    def from_crawler(cls, crawler):
        project_spider = cls()
        crawler.signals.connect(project_spider.spider_opened, signal=signals.spider_opened)
        return project_spider

    def process_request(self, request, spider):
        return None

    def process_response(self, request, response, spider):
        return response

    def process_exception(self, request, exception, spider):
        return None

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
