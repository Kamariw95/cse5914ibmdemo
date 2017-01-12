import json
from watson_developer_cloud import AlchemyDataNewsV1
from alchemy_settings.hidden import API_KEY


class AlchemyService():
    alchemy_data_news = AlchemyDataNewsV1(api_key=API_KEY)

    def __init__(self):
        pass
    '''
    getResults(self, search): Takes in the search text and is supposed to return an object.
        This object would have 2 objects inside:
            positive_articles
            negative_articles

        do return filterResults(results)
    '''
    def getResults(self, search):
        results = alchemy_data_news.get_news_documents(start='now-7d', end='now',
                                                       time_slice='12h')

        results = alchemy_data_news.get_news_documents(
            start='1453334400',
            end='1454022000',
            return_fields=['enriched.url.title',
                           'enriched.url.url',
                           'enriched.url.author',
                           'enriched.url.publicationDate'],
            query_fields={
                'q.enriched.url.enrichedTitle.entities.entity':
                    '|text=' + search + ',type=company|'})

        print(json.dumps(results, indent=2))

    '''
    filterResults(self, results, type_flag): This would take in the results and return back the result object that
    you want to return in the getResults function. So it would do the work to sort them into positive_articles and
    negative_articles on a new results object.

    so you should return result, where result.positive_articles and result.negative_articles should be on the object.
    '''
    def filterResults(self, results):
        pass
