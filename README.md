# Blog analysis

This is the code used in the blog post on www.databrawl.com. This project
contains script for scraping www.google.com for most popular programming blogs,
identifying their traffic by scraping www.statshow.com and launching various
analysis based on that data.

Note: Using Python 3.6

## Quickstart:

This will create a virtual environment and install dependencies. Launch from
the desired directory you wish the project to reside.
<sub>\* *Note: [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) needed.*</sub>

```bash
$ mkvirtualenv blog_analysis -p /usr/bin/python3.6
$ pip install -r requirements.txt
```

Available commands:

1. Scrape top programming blogs, classified by the programming language
    ```bash
    $ python python blog_analysis/run.py blogs
    ```
2. Scrape traffic data for the blogs
    ```bash
    $ python blog_analysis/run.py traffic
    ```
3. Analyze the traffic data and run data visualization routines
    ```bash
    $ python blog_analysis/run.py analyzer
    ```