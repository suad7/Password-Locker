import unittest 
from user import User
from credentials import Credentials

class TestUser(unittest.TestCase):
    '''defines test cases for user methods'''

    def setUp(self):
        '''set up a method to run before each case '''
        self.new_user = User("Suad7")
        self.generate = Credentials ("twitter", "lordSpiral", "sitUp!")
        def test_init(self):
            '''Testing to see if the object is properly initialized'''




