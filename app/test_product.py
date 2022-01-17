import unittest
from models import product
Product = product.Product

class ProductTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the product class
    '''
    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_product = Product("John Doe", "Pitch title", "This is a sample of a product pitch")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_product, Product))

if __name__ == '__main__':
    unittest.main()