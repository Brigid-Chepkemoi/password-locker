from credentials import Credentials


class Main:
    credentials_list = []

    def menu(self):
        print("Press 1 to create a user")
        print("Press 2 to to show users")
        print("Press 3 to create a credentials")
        next_action = input("select next action: ")
        if next_action == '3':
            self.create_credentials()
        else:
            exit()

    def create_user(self):
        username = input("Enter username: ")
        password = input("Enter Password: ")
        credentials = Credentials(username, password)
        credentials.create_credentials(self.credentials_list)
        self.menu()

    def create_credentials(self):
        username = input("Enter username: ")
        password = input("Enter Password: ")
        credentials = Credentials(username, password)
        credentials.create_credentials(self.credentials_list)
        self.menu()


if __name__ == '__main__':
    Main().menu()
