import Article


class Author:
    all_authors = []
#  initializers  it  initializes the values
def __init__(self, name):
        self._name = name
        self.all_authors.append(self)

def name(self):
        return self._name
# This is a list that selects only those articles where the author of the article is equal to current author object self
def articles(self):
        return [article for article in Article.all_articles if article.author() == self]
# it iterates to all articles until it gets the relevant article

"""

Returns a list of unique magazines that the author has contributed to
Returns a list of unique magazines that the author has contributed to

"""


def magazines(self):
        return list(set(article.magazine() for article in self.articles()))
# writer allows you to add a new article
def add_article(self, magazine, title):
        ne_article = Article(self, magazine, title)
        return ne_article

def topic_areas(self):
        return list(set(magazine.category() for magazine in self.magazines())) 

        """
        # Returns a list of unique topic areas/categories of the magazines the author has contributed to
    
        """

    
