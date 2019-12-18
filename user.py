class User:
    ''' class that generates a new instance of users '''

    account_list = []


    def __init__(self, username, password):

        '''define object properties '''

        self.username = username
        self.password = password

    def save_acc(self):
        '''Method to push new created account and password to storage'''

        User.account_list.append(self)

    @classmethod
    def user_auth(cls,username, password):
        '''method that checksif user exist by name'''

        for acc in cls.account_list:
            if acc.username == username and acc.password == password:
                return True
        return False