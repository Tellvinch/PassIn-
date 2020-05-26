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
        Method that takes in a name and returns a user that matches that name.

        Args:
            username: nanme to search for
        Returns :
            details of person that matches the name.
        '''

        for user in cls.users:
            if user.username == username:
                return user 

    @classmethod
    def user_exist(cls, username):
        '''
        Method that checks if a user exists from the users list.
        Args:
            name:  name to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for user in cls.users:
            if user.username == username:
                return True

        return False

    @classmethod
    def display_users(cls):
        '''
        method that returns the contact list
        '''
        return cls.users

    def login(self):
        """
        This method checks if a user object exists in the users list
        """
        if User in User.users:
            print(User)
            return User

    
    @classmethod
    def copy_username(cls,password):
        user_found = User.find_by_name(password)
        pyperclip.copy(user_found.username)

