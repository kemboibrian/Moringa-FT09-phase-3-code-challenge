
from models.article import Article

class Author:
    def __init__(self, id, name):
        self._id = id
        self._name = name

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @staticmethod
    def create_author(name):
        query = "INSERT INTO authors (name) VALUES (?)"
        with connection.cursor() as cursor:
            cursor.execute(query, (name,))
            connection.commit()
            author_id = cursor.lastrowid
        return Author(author_id, name)

    def articles(self):
        query = """
            SELECT id, title, content
            FROM articles
            WHERE author_id = ?
        """
        with connection.cursor() as cursor:
            cursor.execute(query, (self.id,))
            articles_data = cursor.fetchall()
        
        articles = []
        for article_data in articles_data:
            article = Article(*article_data)
            articles.append(article)
        
        return articles

    def magazines(self):
        query = """
            SELECT magazines.id, magazines.name, magazines.category
            FROM magazines
            JOIN articles ON articles.magazine_id = magazines.id
            WHERE articles.author_id = ?
        """
        with connection.cursor() as cursor:
            cursor.execute(query, (self.id,))
            magazines_data = cursor.fetchall()
        
        magazines = []
        for magazine_data in magazines_data:
            magazine = Magazine(*magazine_data)
            magazines.append(magazine)
        
        return magazines

    def __repr__(self):
        return f'<Author {self.name}>'
