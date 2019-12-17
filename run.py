class User:
    ''' class that generates a new instance of users '''

    account_list = []


    def __init__(self, username, password):

        '''define object properties '''

        self.username = username
        self.password = password