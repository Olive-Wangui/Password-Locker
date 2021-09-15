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
        Test to see if the initialization of the user instances is well done
        '''
        self.assertEqual(self.new_user.first_name, 'Olive')
        self.assertEqual(self.new_user.last_name, 'Wangui')
        self.assertEqual(self.new_user.password, 'lil2000')
        
    def test_save_user(self):
        '''
        Test to check if the new users information is saved into the users list
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
        Function to test whether the login function check_user works as expected
        '''
        self.new_user = User('Olive', 'Wangui', 'lil2000')
        self.new_user.save_user()
        user2 = User('Ian', 'Wangui', 'lil2000')
        user2.save_user()
        
        for user in User.users_list:
            if user.last_name == user2.last_name and user.password == user2.password:
                current_user = user.last_name
                return current_user
            
            self.assertEqual(user.first_name, Credential.check_user(user2.password, user2.first_name))
            
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
        
    def test_save_credentials(self):
        '''
        Test to check if the new credential info is saved into the credentials
        '''
        self.new_credential.save_credentials()
        twitter = Credential('Jane', 'Twtitter', 'maryjoe', 'lil2000')
        twitter.save_credentials()
        self.assertEqual(len(Credential.credentials_list),2)
        
    # def test_generate_password(self):
	# 	'''
	# 	Test to check if the generate password generates 8 character long alphanumeric numbers
	# 	'''
	# 	self.twitter = Credential('Twitter','maryjoe','')
	# 	self.twitter.password = generate_password()
	# 	self.assertEqual()
    
    def tearDown(self):
        '''
        Function to clear the credentials list after every test
        '''
        Credential.credentials_list = []
        User.users_list = []
        
    def test_display_credentials(self):
        '''
        Test to check if the find_by_site_name method returns the correct credential
        '''
        self.new_credential.save_credentials()
        twitter = Credential('Jane', 'Twitter', 'maryjoe', 'lil2000')
        twitter.save_credentials()
        credential_exists = Credential.find_by_site_name('Twitter')
        self.assertEqual(credential_exists, twitter)
        
    def test_find_by_site_name(self):
        '''
        Test to check if the find_by_site_name method returns the correct credential
        '''
        self.new_credential.save_credentials()
        twitter = Credential('Jane', 'Twitter', 'maryjoe', 'lil2000')
        twitter.save_credentials()
        credential_exists = Credential.find_by_site_name('Twitter')
        self.assertEqual(credential_exists, twitter)
        
    def test_copy_credential(self):
        '''
        Test to check if the copy credential method copies the correct credential
        '''
        self.new_credential.save_credentials()
        twitter = Credential('Jane', 'Twitter', 'maryjoe', 'lil2000')
        twitter.save_credentials()
        find_credential = None
        for credential in Credential.user_credentials_list:
            find_credential = Credential.find_by_site_name(credential.site_name)
            return pyperclip.copy(find_credential.password)
        Credential.copy_credentials(self.new_credential.site_name)
        self.assertEqual('lil2000', pyperclip.paste())
        print(pyperclip.paste())
        
if __name__ == '__main__':
    unittest.main(verbosity=2)      
    
