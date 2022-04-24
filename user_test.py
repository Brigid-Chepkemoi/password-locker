import unittest



from user import User

class TestUser(unittest.TestCase):

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.user_list = self.user_list("James", "p1", "p1")

    def test_init(self):

        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.user_list.username, "James")
        self.assertEqual(self.user_list.password, "p1")
        self.assertEqual(self.user_list.password2, "p1")

   def show_credentials(self, credentials_list, authenticated_user):
        """
        method to show credentials for logged-in user
        """
        print('you' + '\t \t' + 'account' + '\t' + "\tpassword" + '\t' + "platform")
        for user in credentials_list:
            if user.startswith(authenticated_user):
                print(user)

if __name__ == '__main__':
        unittest.main()
