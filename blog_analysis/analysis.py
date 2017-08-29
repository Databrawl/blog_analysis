from itertools import groupby
from operator import itemgetter


def get_languages_popularity(data):
    """
    Count total daily views for all languages and sort in descending order.
    """
    query_sorted_data = sorted(data, key=itemgetter('query'))
    for k, group in groupby(query_sorted_data, key=itemgetter('query')):
        group = list(group)
        daily_page_views = map(lambda r: int(r['daily_page_views']), group)
        total_page_views = sum(daily_page_views)
        yield (group[0]['query'], total_page_views)
