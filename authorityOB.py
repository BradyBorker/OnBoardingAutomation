#!/usr/bin/env python3
'''
Automate authority process:
1) Click 'New User'
2) Fill in Full Name, Email, Username
3) Generate and fill random password
4) Click 'Create User'
5) Click "Edit User"
6) Click "Add New Application"
7) Click "Support"
8) Add role ("video_call_tr", "general_support", etc.)
9) Click "Create User Application
10) Click "Users" and repeat until done

Functions:
.moveTo(x, y, duration)
.position()
.click()
.typewrite("string")

time.sleep()

'''
import pyautogui, time, csv, re, random, string

def main():
	userData = {}
	role = "\"video_call_tr\""
	setEmailUserFirstLast(readCSV(), userData)
	
	for key in userData:
		stepOne()
		stepTwo(key, userData)
		stepThree(role)
	

# Click 'New User'
def stepOne():
	pyautogui.moveTo(3678, 214, duration=1)
	pyautogui.click()
	pyautogui.click()
	pyautogui.click()
	time.sleep(3)

# Fill in Name, Email, Username, Password, and Password Confirmation.
# Click 'Create User'
def stepTwo(key, dictionary):
	pyautogui.moveTo(2296, 381, duration=1)
	pyautogui.click()
	pyautogui.typewrite(dictionary[key][1] + ' ' + dictionary[key][2] + ' ' + dictionary[key][4])
	pyautogui.typewrite(["tab"])
	pyautogui.typewrite(key)
	pyautogui.typewrite(["tab"])
	pyautogui.typewrite(dictionary[key][0])
	pyautogui.typewrite(["tab"])
	pyautogui.typewrite(dictionary[key][3])
	pyautogui.typewrite(["tab"])
	pyautogui.typewrite(dictionary[key][3])
	pyautogui.moveTo(1895, 780, duration=1)
	# Click 'Create User'
	pyautogui.click()
	time.sleep(3)

# Click edit user, click 'add new application'
# Click Application, click support, add role, 'create user application'
def stepThree(role):
	pyautogui.moveTo(3504, 214, duration=1)
	pyautogui.click()
	pyautogui.moveTo(1909, 846, duration=1)
	pyautogui.click()
	pyautogui.moveTo(2284, 413, duration=1)
	pyautogui.click()
	pyautogui.moveTo(2259, 621, duration=1)
	pyautogui.click()
	pyautogui.moveTo(2227, 465, duration=1)
	pyautogui.click()
	pyautogui.typewrite(role)
	pyautogui.moveTo(1934, 890, duration=1)
	pyautogui.click()
	time.sleep(5)
	
	pyautogui.moveTo(2090, 155, duration=1)
	pyautogui.click()
	time.sleep(2)
	
def readCSV():
	userList = []
	with open('userImportList.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		for row in csv_reader:
			userList.append(row)
	return userList

def getPassword():
	source = string.ascii_letters + string.digits + random.choice('!@#$%^&()')
	# Set guaranteed upper, lower, digits, and special chars
	password = random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase) + random.choice(string.digits) + random.choice('!@#$%^&()')
	# Append random characters to end
	for i in range(8):
		password += random.choice(source)
	return password

def setEmailUserFirstLast(emailList, dictionary):
	# Sets emails collected from readCSV() as key in userData dictionary
	for emails in emailList:
		dictionary[''.join(emails)] = []
	# appends username, first, and last name into dictionary
	for key in dictionary:
		matched = re.match(r"(([a-z'-]*)\.([a-z'-]+)\.?([a-z'-]*)_?(\w*)?)@id\.me", key)
		if matched.group(5):
			if matched.group(4):
				dictionary[key] += [matched.group(1), matched.group(2).title() + ' ' + matched.group(3).title(), matched.group(4).title(), getPassword(), matched.group(5)]
			else:
				dictionary[key] += [matched.group(1), matched.group(2).title(), matched.group(3).title(), getPassword(), matched.group(5)]
		else:
			if matched.group(4):
				dictionary[key] += [matched.group(1), matched.group(2).title() + ' ' + matched.group(3).title(), matched.group(4).title(), getPassword()]
			else:
				dictionary[key] += [matched.group(1), matched.group(2).title(), matched.group(3).title(), getPassword()]
	return dictionary
	
main()

'''
jenna.tutein_allm@id.me
lydia.caines_allm@id.me
mark.diaz_allm@id.me
stephanie.fine_allm@id.me
nigel.gordon_allm@id.me
tasha.johnson_allm@id.me
deasha.marcellus_allm@id.me
mercedes.marshall_allm@id.me
kiser.merrow_allm@id.me
amanda.myers_allm@id.me
jonathan.page_allm@id.me
al.paul_allm@id.me
juan.paulino_allm@id.me
mattison.perez_allm@id.me
'''