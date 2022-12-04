import os

def get_user():
    return os.getenv('USER',os.getenv('USERNAME','none' ))

print(get_user())