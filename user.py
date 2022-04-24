class User:
    """
    This class creates a new user
    """
    username = ""
    password = ""
    password2 = ""
    user_list = []

    authenticated = False

    def __init__(self, login, auth, auth2):
        self.username = login
        self.password = auth
        self.password2 = auth2

    def create_user(self, user_list):
        """
        Method to save a user
        """
        self.user_list = user_list
        if self.username+' '+self.password in self.user_list:
            print("User already exists")
        elif self.password != self.password2:
            print("Password does not match")
        else:
            self.user_list.append(self)
            handle = open("/home/brie/dat1.txt", "a")
            handle.write(self.username+' '+self.password+'\n')
            handle.close()
            print(self.username+' '+self.password)
            print("User added successfully")

    def get_user(self, username):
        """
        Method to modify  a username
        """
        for user in self.user_list:
            if user.username == username:
                return user
            else:
                return 0


