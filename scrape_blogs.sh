#!/usr/bin/env bash

export WORKON_HOME=~/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
workon blog_analysis
export SCRAPY_SETTINGS_MODULE=scraping.settings

#Start Splash server container
docker run -d -p 5023:5023 -p 8050:8050 -p 8051:8051 scrapinghub/splash

python blog_analysis/run.py blogs
python blog_analysis/run.py traffic

#Stop the container
docker rm $(docker stop $(docker ps -a -q --filter ancestor=scrapinghub/splash --format="{{.ID}}"))
