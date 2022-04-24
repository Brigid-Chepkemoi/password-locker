import os
import re
import pyperclip as pc


class Credentials(object):
    system = ''
    username = ""
    password = ""
    created_by = ""
    platform = ""

    def __init__(self, created_by, username, password, platform):
        self.created_by = created_by
        self.username = username
        self.password = password
        self.platform = platform

    def create_credentials(self, credentials_list):
        if credentials_list.__contains__(
                self.created_by + '\t \t' + self.username + '\t \t' + self.password + '\t \t' + self.platform):
            print("Account already exists")
        else:
            credentials_list.append(self.created_by + ' ' + self.username + ' ' + self.password + ' ' + self.platform)
            handle = open("/home/brie/dat2.txt", "a")
            handle.write(
                self.created_by + '\t \t' + self.username + '\t \t' + self.password + '\t \t' + self.platform + '\n')
            handle.close()
            print("Credentials added successfully")

    def delete_user(self, username):
        for user in self.user_list:
            if user.username == username:
                self.user_list.remove(user)
            else:
                print("User doesn't exist")

    def show_credentials(self, credentials_list, authenticated_user):
        """
        method to show credentials for logged-in user
        """
        print('you' + '\t \t' + 'account' + '\t' + "\tpassword" + '\t' + "platform")
        for user in credentials_list:
            if user.startswith(authenticated_user):
                print(user)

    def delete_credentials(self, authenticated_user, account, platform):
        """
        method to delete credentials
        """
        input_file = open('/home/brie/dat2.txt', "r")
        output_file = open('/home/brie/dat3.txt', "w")
        output_file.write(input_file.readline())
        for line in input_file:
            if not line.lstrip().startswith(authenticated_user + "\t \t" + account) and not line.lstrip().endswith(
                    platform):
                output_file.write(line)
        input_file.close()
        output_file.close()
        os.rename('/home/brie/dat3.txt', '/home/brie/dat2.txt')
        print('Account deleted')

    def copy_credentials(self,credentials_list,authenticated_user, account, platform):
        for accnt in credentials_list:
            if accnt.lstrip().startswith(authenticated_user + "\t \t" + account) and accnt.lstrip().endswith(platform):
                info_list = re.split(r'\t+',accnt)
                while (" " in info_list):
                    info_list.remove(" ")
                print(info_list)
                print(info_list[2])
                pc.copy(info_list[2])
