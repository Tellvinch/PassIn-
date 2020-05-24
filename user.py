import pyperclip


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

    @classmethod
    def user_exist(cls, number):
        '''
        Method that checks if a contact exists from the contact list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for user in cls.users:
            if user.password == number:
                return True

        return False

    @classmethod
    def display_users(cls):
        '''
        method that returns the contact list
        '''
        return cls.users

    @classmethod
    def copy_username(cls, username):
        user_found = User.find_by_name(username)
        pyperclip.copy(user_found.username)
