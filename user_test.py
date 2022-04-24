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


  def reload_data(self):
        self.user_list=[]
        self.credentials_list=[]
        with open("/home/brie/dat1.txt") as file:
            for line in file:
                line = line.strip()
                self.user_list.append(line)
        file.close()
if __name__ == '__main__':
        unittest.main()
