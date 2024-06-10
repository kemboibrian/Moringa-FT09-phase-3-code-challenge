

class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self._id = id
        self._title = title
        self._content = content
        self._author_id = author_id
        self._magazine_id = magazine_id

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def content(self):
        return self._content

    @property
    def author_id(self):
        return self._author_id

    @property
    def magazine_id(self):
        return self._magazine_id

    @staticmethod
    def create_article(author, magazine, title, content):
        query = """
            INSERT INTO articles (title, content, author_id, magazine_id)
            VALUES (?, ?, ?, ?)
        """
        with connection.cursor() as cursor:
            cursor.execute(query, (title, content, author.id, magazine.id))
            connection.commit()
            article_id = cursor.lastrowid
        return Article(article_id, title, content, author.id, magazine.id)

    def __repr__(self):
        return f'<Article {self.title}>'

    @property
    def author(self):
        from models.author import Author
        # Assuming the relationship between Article and Author is defined in the database
        query = """
            SELECT a.*
            FROM authors a
            JOIN articles art ON a.id = art.author_id
            WHERE art.id = ?
        """
        with connection.cursor() as cursor:
            cursor.execute(query, (self.id,))
            author_data = cursor.fetchone()
            author = Author(*author_data)
        return author
