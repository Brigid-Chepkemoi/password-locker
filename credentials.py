class Credentials(object):
    system = ''
    username = ""
    password = ""

    def __init__(self, username, password, system):
        self.username = username
        self.password = password
        self.system = system

    def create_credentials(self, credentials_list):
        if credentials_list.__contains__(self.username):
            print("Account already exists")
        else:
            credentials_list.append(self)

    def modify_user(self, username, email):
        for user in self.user_list:
            if user.username == username:
                self.user_list.remove(user)
                self._init_(username, email)
            else:
                print("User doesn't exist")

    def delete_user(self, username):
        for user in self.user_list:
            if user.username == username:
                self.user_list.remove(user)
            else:
                print("User doesn't exist")
