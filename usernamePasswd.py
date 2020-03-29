#! /usr/bin/python3

import random
import os

# vairables for alphabet, numbers, temp location for username/passwords
alpha = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
number =['1','2','3','4','5','6','7','8','9','0']
userName = []
passWord = []

# randomizes the user name with 11 letters and 4 numbers
def randUser(alpha, num):
	for i in range(0,10):
		 userName.append(random.choice(alpha))
	for i in range(0,3):
		userName.append(random.choice(num))
	random.shuffle(userName)
	name = ''.join(userName)
	print("username: ", name)
	return name
# randomizes the password with 7 numbers and 5 letters
def randPass(alpha, num):
	for i in range(0,6):
		passWord.append(random.choice(num))

	for i in range(0,4):
		passWord.append(random.choice(alpha))
	random.shuffle(passWord)
	passw = ''.join(passWord)
	print("password: ", passw)
	return passw

siteUsed = input("Where will this be used?\n>>")
name = randUser(alpha, number)
passw = randPass(alpha, number)
# this creates and executes the bash command in linux shell
info = """echo "%s %s %s" >> /home/skelly/Scripting/RandUsrPw/save.txt""" % (name, passw, siteUsed)
os.system(info)
