from user import User
from credentials import Credentials


def create_user(username, password):
    '''
    Function to create a new user
    '''
    new_user = User(username, password)
    return new_user


def save_users(contact):
    '''
    Function to save user
    '''
    contact.save_user()


def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_contact()


def find_user(username):
    '''
    Function that finds a contact by number and returns the contact
    '''
    return User.find_by_name(username)


def check_existing_users(username):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return User.user_exist(username)


def display_users():
    '''
    Function that returns all the saved contacts
    '''
    return User.display_users()


def main():
    print("Hello Welcome to PassIn. What is your name?")
    username = input()
    print(f"Hello {username}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : cc - create a new account, in - Login, , ex -exit PassIn ")

        short_code = input().lower()

        if short_code == 'cc':
            print("New user")
            print("*"*10)

            print("username:")
            username = input()

            print("password:")
            password = input()

            # create and save new user.
            save_users(create_user(username, password))
            print('\n')
            print(f"New Contact {username} {password} created")
            print('\n')

        elif short_code == 'dc':

            if display_users():
                print("Here is a list of all your users")
                print('\n')

                for user in display_users():
                    print(
                        f"{user.username} {user.password}")

                print('\n')
            else:
                print('\n')
                print("You dont seem to have any users saved yet")
                print('\n')

        elif short_code == 'fc':

            print("Enter the number you want to search for")

            search_name = input()
            if check_existing_users(search_name):
                search_user = find_user(search_name)
                print(f"{search_name.username} {search_name.last_name}")
                print('-' * 20)

                print(f"Username.......{search_user.username}")
                print(f"Your password......{search_user.password}")
            else:
                print("That user does not exist")

        elif short_code == "ex":
            print("Bye .......")
            break
        else:
            print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':

  main()
