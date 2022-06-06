import json
import os

DB_FOLDER_NAME = "db"
USERS_FILE_NAME = "users.txt"
DB_FOLDER_FILE_NAME = os.path.abspath(USERS_FILE_NAME)



def register(username, password, first_name, last_name):
    # with open(DB_FOLDER_FILE_NAME, "r+") as file:
    with open("../db/users.txt", "r+") as file:
        for user_line in file:
            user = json.loads(user_line.strip())
            if user["username"] == username:
                return False

        user_obj = {
            "username": username,
            "password": password,
            "firstName": first_name,
            "lastName": last_name
        }

        file.write(json.dumps(user_obj))
        file.write("\n")
        return True


def login(username, password):
    # with open(os.path.join(DB_FOLDER_NAME, USERS_FILE_NAME), "r") as file:
    with open("../db/users.txt", "r") as user, open("../db/session.txt", "w") as session:
        for user_line in user:
            user = json.loads(user_line.strip())
            if user["username"] == username and user["password"] == password:
                session.write(user_line)

                return True
            return False

