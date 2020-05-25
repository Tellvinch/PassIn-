class Credentials:
    """
    Class that generates new instances of contacts.
    """

    accounts = [one]
 # Init method up here

    def save_accounts(self):
        '''
        save_contact method saves contact objects into contact_list
        '''

        Credentials.accounts.append(self)

    def __init__(self, account_name, account_password):

      # docstring removed for simplicity

        self.account_name = account_name
        self.account_password = account_password

    def delete_accounts(self):
        '''
        delete_account method deletes a saved account from the accounts
        '''

        Credentials.accounts.remove(self)

    @classmethod
    def find_by_name(cls, account_name):
        '''
        Method that takes in a number and returns a contact that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''

        for credentials in cls.accounts:
            if credentials.account_name == account_name:
                return credentials

    @classmethod
    def account_exist(cls, number):
        '''
        Method that checks if a contact exists from the contact list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for Credentials in cls.accounts:
            if Credentials.account_password == number:
                return True

        return False

    @classmethod
    def display_accounts(cls):
        '''
        method that returns the contact list
        '''
        return cls.accounts


# from user import user


# class Credentials:
#     """
#         Class that generates new instances of credentials
#         """

#     def password():
#         name = input("Save password for?? Answer with facebook,instagram etc:")
#         print(f'Cool you want to save your {name} passsword')
#         crepass = input(f'Enter your {name} password:')
#         print(
#             f'Are you sure you want to save {crepass} as your {name} password?')
#         print("1.Yes,save password.")
#         print("2.No,delete")
#         option = int(input())
#         if option == 1:
#                 print(f'All done! .Your password is safe now')
#                 # {user.new_username}
#         else:
#                 print("Moved to trash!")
#         print("Do you want to see what you have saved?")
#         print("1.Yes please")
#         print("2.Not now")
#         view = int(input())
#         if view == 1:
#                 print("Name       -     Password")
#                 print(f'{name}    -     {crepass}')
#                 # {user.new_username}
#         else:
#                 print("Moved to trash!")

#     password()
