class User:
    user_list = []
    username = ""
    email = ""
    authenticated = False

    def __init__(self, username, email, user_list):
        self.username = username
        self.email = email
        self.user_list = user_list

    def save_user(self):
        if self in self.user_list:
            print("user already exist")
        else:
            self.user_list.append(self)
            print("User added successfully")

    def get_user(self, username):
        for user in self.user_list:
            if user.username == username:
                return user
            else:
                return 0

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
