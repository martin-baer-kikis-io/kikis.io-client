from twisted.internet import reactor, defer
#from scrapy.crawler import CrawlerRunner
#from scrapy.utils.log import configure_logging
#from scrapy.utils.project import get_project_settings


class Run_Spider_From_SubClass:

    def __init__(self, url_list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url_list = url_list

        #configure_logging()
        #self.runner = CrawlerRunner(get_project_settings())

    @defer.inlineCallbacks
    def crawl(self):
        for url in self.url_list:
            yield self.runner.crawl('MySpider', url=url)
        reactor.stop()

    def run_spider_in_loop(self):
        self.crawl()
        reactor.run()


urls = ['http://crossbar:8080', 'http://com.kikis.get']
runner = Run_Spider_From_SubClass(urls)
runner.run_spider_in_loop()
