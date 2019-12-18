from credentials import Credentials
from user import User
import random


def create_user(username, password):
    '''function to create a new user '''

    new_acc = User(username, password)

    return new_acc


def users_data(app_title, acc_name, acc_password):
        
    '''Function to create a new data entry'''
    new_data = Credentials(app_title, acc_name, acc_password)
    return new_data


def authenticate_user(username, password):

    '''Function to authenticate user'''

    return User.user_auth(username,password)

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


def main():
    
    print("This is password locker!")
    print("To sign up, key 'su', to log in, key 'li' and 'xx' to exit ...")
    log_in = False

    while True:
        answer = input ('>>> ')

        if answer == "li":

            print("Enter your Username: ")
            username = input('>>> ')

            print("Enter your password: ")
            password = input ('>>> ')

            log_in = authenticate_user(username, password) if answer == 'li' else False
            print("Login successful!")
            print('\n')

            while log_in:
                print('\n')
                print("Use the following short codes to navigate \n ad - to save an existing account data \n cd - to create new account data \n vd - to view list of inputed data \n dd - to delete account data from list \n ex - to exit application")
                short_code = input(">>>")

                if short_code == "ad":
                        print ("Enter existing account data...")

                        print ("Enter the name of the account")

                        app_title = input(">>>")

                        print ("Enter the username to the account")
                        acc_name = input (">>>")

                        print ("Enter the account's password")
                        acc_password = input (">>>")

                        save_user_data(users_data(app_title, acc_name, acc_password))

                        print (f"Data for {app_title} has been saved.")

                elif short_code == "cd":
                        print ("Create new account data...")
 
                        print ("Enter the name of the account")
                        app_title = input(">>>")

                        print ("Enter the username to the account")
                        acc_name = input (">>>")

                        print ("For the password; \n key in 'y' if you want a generated password \n 'n' if you want to input a custom one ")
                        answer_password = input(">>>")

                        if answer_password == "y":
                                print("Input password preffered length...")
                                pass_length= int(input(">>>"))
                                acc_password = pass_generate(pass_length)
                                print(f"{app_title}'s password is {acc_password}")

                        elif answer_password == "n":
                                print("Input your own password")
                                acc_password = input (">>>")

                        else:
                                print ("Your choice is in valid, try again")

                                save_user_data(users_data(app_title, acc_name, acc_password))

                                print (f"Data for {app_title} has been saved.")
                                print('\n')


                if short_code == "vd":
                        if display_data():
                                print("Here is a list of all your stored account data")
                                print('\n')

                                for data in display_data():
                                        print (f"Application Title >>> {data.app_title}")
                                        print (f"Application Username >>> {data.acc_name}")
                                        print (f"Application Password >>> {data.acc_password}")
                                        print('\n')

                        else:
                                print("You don't seem to have any stored account data")
                                print('\n')

                if short_code == "dd":
                        print ("Enter the account name of the data you'd like to delete...")
                        delete_answer = input(">>>")
                        found_acc = find_account(delete_answer)
                        if (found_acc):
                                print (f"{delete_answer} you are here ")
                                delete_data(found_acc)
                                print(f"Your {delete_answer}'s data has been successfully deleted")

                elif short_code == "ex":
                        print("Exiting the application...Goodbye!")
                        exit()

                else:
                        print("Invalid code, try again")
                        print("Wrong username and/or password. Try again")
        
        elif answer == "su":
            print("Create a new account to store your data...")

            print("Enter a Username:")
            username = input(">>>")

            print("Enter a password:")
            password = input(">>>")

            save_created_user(create_user(username, password))
            print(f"Welcome {username}, your account has been successfully set up")
            print('\n')
            print("Now to login, use li")

        elif answer == "xx":
            print ("Goodbye!")
            exit()
        else:
            print("Invalid code, try again")

if __name__ == '__main__':
        main()     





