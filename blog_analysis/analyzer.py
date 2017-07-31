import csv
import os
from operator import itemgetter

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from scraping.spiders.blogs import BlogsSpider


def get_top_languages(n, file_name):
    """
    Get most popular programming languages based on GitHub repo statistics.

    *Data is taken from githut.info
    :return: list of top `n` languages
    """
    f_name = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                          f'data/{file_name}')
    with open(f_name) as languages_file:
        reader = csv.reader(languages_file)
        languages_data = list(reader)[1:]
    push_events = filter(lambda entry: entry[1] == 'PushEvent',
                         languages_data)
    sorted_results = sorted(push_events, key=lambda x: int(x[2]),
                            reverse=True)
    languages = map(itemgetter(0), sorted_results)
    return list(languages)


def get_top_blogs():
    """
    Analyze connection between post frequency and visitors
    :return:
    """
    settings = get_project_settings()
    languages = get_top_languages(30, settings['LANGUAGES_DATA'])
    process = CrawlerProcess(settings)
    process.crawl(BlogsSpider, languages)
    process.start()  # the script will block here until the crawling is done


if __name__ == '__main__':
    get_top_blogs()
