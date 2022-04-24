from credentials import Credentials
from user import User


class Main:
    credentials_list = []
    user_list = []
    # def authenticate(self):

    def main_menu(self):

        print("Press 1 to create a user")
        print("Press 2 to login to a  user account")
        next_action = input("select next action: ")
        if next_action == '1':
            self.create_user()
        # elif next_action == '2':
            #self.authenticate()
        else:
            exit()

    def create_user(self):
        """
        this method creates users for our application
          """
        login = input("Enter username: ")
        auth = input("Enter Password: ")
        auth2 = input("Confirm Password: ")
        user = User(login, auth, auth2)
        # self.user_list.append(user)
        user.create_user(self.user_list)
        # self.main_menu()

    def create_credentials(self):
        username = input("Enter username: ")
        password = input("Enter Password: ")
        credentials = Credentials(username, password)
        credentials.create_credentials(self.credentials_list)
        self.main_menu()


if __name__ == '__main__':
    Main().main_menu()
