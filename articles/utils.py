from nltk.corpus import wordnet as wn

from keyword_handler import KeywordHandler
from models import Article, Relationship


class ArticleHandler(object):

    @staticmethod
    def calculate_relationship(word_list1, word_list2):
        score = 0
        for w1 in word_list1:
            w1_list = wn.synsets(w1)
            for w2 in word_list2:
                w2_list = wn.synsets(w2)
                for s1 in w1_list:
                    for s2 in w2_list:
                        try:
                            score += s1.lch_similarity(s2)
                        except:
                            pass
        return score

    def __init__(self):
        self.kw_handler = KeywordHandler()

    def add_new_article(self, url):
        kws = self.kw_handler.get_kw_for_url(url)
        kws = ",".join(kws)
        article = Article(link=url, keywords=kws)
        article.save()
        return article

    def compute_relationship(self, article):
        for a in Article.objects.all():
            score = self.calculate_relationship(article.keywords, a.keywords)
            r = Relationship(id1=article.id, id2=a.id, score=score)
            r.save()
