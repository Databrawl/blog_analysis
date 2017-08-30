import urllib.parse

import scrapy
from scrapy_splash import SplashRequest


class TrafficSpider(scrapy.Spider):
    name = 'traffic'
    allowed_domains = ['www.statshow.com']

    def __init__(self, blogs_data):
        super(TrafficSpider, self).__init__()
        self.blogs_data = blogs_data

    def start_requests(self):
        url_template = urllib.parse.urlunparse(
            ['http', self.allowed_domains[0], '/www/{path}', '', '', ''])
        for blog in self.blogs_data:
            url = url_template.format(path=blog['url'])
            request = SplashRequest(url, endpoint='render.html',
                                    args={'wait': 0.5}, meta={'blog': blog})
            yield request

    def parse(self, response):
        site_data = response.xpath('//div[@id="box_1"]/span/text()').extract()
        views_data = list(filter(lambda r: '$' not in r, site_data))
        if views_data:
            blog_data = response.meta.get('blog')
            traffic_data = {
                'daily_page_views': views_data[0].translate({ord(','): None}),
                'daily_visitors': views_data[1].translate({ord(','): None})
            }
            blog_data.update(traffic_data)
            yield blog_data
