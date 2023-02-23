import discord, io
import json, os

users = {}
moves = {}

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
    users[user.split()[1]] = author
    print(users)
    update_file()

def get_users() -> dict[str, discord.User]:
    return users

def update_moves(file: bytes):
    file_decoded = file.decode('utf-8').split('\r\n')
    for line in file_decoded:
        split_lines = line.split(',')
        if len(split_lines) == 2:
            moves[split_lines[0]] = split_lines[1]

def get_moves() -> dict[str, str]:
    return moves

