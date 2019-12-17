import unittest 
from user import User
from credentials import Credentials

class TestUser(unittest.TestCase):
    '''defines test cases for user methods'''

    def setUp(self):
        '''set up a method to run before each case '''

        self.new_user = User("Suad" , "samar99")
        self.generate = Credentials ("twitter", "lordSpiral", "sitUp!")

    def test_init(self):
            '''Testing to see if the object is properly initialized'''

        self.assertEqual(self.new_user.username, "Suad")
        self.assertEqual(self.new_user.password, "samar99")

        self.assertEqual(self.generate.app_title, "twitter")
        self.assertEqual(self.generate.acc_name, "lordSpiral")
        self.assertEqual(self.generate.acc_password, "sitUp!")

    def test_saved_acc(self):
            '''Test case saving username and passwords'''

        self.assertEqual(len(User.account_list), 0)

    def test_user_auth(self):
            '''Test is user login'''

        self.new_user.save_acc()
        test_user = User ("suad", "samar99")
        test_user.save_acc()

        user_exist = User.user_auth("suad", "samar99")

        self.assertTrue(user_exist)





