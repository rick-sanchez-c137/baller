from twisted.internet import reactor
from baller.spiders import BallerSpider
from scrapy.crawler import CrawlerRunner

def run_crawl():
    """
    Run a spider within Twisted. Once it completes,
    wait 5 seconds and run another spider.
    """
    runner = CrawlerRunner({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        })
    deferred = runner.crawl(QuotesSpider)
    # you can use reactor.callLater or task.deferLater to schedule a function
    deferred.addCallback(reactor.callLater, 5, run_crawl)
    return deferred

run_crawl()
reactor.run()   # you have to run the reactor yourself