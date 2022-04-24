import os
from time import sleep

from credentials import Credentials
from user import User


class Main:
    credentials_list = []
    user_list = []
    authenticated_user = ""
    authenticated_password = ""
    cred_name = ""
    cred_password = ""
    cred_platform = ""

    def authenticate(self):
        self.screen_clear()
        login = input("Enter username: ")
        password = input("Enter password: ")
        user = login + ' ' + password
        if user in self.user_list:
            self.authenticated_user = login
            self.authenticated_password = password
            self.credentials_menu()
        else:
            print("Wrong username and password combination ")
            sleep(5)
            self.authenticate()

    def main_menu(self):
        self.screen_clear()
        self.reload_data()
        print("Press 1 to create a user")
        print("Press 2 to login to a  user account")
        next_action = input("select next action: ")
        if next_action == '1':
            self.create_user()
        elif next_action == '2':
            self.authenticate()
        else:
            exit()

    def credentials_menu(self):
        self.screen_clear()
        print("Press 1 to show your credentials")
        print("Press 2 to add a new credentials to your list")
        print("Press 3 to delete credentials")
        print("Press 4 to copy credentials")
        action = input("select next action: ")
        credentials = Credentials(self.authenticated_user, self.cred_name, self.cred_password, self.cred_platform)
        if action == "1":
            credentials.show_credentials(self.credentials_list, self.authenticated_user)
        elif action == "2":
            self.create_credentials()
        elif action == "3":
            self.screen_clear()
            accnt_to_del = input("Enter the account name to delete: ")
            pltfrm_to_del = input("Enter the platform for the account to delete: ")
            credentials.delete_credentials(self.authenticated_user, accnt_to_del, pltfrm_to_del)
        elif action == "4":
            self.screen_clear()
            self.reload_data()
            accnt_to_copy = input("Enter the account name for the password you want to copy: ")
            pltfrm_to_copy = input("Enter the platform for the account to copy: ")
            credentials.copy_credentials(self.credentials_list, self.authenticated_user, accnt_to_copy, pltfrm_to_copy)
        else:
            self.credentials_menu()

    def create_user(self):
        """
        this method creates users for our application
          """
        self.screen_clear()
        login = input("Enter username: ")
        auth = input("Enter Password: ")
        auth2 = input("Confirm Password: ")
        user = User(login, auth, auth2)
        # self.user_list.append(user)
        user.create_user(self.user_list)
        # self.main_menu()

    def create_credentials(self):
        """
        Method to create new credentials
        """
        self.screen_clear()
        username = input("Enter username: ")
        password = input("Enter Password: ")
        platform = input("Enter the platform to which these credentials belong: ")
        credentials = Credentials(self.authenticated_user, username, password, platform)
        credentials.create_credentials(self.credentials_list)
        self.main_menu()

    def screen_clear(self):
        if os.name == 'posix':
            _ = os.system('clear')
        else:
            _ = os.system('cls')

    def reload_data(self):
        self.user_list=[]
        self.credentials_list=[]
        with open("/home/brie/dat1.txt") as file:
            for line in file:
                line = line.strip()
                self.user_list.append(line)
        file.close()

        with open("/home/brie/dat2.txt") as file:
            for line in file:
                line = line.strip()
                self.credentials_list.append(line)
        file.close()


if __name__ == '__main__':
    Main().main_menu()
