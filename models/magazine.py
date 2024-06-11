from database import connection

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

    def __repr__(self):
        return f'<Magazine {self.name}>'

# Move the Article and Author imports to the end
from models.article import Article
from models.author import Author
