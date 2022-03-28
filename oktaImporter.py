#!/usr/bin/env python3
#!/usr/bin/env python3
'''
This program will automate the okta user import process.
!!! Make sure 'Set by admin' is set !!!
'''

import pyautogui, time, json

def main():
	# Get user data from JSON file
	userData = getUserData()
	# Add users in userData to okta
	for key in userData:
		addUser(key, userData)
		
def getUserData():
	f = open('userData.json')
	data = json.load(f)
	return data

def addUser(key, dictionary):
	# Move to 'First name'
	pyautogui.moveTo(2756, 409, duration=.1)
	pyautogui.click()
	pyautogui.click()
	# Write First name
	pyautogui.typewrite(dictionary[key][1])
	pyautogui.typewrite(["tab"])
	# Write Last name
	pyautogui.typewrite(dictionary[key][2])
	pyautogui.typewrite(["tab"])
	# Write Username
	pyautogui.typewrite(dictionary[key][0])
	pyautogui.typewrite(["tab"])
	# Write Email
	pyautogui.typewrite(key)
	# Write Password
	pyautogui.moveTo(2801, 784, duration=.5)
	pyautogui.click()
	pyautogui.typewrite(dictionary[key][3])
	# Click 'Save and Add Another'
	pyautogui.moveTo(2898, 917, duration=.5)
	pyautogui.click()
	time.sleep(1)

main()