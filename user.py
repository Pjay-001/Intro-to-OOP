class User:
    def __init__(self, schoolName, schoolAddress):


    def register(self, name, phone, email, password):
        return name

    def login(self, name, phone, email, password):
        if email == 'test@gmail.com' and password == 'abc':
            return True
        else:
            return False
    def show(self):

