import unittest
from app.models import Jokes

class JokesTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the jokes class
    '''
    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_joke = Jokes("John Doe", "Joke title", "This is a sample of a joke")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_joke, Jokes))
