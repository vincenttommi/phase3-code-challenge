# class Magazine:
#     def __init__(self, name,category):
#         self._name = name
#         self._category = category


#     def name(self):
#         return self._name
#     def category(self):
#         return self._category
    
# v = Magazine('The Standard')
# print(v.name())

""" `Magazine __init__(name, category)
  - A magazine is initialized with a name as a string and a category as a string
  - The name and category of the magazine **can be** changed after being initialized.
- `Magazine name()`
  - Returns the name of this magazine
- `Magazine category()`
  - Returns the category of this magazine
- `Magazine all()`
  - Returns an list of all Magazine instances
  """
import Article


class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
        self.all_magazines.append(self) # add the current magazine  to all magazines instances
        

    def name(self):
        return self._name  # returns the name of this magazine

    def category(self):
        return self._category   #returns the category of these magazine

    @classmethod
    def all(cls):
        return cls.all_magazines #  return a list  of all magazines instances

    @classmethod
    def find_by_name(cls, name):
        for magazine in cls.all_magazines:
            if magazine.name() == name:
                return magazine  # iterates  overs all magazines intances and returns  the first magazine object
            # that matches the  given name

    @classmethod
    def article_titles(cls):
        return [article.title() for article in Article.all_articles if article.magazine() == cls] 
    
    """
        Returns a list of titles of all articles written for magazines of the current class (Magazine)

    """

    def contributing_authors(self):
        
        authors = [article.author() for article in Article.all_articles if article.magazine() == self]
        # retrieves alist of authors who have written articles for the current magazine instance 
        return [author for author in authors if authors.count(author) > 2]
    """
    Returns a list of authors who have written more than 2 articles for the current magazine instance
    """






        


  
