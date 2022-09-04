import os
import sys
from user_pass import user_pass
import pywhatkit
import bcrypt

curly = '}'

def login(user, password):
	try:
		if bcrypt.checkpw(password.encode("utf-8"), user_pass[user]):
			print('Logged in')
			loggedin = True

		else:
			print('The password is incorrect' )
			loggedin = False

	except:
		print('The user doesn\'t exist')
		loggedin = False

	return user, loggedin

def start(user):
	pywhatkit.playonyt('https://youtu.be/xvFZjo5PgG0')
	return f'Welcome {user}'

def set_user(new_user, new_user_pass):
	if new_user in user_pass:
		sys.exit('User already exists')
	else:
		hashed = bcrypt.hashpw(new_user_pass.encode("utf-8"), bcrypt.gensalt())
		f = open('user_pass.py', 'ab+')
		f1 = open('user_pass.py', 'a+')
		f.seek(-1, os.SEEK_END)
		f.truncate()
		f1.write(f'	\'{new_user}\' : {hashed}, \n{curly}')
		f.flush()
		f1.flush()
		f.close()
		f1.close()
		return 'for pytest'

def login_or_create(l):

	if l.lower().strip() == 'l':
		user = input('Enter your username: ')
		password = input('Enter password: ')
		user, loggedin = login(user, password)

	elif l.lower().strip() == 'c':
		new_user = input('New username: ')

		new_user_pass = input('Password: ')

		set_user(new_user, new_user_pass)

		print('User created')
		sys.exit(0)

	else:
		sys.exit('An error occurred, try again')

	if loggedin == True:
		print(start(user))

def main():
	return login_or_create(input('Press and enter "l" to login or "c" to create an account: '))

if __name__ == '__main__':
	main()