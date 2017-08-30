import urllib.parse

import scrapy
from scrapy_splash import SplashRequest


class BlogsSpider(scrapy.Spider):
    name = 'blogs'
    allowed_domains = ['cse.google.com']

    def __init__(self, queries):
        super(BlogsSpider, self).__init__()
        self.queries = queries

    def start_requests(self):
        params_dict = {
            'cx': ['partner-pub-9634067433254658:5laonibews6'],
            'cof': ['FORID:10'],
            'ie': ['ISO-8859-1'],
            'q': ['query'],
            'sa.x': ['0'],
            'sa.y': ['0'],
            'sa': ['Search'],
            'ad': ['n9'],
            'num': ['10'],
            'rurl': [
                'http://www.blogsearchengine.org/search.html?cx=partner-pub'
                '-9634067433254658%3A5laonibews6&cof=FORID%3A10&ie=ISO-8859-1&'
                'q=query&sa.x=0&sa.y=0&sa=Search'
            ],
            'siteurl': ['http://www.blogsearchengine.org/']
        }

        params = urllib.parse.urlencode(params_dict, doseq=True)
        url_template = urllib.parse.urlunparse(
            ['https', self.allowed_domains[0], '/cse',
             '', params, 'gsc.tab=0&gsc.q=query&gsc.page=page_num'])
        for query in self.queries:
            for page_num in range(1, 11):
                url = url_template.replace('query', urllib.parse.quote(query))
                url = url.replace('page_num', str(page_num))
                yield SplashRequest(url, self.parse, endpoint='render.html',
                                    args={'wait': 0.5})

    def parse(self, response):
        if 'gsc.q=C' in str(response.request):
            print('we found it!')
        urls = response.css('div.gs-title.gsc-table-cell-thumbnail') \
            .xpath('./a/@href').extract()
        gsc_fragment = urllib.parse.urlparse(response.url).fragment
        fragment_dict = urllib.parse.parse_qs(gsc_fragment)
        page_num = int(fragment_dict['gsc.page'][0])
        query = fragment_dict['gsc.q'][0]
        page_size = len(urls)
        for i, url in enumerate(urls):
            parsed_url = urllib.parse.urlparse(url)
            rank = (page_num - 1) * page_size + i
            yield {
                'rank': rank,
                'url': parsed_url.netloc,
                'query': query
            }
