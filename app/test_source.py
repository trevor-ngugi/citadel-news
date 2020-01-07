import unittest
from models import source
Source=source.Source

class TestSource(unittest.TestCase):
    """
    test class to check the behaviour of the source class
    """
    def setUp(self):
        """
        set up method that will run before each test
        """
        self.new_source=Source('abc','abc')

    def test_instance(self):
        """
        to check if instance if article class
        """
        self.assertTrue(isinstance(self.new_source,Source))

if __name__ == "__main__":
    unittest.main()