# a2.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Bryce Wong
# EMAIL
# STUDENT ID

from pathlib import Path
import Profile
import time
administrator_mode = False
current_file = None
timestamp = time.time()

def mode():
    global administrator_mode
    mode  = input("Enter  Mode: ")
    if 'admin' in mode:
        administrator_mode = True
    else:
        administrator_mode  = False
    return administrator_mode


def edit_file(command = None):
    global administrator_mode
    if administrator_mode:
        path = command[1]
        print(path)
        profile = Profile.Profile()
        profile.load_profile(path = path)
        if '-bio' in command:
            bio_index = command.index('-bio')
            bio = command[bio_index+1]
        else:
            bio_index = 0
        if '-usr' in command:
            index = command.index('-usr')
            new = " ".join(command[index + 1]).strip('"')
            profile.username = new
            profile.save_profile(path)
            print("username updated")
        if '-pwd' in command:
            index = command.index('-pwd')
            new = command[index + 1]
            profile.password = new.strip('"')
            profile.save_profile(path)
            print("password updated")
        if '-bio' in command:
            profile.bio = bio.strip('"')
            profile.save_profile(path)
            print("bio updated")
        if '-addpost' in command:
            index = command.index('-addpost')
            post = " ".join(command[index + 1])
            new_post = Profile.Post(post, timestamp=timestamp)
            profile.add_post(new_post)
            profile.save_profile(path)
            print('post added')
        start()
    else:
        if current_file is not None:
            profile = Profile.Profile()
            profile.load_profile(path = current_file)
            print("""
            edit commands:
            pwd - update password
            bio - update bio
            usr - update username
            addpost - add a post 
            """)
            second_command = input("")
            if 'pwd' in second_command:
                new_password = input("input new password:  ")
                if new_password == 'admin':
                    administrator_mode = True
                    start()
                profile.password = new_password
                profile.save_profile(current_file)
                print("password updated")
            if 'bio' in second_command:
                new_bio = input("input new bio: ")
                if new_bio == 'admin':
                    administrator_mode = True
                    start()
                profile.bio = new_bio
                profile.save_profile(current_file)
                print("updated bio")
            if 'usr' in second_command:
                new_usr = input("input new username: ")
                if new_usr == 'admin':
                    administrator_mode = True
                    start()
                profile.username = new_usr
                profile.save_profile(current_file)
                print("username updated")
            if 'addpost' in second_command:
                post = input("input post: ")
                if post == 'admin':
                    administrator_mode = True
                    start()
                post = Profile.Post(post, timestamp=timestamp)
                profile.add_post(post)
                profile.save_profile(current_file)
                print("added post")
        else:
            print("please open a file first")
            start()
        start()



def read_file(command = None):
    global administrator_mode
    if administrator_mode:
        file_path = command[1]
        if Path(file_path).exists():
            with open(file_path, 'r')as file:
                lines = file.readlines()
                if lines:
                    for line in lines:
                        print(line)
                else:
                    print("EMPTY")
                    start()
        else:
            print("ERROR")
    else:
        path  = input("input file path:")
        if path == 'admin':
            administrator_mode = True
            start()
        if Path(path).exists():
            with open(path, 'r')as file:
                lines = file.readlines()
                if lines:
                    for line in lines:
                        print(line)
                else:
                    print("EMPTY")
                    start()
        else:
            print("ERROR")

    start()


def delet_file(command):
    global administrator_mode
    if administrator_mode:
        file_path = command[1]
        if Path(file_path).exists():
            Path(file_path).unlink()
            print(f"{file_path} DELETED")
        else:
            print("ERROR")
    else:
        path = input("input file path: ")
        if path == 'admin':
            administrator_mode = True
            start()
        if Path(path).exists():
            Path(path).unlink()
            print(f"{path} DELETED")
        else:
            print("ERROR")
    start()


def start():
    global administrator_mode
    if administrator_mode:
        print("administrator mode")
        command = input("Please Enter Command: ")
        command_list = command.split(' ')
        type = command_list[0]
        if type == 'C':
            create_file(command_list)
        elif type == 'R':
            read_file(command_list)
        elif type == 'D':
            delet_file(command_list)
        elif type == 'O':
            open_file(command_list)
        elif type == 'E':
            edit_file(command_list)
        elif type == 'P':
            print_data(command_list)
        else:
            print("Please Enter Correct Command")
            start()
    else:
        command = input("Please Enter Command: ")
        if command == 'admin':
            administrator_mode = True
            start()
        if command == 'C':
            create_file()
        if command == 'O':
            open_file()
        if command == 'R':
            read_file()
        if command == 'D':
            delet_file()
        if command == 'E':
            edit_file()
        if command == 'P':
            print_data()


def create_file(command = None):
    global administrator_mode
    if administrator_mode:
        dir_path = command[1]
        command_extention = command[2]
        file_name = command[3]
        file_path = f"{dir_path}\\{file_name}.dsu"
        if Path(file_path).exists():
            print("file already exists")
        else:
            Path(file_path).touch()
            print(f'{file_path}')
        use = input("username: ")
        password = input('password: ')
        bio = input('input bio: ')
        profile = Profile.Profile(username=use, password=password)
        profile.bio = bio
        profile.save_profile(path = file_path)
        start()
    else:
        directory = input("input directory path: ")
        if directory == 'admin':
            administrator_mode = True
            start()
        name = input("input file name: ")
        if name == 'admin':
            administrator_mode = True
            start()
        file_path = f"{directory}\\{name}.dsu"
        if Path(file_path).exists():
            print("file already exists")
        else:
            Path(file_path).touch()
            print(f"file: {name}.dsu created at {file_path}")
        use = input("Enter username: ") 
        if use == 'admin':
            administrator_mode = True
            start()
        password = input("Enter password: ")
        if password == 'admin':
            administrator_mode = True
            start()
        bio = input("Enter bio: ")
        if bio == 'admin':
            administrator_mode = True
            start()
        profile = Profile.Profile(username=use, password=password)
        profile.save_profile(path = file_path)
        start() 


def print_data(command = None):
    global administrator_mode
    global current_file
    if administrator_mode:
        file = command[1]
        profile = Profile.Profile()
        profile.load_profile(file)
        print(command)
        if '-usr' in command:
            print("Username:", profile.username)
        if '-pwd' in command:
            print("Password:", profile.password)
        if '-bio' in command:
            print("Bio:", profile.bio)
        if '-posts' in command:
            for i, post in enumerate(profile._posts):
                print(f"Post {i}: {post}")
        if '-post' in command:
            post_index = command.index('-post')
            post_id = int(command[post_index + 1])
            if 0 <= post_id < len(profile._posts):
                print(f"Post {post_id}: {profile._posts[post_id]}")
            else:
                print("Invalid post ID")
        if '-all' in command:
            print("Username:", profile.username)
            print("Password:", profile.password)
            print("Bio:", profile.bio)
            print("Posts:")
            for i, post in enumerate(profile._posts):
                print(f"  Post {i}: {post}")
        start() 
    else:
        if current_file is not None:
            profile = Profile.Profile()
            profile.load_profile(path = current_file)
            print("""
            print commands:
            pwd - print password
            bio - print bio
            usr - print username
            post - print posts
            all - print all 
            """)
            comm = input("input command: ")
            if comm == 'admin':
                administrator_mode = True
                start()
            if 'pwd' in comm:
                print("Password:", profile.password)
            if 'usr' in comm:
                print("Username:", profile.username)
            if profile.bio:
                if 'bio' in command:
                    print("Username:", profile.bio)
            if 'post' in comm:
                print("posts:")
                for i, post in enumerate(profile._posts):
                    print(f"  Post {i}: {post}")
            if 'all' in comm:
                print("Username:", profile.username)
                print("Password:", profile.password)
                print("Bio:", profile.bio)
                print("Posts:")
                for i, post in enumerate(profile._posts):
                    print(f"  Post {i}: {post}")
        
            
        else:
            print("please open a file first")
            start()
    start()



def open_file(command = None):
    global administrator_mode
    global current_file
    if administrator_mode:
        path = command[1]
        current_file = path
      
    else:
        path = input("enter file path: ")
        if path == 'admin':
            administrator_mode = True
            start()
        print(f"file opened: {path}")
        current_file = path

    start()


if __name__ == "__main__":
    mode()
    if not administrator_mode:
         print("""
        List of Commands:
        C - create file
        R - read file
        D - delete file
        O - open file
        E - edit a file
        P - print contents of file
        """)
    start()
