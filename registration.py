from user import User

user = User()



email = input('Enter Your Email')
password = input('Enter Your Password')
print(User.login(email, password))





