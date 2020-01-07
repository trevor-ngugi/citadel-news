import unittest
from models import article
Article=article.Article

class TestArticle(unittest.TestCase):
    """
    test class to check behaviour of  the article class
    """
    def setUp(self):
        """
        set up method that will run before each test
        """
        self.new_article=Article("Bob", "Random Title", "Short","random.com","random.jpg","12/12/12", "None")

    def test_instance(self):
        """
        to check if instance if article class
        """
        self.assertTrue(isinstance(self.new_article,Article))

    def test_init(self):
        """
        Tests for proper instantiation
        """
        self.assertEqual(self.new_article.author, "Bob")
        self.assertEqual(self.new_article.title, "Random Title")
        self.assertEqual(self.new_article.description, "Short")
        self.assertEqual(self.new_article.url, "random.com")
        self.assertEqual(self.new_article.urlToImage, "random.jpg")
        self.assertEqual(self.new_article.published_At, "12/12/12")
        self.assertEqual(self.new_article.content, "None")

if __name__ == "__main__":
    unittest.main()

