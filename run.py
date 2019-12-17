from credentials import Credentials
from user import User
import random

def create_user (username, password):
    '''function to create a new user '''

    new_acc = User (username, password)

    return new_acc

def users_data(app_title, acc_name, acc_password):
    '''Function to create a new data entry'''

    new_data = Credentials (app_title, acc_name, acc_password)

    return new_data

def authenticate_user(username, password):
        '''Function to authenticate user'''

    return User.user_auth(username, password)

def save_created_user(user):
        '''Function to store user information'''

    user.save_acc()

def save_user_data(credentials):
    '''Function to store user data'''

    credentials.save_data()

def display_data():
        '''Function to display saved data'''

    return Credentials.display_account()

def delete_data(x):
    '''Function to remove stored data'''

    Credentials.delete_data(x)

def find_account(app_title):
        '''Function to locate and display account details'''

    return Credentials.locate_account(app_title)

def pass_generate(length):
    '''Function to create a random password'''

    return Credentials.random_password(length)


   
