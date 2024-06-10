import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine

class TestModels(unittest.TestCase):
    def test_author_creation(self):
        author = Author(1, "John Doe")
        self.assertEqual(author.name, "John Doe")

    def test_article_creation(self):
        author = Author(1, "John Doe")  # Create an Author instance
        magazine = Magazine(1, "Tech Weekly", "Technology")  # Create a Magazine instance
        article = Article(1, "Test Title", "Test Content", author.id, magazine.id)  # Pass Author and Magazine instances
        self.assertEqual(article.title, "Test Title")

    def test_magazine_creation(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        self.assertEqual(magazine.name, "Tech Weekly")

if __name__ == "__main__":
    unittest.main()
