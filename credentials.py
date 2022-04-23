class Credentials(object):
    username = ""
    password = ""

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def create_credentials(self, credentials_list):
        if credentials_list.__contains__(self.username):
            print("Account already exists")
        else:
            credentials_list.append(self)

