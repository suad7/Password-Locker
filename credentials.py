import random
import string


class Credentials:
    '''class to instanciate new account credentials'''

    generated = []

    def __init__(self, app_title, acc_name, acc_password):
        '''Method to instanciate object properties'''

        self.app_title = app_title
        self.acc_name = acc_name
        self.acc_password = acc_password

    def save_data(self):
            '''Method that saves our accounts'''

            Credentials.generated.append(self)

    def delete_data(self):
            '''Method to delete an account of our list'''

            Credentials.generated.remove(self)

    def random_password(self):
            '''method to generate a random password'''

            characters = string.ascii_lowercase + string.digits
            gen_password = ''.join(random.choice(characters) for i in range (0,12))

            return gen_password

    @classmethod
    def display_account(cls):
        '''Method to display stored account data'''

        return cls.generated

    @classmethod
    def locate_account(cls, app_title):
        '''Method to search and display the account data'''

        for acc in cls.generated:
            if acc.app_title == app_title:
                return acc

