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
    Function that creates new credential
    '''
    new_credential = Credential(user_name, site_name, account_name, password)
    return new_credential

def save_credential(credential):
    '''
    Function to save a newly created credential
    '''
    Credential.save_credentials(credential)
    
def display_credentials(user_name):
    '''
    Function that displays credentials saved by a user
    '''
    return Credential.display_credentials(user_name)

def copy_credentials(site_name):
    '''
    Function to copy credentials details to the clipboard
    '''
    return Credential.copy_credential(site_name)

def main():
    print(' ')
    print('Hello! Welcome.')
    while True:
        print(' ')
        print("-"*60)
        print('Use these codes to navigate: \n ca-Create an Account \n li-log In \n ex-Exit')
        short_code = input('Enter a choice: ').lower().strip()
        if short_code == 'ex':
            break
        
        elif short_code == 'ca':
            print("-"*60)
            print(' ')
            print('To create a new account:')
            first_name = input('First Name - ').strip()
            last_name = input('Last Name - ').strip()
            password = input('Enter your password - ').strip()
            save_user(create_user(first_name, last_name, password))
            print(" ")
            print(f'New Account Created for: {first_name} {last_name} using password: {password}')
        
        elif short_code == 'li':
            print("-"*60)
            print(' ')
            print('To log in, Please enter your account details:')
            user_name = input('Enter your first name - ').strip()
            password = str(input('Enter your password - '))
            user_exists = verify_user(user_name, password)
            if user_exists == user_name:
                print(" ")
                print(f'Welcome {user_name}! Kindly choose an option to proceed.')
                print(' ')
                while True:
                    print("-"*60)
                    print('Navigation codes: \n cc-Create a credential \n dc-Display Credentials \n copy-Copy password \n ex-Exit')
                    short_code = input('Enter a choice: ').lower().strip()
                    print("-"*60)
                    if short_code == 'ex':
                        print(" ")
                        print(f'Au Revoir {user_name}')
                        break
                    elif short_code == 'cc':
                        print(' ')
                        print('Please enter your credentials:')
                        site_name = input('Your Site\'s Name - ').strip()
                        account_name = input('Your Account\'s Name - ').strip()
                        while True:
                            print(' ')
                            print("-"*60)
                            print('Choose an option for entering your password: \n ep-enter existing password \n gp-generate a password \n ex-exit')
                            psw_choice = input('Enter an option: ').lower().strip()
                            print("-"*60)
                            if psw_choice == 'ep':
                                print(" ")
                                password = input('Passcode entry: ').strip()
                                break
                            elif psw_choice == 'gp':
                                password = generate_password()
                                break
                            elif psw_choice == 'ex':
                                break
                            else:
                                print('Sorry wrong passcode entered. Try again!')
                        save_credential(create_credential(user_name, site_name, account_name, password))
                        print(' ')
                        print(f'Credential created: Site Name: {site_name} - Account Name: {account_name} - Password: {password}')
                        print(' ')
                    elif short_code == 'dc':
                        print(' ')
                        if display_credentials(user_name):
                            print('Here is a list of all your credentials')
                            print(' ')
                            for credential in display_credentials(user_name):
                                print(f'Site Name: {credential.site_name} - Account Name: {credential.account_name} - Password: {password}')
                                print(' ')
                            else:
                                print(' ')
                                print("No credentials saved yet")
                                print(' ')
                    elif short_code == 'copy':
                        print(' ')
                        chosen_site = input('Please the site name for the credential password to copy: ')
                        copy_credentials(chosen_site)
                        print(' ')
                    else:
                        print('Wrong entry option. Try again!')
                    
                else:
                    print(' ')
                    print('Oops! Wrong details entered. Try again or create a new account.')
                        
            else:
                print("-"*60)
                print(' ')
                print('Wrong option entered. Try again!')
                
                
if __name__ == '__main__':
    main()