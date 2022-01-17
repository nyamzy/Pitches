import unittest
from models import vows
Vows = vows.Vows

class VowsTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the vows class
    '''
    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_vow = Vows("John Doe", "Vow title", "This is a sample of a vow")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_vow, Vows))

if __name__ == '__main__':
    unittest.main()