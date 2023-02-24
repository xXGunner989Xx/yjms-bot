import discord, io
import json, os
from player import Player

users = []

global FILE_PATH
FILE_PATH = os.environ.get('USER_FILE_PATH') if os.environ.get('USER_FILE_PATH') else "users.json"
def update_file():
    with open(FILE_PATH, "w") as fp:
        fp.write((json.dumps(users)))

def remove_user(user: str):
    if len(user) > 20:
        print("user invalid\n")
        return
    if user in users.keys():
        del users[user]
    update_file()

def add_user(author: discord.User, user: str):

    # check if user in list. if yes, update
    for i in range(len(users)):
        if (author == users[i].discord_name):
            users[i].reddit_name = user
            return
    # otherwise, add new entry
    new_entry = Player(author, user)
    print(new_entry.get_reddit_name(), new_entry.get_discord_name())
    users.append(new_entry.serialize())
    print(users)
    update_file()

def get_users() -> dict[str, discord.User]:
    return users

def update_moves(file: bytes):
    file_decoded = file.decode('utf-8').split('\r\n')
    for line in file_decoded:
        split_lines = line.split(',')
        if len(split_lines) == 2:
            for i in range(len(users)):
                if users[i].reddit_name == split_lines[0]:
                    users[i].latest_move = split_lines[1]

