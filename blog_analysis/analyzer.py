import argparse
import csv
import glob
import json
import os
from operator import itemgetter

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from scraping.spiders.blogs import BlogsSpider
from scraping.spiders.traffic import TrafficSpider

settings = get_project_settings()


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
    return list(languages)[:n]


def get_top_blogs():
    """
    Get URLs of most popular blog posts for most popular programming languages
    on GitHub.
    """
    languages = get_top_languages(30, settings['LANGUAGES_DATA'])
    process = CrawlerProcess(settings)
    process.crawl(BlogsSpider, languages)
    process.start()  # the script will block here until the crawling is done


def get_latest_file(directory):
    list_of_files = glob.glob(os.path.join(directory, '*'))
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file


def estimate_traffic():
    """
    Analyze traffic of the scraped blogs.
    """
    process = CrawlerProcess(settings)
    blogs_file = get_latest_file(settings['BLOGS_FEED_DIR'])
    with open(blogs_file) as f:
        blogs = json.load(f)
    process.crawl(TrafficSpider, blogs)
    process.start()  # the script will block here until the crawling is done


if __name__ == '__main__':
    desc = 'Analyze and compare programming blogs traffic.'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('spider', choices=['blogs', 'traffic'],
                        help='Scrapy spider name to run.')

    args = parser.parse_args()
    if args.spider == 'blogs':
        get_top_blogs()
    elif args.spider == 'traffic':
        estimate_traffic()
