from user import User
from credentials import Credentials
import random


def create_user(username, password):
    '''
    Function to create a new user
    '''
    new_user = User(username, password)
    return new_user


def create_account(account_name, account_password):
    '''
    Function to create a new account
    '''
    new_account = Credentials(account_name, account_password)
    return new_account


def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()


def save_accounts(credentials):
    '''
    Function to save account
    '''
    credentials.save_accounts()


def login(user):
    username = input("Enter username: ")
    password = input("Enter password: ")
    User1 = User(username, password)

    if User1 is not None:
        user.login
        print(f"Welcome {username}! You're now Logged In")
    else:
        print("Invalid Username or Password.")


def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_contact()


def del_credentials(credentials):
    '''
    Function to delete an account
    '''
    credentials.delete_credentials()


def find_user(username):
    '''
    Function that finds a contact by number and returns the contact
    '''
    return User.find_by_name(username)


def find_account(account_name):
    '''
    Function that finds an account by name and returns the account_name
    '''
    return Credentials.find_by_name(account_name)


def check_existing_users(username):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return User.user_exist(username)


def check_existing_accounts(account_name):
    '''
    Function that check if an account exists with that number and return a Boolean
    '''
    return Credentials.account_exist(account_name)


def display_users(user):
    '''
    Function that returns all the saved contacts
    '''
    return User.display_users()


def display_accounts():
    '''
    Function that returns all the saved accounts
    '''
    return Credentials.display_accounts()


def main():
    print("Hello Welcome to PassIn. What is your name?")
    username = input()
    print(f"Hello {username}. what would you like to do?")
    print('\n')

    while True:
        print("Reply with")
        print("1.Create new account")
        print("2.Login")
        print("3.Search account")
        print("4.Exit passin")

        answer = input()

        if answer == '1':
            print("New user")
            print("*"*10)

            print("Username:")
            username = input()

            print("Password:")
            passw = input()
            num = random.randint(0, 1000)
            password = (f"{passw}{num}")

            # create and save new user.
            save_user(create_user(username, password))
            User.save_user
            print('\n')
            print(
                f"Good job {username} your account was successfully created,we added some numbers to you password to make more unique its now {password}")
            print('\n')

        elif answer == '2':
            login(User)
            print("Reply with:")
            print("1.Display my saved passwords")
            print("2.Add a new account and password")
            option = input()
            if option == '1':  
                if display_accounts():
                    print("Here is a alist of all the accounts")
                    print("\n")

                for credentials in display_accounts():
                    print(f"Hey {credentials.account_name} your {credentials.account_password} password is safely stored!", "yellow")
                    print("\n")

            else:
                print("New account password")
                print("*"*10)

                print("Password for:")
                account_name = input()

                print("Now enter the Password:")
                account_password = input()
                
                # create and save new user.
                save_accounts(create_account(account_name, account_password))
                Credentials.save_accounts
                print('\n')
                print(
                f"Good job {username} your password was successfully created and saved")
                print('\n')
                


        elif answer == '3':

            print("Enter the account you want to search for")
            search_account_name = input()
            if check_existing_users(search_account_name):
                search_credentials = find_account(search_account_name)
                print(
                    f"{search_account_name.account_name} {search_account_name.account_name}")
                print('-' * 20)
                print(f"Username.......{search_credentials.account_name}")
                print(
                    f"Your password......{search_credentials.account_password}")
            else:
                print("That user does not exist")

        elif answer == '4':
            print("Bye .......")
            break
        else:
            print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':

    main()
