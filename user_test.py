import unittest  # Importing the unittest module
from user import User  # Importing the user class


class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.User1 = User("Tellvinch", "444")  # create user object

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.users = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.User1.username, "Tellvinch")
        self.assertEqual(self.User1.password, "444")

    def test_save_user(self):
        '''
        test_save_contact test case to test if the contact object is saved into
         the contact list
        '''
        self.User1.save_user()  # saving the new contact
        self.assertEqual(len(User.users), 1)


# Items up here...


    def test_save_multiple_user(self):
        '''
        test_save_multiple_contact to check if we can save multiple contact
        objects to our contact_list
        '''
        self.User1.save_user()
        test_user = User("Vinch", "555")
        test_user.save_user()
        self.assertEqual(len(User.users), 2)

    def test_delete_contact(self):
        '''
        test_delete_contact to test if we can remove a contact from our contact list
        '''
        self.User1.save_user()
        test_user = User("Yellow", "888")
        test_user.save_user()

        self.User1.delete_user()
        self.assertEqual(len(User.users), 1)

    def test_find_user_by_name(self):
        '''
        test to check if we can find a contact by phone number and display information
        '''

        self.User1.save_user()
        test_user = User("Alicia", "444")
        test_user.save_user()

        found_user = User.find_by_name("Alicia")

        self.assertEqual(found_user.username, test_user.username)


if __name__ == '__main__':
    unittest.main()
