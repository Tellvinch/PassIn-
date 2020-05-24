import unittest  # Importing the unittest module
from credentials import Credentials  # Importing the user class


class TestCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.User1 = Credentials("Github", "444")  #

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.accounts = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.User1.account_name, "Github")
        self.assertEqual(self.User1.account_password, "444")

    def test_save_credentials(self):
        '''
        test_save_contact test case to test if the contact object is saved into
         the contact list
        '''
        self.User1.save_accounts()  # saving the new contact
        self.assertEqual(len(Credentials.accounts), 1)

    def test_save_multiple_user(self):
        '''
        test_save_multiple_contact to check if we can save multiple contact
        objects to our contact_list
        '''
        self.User1.save_accounts()
        test_accounts = Credentials("youtube", "555")  # new contact
        test_accounts.save_accounts()
        self.assertEqual(len(Credentials.accounts), 2)

    def test_delete_account(self):
        '''
        test_delete_account to test if we can remove an account from our accounts
        '''
        self.User1.save_accounts()
        test_credentials = Credentials("facebook", "888")
        test_credentials.save_accounts()

        self.User1.delete_accounts()
        self.assertEqual(len(Credentials.accounts), 1)

    def test_find_credential_by_name(self):
        '''
        test to check if we can find a contact by phone number and display information
        '''

        self.User1.save_accounts()
        test_credentials = Credentials("Alicia", "444")
        test_credentials.save_accounts()

        found_credentials = Credentials.find_by_name("Alicia")

        self.assertEqual(found_credentials.account_name,
                         test_credentials.account_name)

    def test_account_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the contact.
        '''

        self.User1.save_accounts()
        test_credentials = Credentials("test", "2222")
        test_credentials.save_accounts()

        account_exists = Credentials.account_exist("2222")

        self.assertTrue(account_exists)

    def test_display_all_accounts(self):
        '''
        method that returns a list of all contacts saved
        '''

        self.assertEqual(Credentials.display_accounts(), Credentials.accounts)


if __name__ == '__main__':
    unittest.main()
