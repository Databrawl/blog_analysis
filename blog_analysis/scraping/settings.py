# -*- coding: utf-8 -*-

# Scrapy settings for scraping project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.dirname(BASE_DIR)

BOT_NAME = 'blog_analysis'

SPIDER_MODULES = ['scraping.spiders']
NEWSPIDER_MODULE = 'scraping.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware':
        810,
}

FEED_DIR = os.path.join(ROOT_DIR, 'feeds')
FEED_URI = f'file:///{FEED_DIR}/%(name)s/%(time)s.json'
BLOGS_FEED_DIR = os.path.join(FEED_DIR, 'blogs')
TRAFFIC_FEED_DIR = os.path.join(FEED_DIR, 'traffic')
FEED_FORMAT = 'json'

# Splash settings
SPLASH_URL = 'http://127.0.0.1:8050'

DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
DUPEFILTER_DEBUG = True

# Other settings
LANGUAGES_DATA = 'q4-2014.csv'
TOP_LANGUAGES_FILE = 'top_languages.csv'
ANALYSIS_DATA_DIR = os.path.join(ROOT_DIR, 'data')
