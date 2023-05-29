"""
- `Article __init__(author, magazine, title)`
  - An article is initialized with an author as an Author object, a magazine as a Magazine object, and title as a string.
  - An article **cannot** change its author, magazine, or title after it is has been initialized.
- `Article title()`
  - Returns the title for that given article
- `Article all()`
  - Returns an list of all Article instances

  readers - it allows you to add  new  article to the others list
  initialisers - also known as constructors  are special methods
  that are used to  initialise state of an object

  writers - also  know as setters or mutators  are that allow you
  to modify  the values  of the instance varibales of an object

  initializers - 

"""

class Article:
    all_articles = []  # Class variable to store all Article instances
    def __init__(self, author, magazine, title):
        self._author = author  # Assign the provided author to the instance variable _author
        self._magazine = magazine  # Assign the provided magazine to the instance variable _magazine
        self._title = title  # Assign the provided title to the instance variable _title
        self.all_articles.append(self)
        # Add the current article instance to the list of all Article instances
    def title(self):
        return self._title
        # Returns the title of the article
    def author(self):
        return self._author
        # Returns the author of the article
    def magazine(self):
        return self._magazine
    #Return the magazine of the article