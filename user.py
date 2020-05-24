class User:
    """
    Class that generates new instances of contacts.
    """

    users = []
 # Init method up here

    def save_user(self):
        '''
        save_contact method saves contact objects into contact_list
        '''

        User.users.append(self)

    def __init__(self, username, password):

      # docstring removed for simplicity

        self.username = username
        self.password = password

    def delete_user(self):
        '''
        delete_user method deletes a saved user from the users
        '''

        User.users.remove(self)

    @classmethod
    def find_by_name(cls, username):
        '''
        Method that takes in a number and returns a contact that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''

        for user in cls.users:
            if user.username == username:
                return user


# class user:
#     """
#         Class that generates new instances of users
#         """

#     def cook():


#         print("Welcome to PassIn.What do you want to do?")
#         print("1.Create an account")
#         print("2.Sign into an existing account ")
#         choice =int(input(">"))
#         if choice == 1 :
#             new_username=input("Enter an name you would like to use: ")
#             new_password=input("Enter a password to use to login: ")
#             print(f'All done! {new_username}.You can now save your passwords in PassIn-')

#         else:
#             username=input("Enter your username:")
#             password=input("Enter a password:")
#             print(f'Your username is {username} and password  {password}')

#         print("*****************************************************************************")

#     cook()
