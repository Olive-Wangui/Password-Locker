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
        
class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours
    
    Args:
    unittest.TestCase: helps in creating test cases
    '''
    def test_check_user(self):
        '''
        Function to test whether the log in function check_user works as expected
        '''
        self.new_user = User('Olive', 'Wangui', 'lil2000')
        self.new_user.save_user()
        user2 = User('Ian', 'Gitonga', 'lil2000')
        user2.save_user()
        
        for user in User.users_list:
            if user.first_name == user2.first_name and user.password == user2.password:
                current_user = user.first_name
                return current_user
            
            self.assertEqual(current_user, Credential.check_user(user2.password, user2.first_name))
            
    def setUp(self):
        '''
        Function to create an account's credentials before each test
        '''
        self.new_credential = Credential('Olive', 'Instagram', 'olly', 'lil2000')
        
    def test__init__(self):
        '''
        Test to see if the initialization of the credential instances well put
        '''
        self.assertEqual(self.new_credential.user_name, 'Olive')
        self.assertEqual(self.new_credential.site_name, 'Instagram')
        self.assertEqual(self.new_credential.account_name, 'olly')
        self.assertEqual(self.new_credential.password, 'lil2000')      
    
