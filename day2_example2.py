"""

"""

class LoginNileshException(Exception):
    pass

def login(username, password):
    if (username == "nilesh"):
        raise LoginNileshException()

def auto_login():
    print('automatically logged in nilesh')

try:
    login("nilesh", "npass")
except LoginNileshException as e:
    auto_login()