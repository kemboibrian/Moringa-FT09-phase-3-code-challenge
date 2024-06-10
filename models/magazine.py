
from models.article import Article
from models.author import Author

class Magazine:
    def __init__(self, id, name, category):
        self._id = id
        self._name = name
        self._category = category

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if 2 <= len(value) <= 16:
            self._name = value
        else:
            raise ValueError("Name must be between 2 and 16 characters.")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            raise ValueError("Category must be a non-empty string.")

    @staticmethod
    def create_magazine(name, category):
        query = "INSERT INTO magazines (name, category) VALUES (?, ?)"
        with connection.cursor() as cursor:
            cursor.execute(query, (name, category))
            connection.commit()
            magazine_id = cursor.lastrowid
        return Magazine(magazine_id, name, category)

    def articles(self):
        query = """
            SELECT id, title, content
            FROM articles
            WHERE magazine_id = ?
        """
        with connection.cursor() as cursor:
            cursor.execute(query, (self.id,))
            articles_data = cursor.fetchall()
        
        articles = []
        for article_data in articles_data:
            article = Article(*article_data)
            articles.append(article)
        
        return articles

    def contributors(self):
        query = """
            SELECT DISTINCT authors.id, authors.name
            FROM authors
            JOIN articles ON articles.author_id = authors.id
            WHERE articles.magazine_id = ?
        """
        with connection.cursor() as cursor:
            cursor.execute(query, (self.id,))
            contributors_data = cursor.fetchall()
        
        contributors = []
        for contributor_data in contributors_data:
            contributor = Author(*contributor_data)
            contributors.append(contributor)
        
        return contributors

    def article_titles(self):
        query = "SELECT title FROM articles WHERE magazine_id = ?"
        with connection.cursor() as cursor:
            cursor.execute(query, (self.id,))
            titles_data = cursor.fetchall()
        
        titles = [title[0] for title in titles_data]
        return titles

    def contributing_authors(self):
        query = """
            SELECT authors.id, authors.name
            FROM authors
            JOIN (
                SELECT author_id
                FROM articles
                WHERE magazine_id = ?
                GROUP BY author_id
                HAVING COUNT(*) > 2
            ) AS top_authors ON authors.id = top_authors.author_id
        """
        with connection.cursor() as cursor:
            cursor.execute(query, (self.id,))
            contributing_authors_data = cursor.fetchall()
        
        contributing_authors = []
        for author_data in contributing_authors_data:
            author = Author(*author_data)
            contributing_authors.append(author)
        
        return contributing_authors

    def __repr__(self):
        return f'<Magazine {self.name}>'
