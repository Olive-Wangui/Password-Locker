import pyperclip
from user_credentials import User, Credential

def create_user(fname, lname, password):
    '''
    Function to create a new user account
    '''
    new_user = User(fname, lname, password)
    return new_user

def save_user(user):
    '''
    Function to save a new user account
    '''
    User.save_user(user)
    
    def verify_user(first_name, password):
        '''
        Function that verifies the existence of the user before creating credentials
        '''
        checking_user = Credential.check_user(first_name, password)
        return checking_user