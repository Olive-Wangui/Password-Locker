import unittest
import pyperclip
from user_credentials import User, Credential

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours
    
    Args:
    unittest.TestCase: helps in creating test cases
    '''
    
    def setUp(self):
        '''
        Function to create a user account before each test
        '''
        self.new_user = User('Olive', 'Wangui', 'lil2000')
        
    def test__init__(self):
        '''
        Test to see if the initialization of the user instance is well done
        '''
        self.assertEqual(self.new_user.first_name, 'Olive')
        self.assertEqual(self.new_user.last_name, 'Wangui')
        self.assertEqual(self.new_user.password, 'lil2000')
        
    def test_save_user(self):
        '''
        Test to check if the new users information is saved as required
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.users_list),1)
