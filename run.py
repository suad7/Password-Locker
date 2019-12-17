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

   
