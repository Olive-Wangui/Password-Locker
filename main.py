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

def generate_password():
    '''
    Function to generate a password automatically
    '''
    gen_pass = Credential.generate_password()
    return gen_pass

def create_credential(user_name, site_name, account_name, password):
    '''
    Function that creates new credentials
    '''
    new_credential = Credential(user_name, site_name, account_name, password)
    return new_credential

def save_credential(credential):
    '''
    Function to save a newly created credential
    '''
    Credential.save_credentials(credential)

