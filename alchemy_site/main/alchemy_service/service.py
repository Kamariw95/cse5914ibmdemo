import json
from watson_developer_cloud import AlchemyDataNewsV1
from alchemy_settings.hidden import API_KEY
from main.dto.alchemy_item import AlchemyItem
from main.dto.alchemy_result import AlchemyResult
from .false_data import alchemy_data


class AlchemyService():

    def __init__(self):
        self.alchemy_data_news = AlchemyDataNewsV1(api_key=API_KEY)
        self.positive_articles = []
        self.negative_articles = []
    '''
    getResults(self, search): Takes in the search text and is supposed to return an object.
        This object would have 2 objects inside:
            positive_articles
            negative_articles

        do return filterResults(results)
    '''
    def getResults(self, search):

        """
        alchemy_data = self.alchemy_data_news.get_news_documents(
            start='now-7d',
            end='now',
            return_fields=['enriched.url.title',
                           'enriched.url.url',
                           'enriched.url.author',
                           'enriched.url.publicationDate',
                           'enriched.url.enrichedTitle.docSentiment'],
            query_fields={
                'q.enriched.url.enrichedTitle.entities.entity':
                    '|text=' + search + '|'})
        """
        docs_obj = alchemy_data['result']['docs']

        for doc in docs_obj:
            print(json.dumps(doc, indent=2))
            if(doc['source']['enriched']['url']['enrichedTitle']['docSentiment']['type'] == "negative"):
                title = doc['source']['enriched']['url']['title']
                url = doc['source']['enriched']['url']['url']
                author = doc['source']['enriched']['url']['author']

                item = AlchemyItem(title, url, author)
                self.negative_articles.append(item)
            elif(doc['source']['enriched']['url']['enrichedTitle']['docSentiment']['type'] == "positive"):
                title = doc['source']['enriched']['url']['title']
                url = doc['source']['enriched']['url']['url']
                author = doc['source']['enriched']['url']['author']

                item = AlchemyItem(title, url, author)
                self.positive_articles.append(item)
            else: #This is where the neutral articles come.
                pass

        result = AlchemyResult(self.positive_articles, self.negative_articles)
        return result

    '''
    filterResults(self, results, type_flag): This would take in the results and return back the result object that
    you want to return in the getResults function. So it would do the work to sort them into positive_articles and
    negative_articles on a new results object.

    so you should return result, where result.positive_articles and result.negative_articles should be on the object.
    '''
    def filterResults(self, results):
        pass
