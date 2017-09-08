from itertools import groupby
from operator import itemgetter

from utils import outlier_threshold


def get_languages_popularity(data):
    """
    Count total daily views for all languages and sort in descending order.

    :param data: scraped data
    """
    query_sorted_data = sorted(data, key=itemgetter('query'))
    result = {'languages': [], 'views': []}
    popularity = []
    for k, group in groupby(query_sorted_data, key=itemgetter('query')):
        group = list(group)
        daily_page_views = map(lambda r: int(r['daily_page_views']), group)
        total_page_views = sum(daily_page_views)
        popularity.append((group[0]['query'], total_page_views))
    sorted_popularity = sorted(popularity, key=itemgetter(1), reverse=True)
    languages, views = zip(*sorted_popularity)
    result['languages'] = languages
    result['views'] = views
    return result


def get_ranking_and_views(data, languages):
    """
    Extract ranking and views information and structure it by languages.

    :param data: scraped data
    :param languages: languages to get data about
    :return: dict of language:data key/value pairs
    """
    filtered_data = filter(lambda elem: elem['query'] in languages, data)
    query_sorted_data = sorted(filtered_data, key=itemgetter('query'))
    result = {}
    for k, group in groupby(query_sorted_data, key=itemgetter('query')):
        group = list(group)
        ranks_views_data = [(r['rank'] + 1, int(r['daily_page_views']))
                            for r in group]
        ranks, views = zip(*ranks_views_data)
        result[group[0]['query']] = ranks, views
    return result


def filter_view_deviations(data):
    """
    Delete rank/views pairs with amount of views significantly deviating from
    the mean value of views.

    :param data: dict of language:data key/value pairs
    :return: dict of language:data key/value pairs without certain rank,view
        points
    """
    result = {}
    for lang, ranks_views in data.items():
        threshold = outlier_threshold(ranks_views[1])
        rank_view_pairs = zip(*ranks_views)
        filtered_rank_view_pairs = filter(lambda p: p[1] <= threshold,
                                          rank_view_pairs)
        ranks, views = zip(*filtered_rank_view_pairs)
        result[lang] = ranks, views
    return result
