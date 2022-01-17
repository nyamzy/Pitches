import unittest
from app.models import User

class UserTest(unittest.TestCase):
    '''
    Test case to test behaviour of the User class
    '''
    def setUp(self):
        self.new_user = User()