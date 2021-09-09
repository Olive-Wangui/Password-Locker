import pyperclip
import random
import string

# General Variables
global users_list
class User:
    '''
    Class to create user accounts and save information
    '''
    # Class Variables
    # Global users_list
    users_list = []
    def __init__(self, first_name, last_name, password):
        '''
        Method to define the properties for each user object will hold
        '''
        
        # Instance Variables
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        
        def save_user(self):
            '''
            Function to save a newly created user instance
            '''
            User.users_list.append(self)
            
class Credential:
    '''
    Class to create account credentials, generate passwords and save the information acquired
    '''
    # Class Variables
    credentials_list = []
    user_credentials_list = []
    @classmethod
    def check_user(cls, first_name, password):
        '''
        Method that checks if the name and passwsord entered match the entries in the users_list
        '''
        current_user = ''
        for user in User.users_list:
            if (user.first_name == first_name and user.password == password):
                current_user = user.first_name
                return current_user 
            
    def __init__(self, user_name, site_name, account_name, password):
        '''
        Method to define the propertoes for each user object will hold
        '''
        # Instance Variables
        self.user_name = user_name
        self.site_name = site_name
        self.account_name = account_name
        self.password = password
        
    def save_credentials(self):
        '''
        Function to save a newly created user instance
        '''
        # Gloabal users_list
        Credential.credentials_list.append(self)
    