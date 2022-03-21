#!/usr/bin/env python3
'''
Takes emails in csv format and returns Google bulk enrollment and bulk Onboarding Ticket creation
'''
import re, random, string, csv

def main():
	# Initialize dictionary that will be used in following format {'email': ['username', 'first name', 'last name', 'password']}
	#userData = {}
	# Get list of emails
	# From list append username, first, and last name to userData dictionary
	setEmailUserFirstLast(readCSV(), userData)
	# Use data in userData to create Google import and pass created list into writeToCSV function to write data to csv
	writeToCSV(googleImport(userData))
	# Write username and password to txt file for trainer
	infoForTrainers(userData)

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
		matched = re.match(r"(([a-z'-]*)\.([a-z'-]*)(_\w*)?)@id\.me", key)
		dictionary[key] += [matched.group(1), matched.group(2).title(), matched.group(3).title(), getPassword()]
	return dictionary

def googleImport(dictionary):
	# Create google header
	googleCSV = []
	googleHeader = ['First Name [Required]', 'Last Name [Required]', 'Email Address [Required]',	'Password [Required]',	'Password Hash Function [UPLOAD ONLY]',	'Org Unit Path [Required]',	'New Primary Email [UPLOAD ONLY]',	'Recovery Email',	'Home Secondary Email',	'Work Secondary Email',	'Recovery Phone [MUST BE IN THE E.164 FORMAT]',	'Work Phone',	'Home Phone',	'Mobile Phone',	'Work Address',	'Home Address',	'Employee ID',	'Employee Type',	'Employee Title',	'Manager Email',	'Department',	'Cost Center',	'Building ID',	'Floor Name',	'Floor Section',	'Change Password at Next Sign-In',	'New Status [UPLOAD ONLY]',	'Advanced Protection Program enrollment']
	googleCSV.append(googleHeader)
	
	# Append data in dictionary to list which will then be written to CSV
	for key in dictionary:
		googleCSV.append([dictionary[key][1], dictionary[key][2], key, dictionary[key][3],'','/','','','','','','','','','','','','','','','','','','','','True','',''])
	return googleCSV

def writeToCSV(googleCSV):
	with open('googleImport.csv', 'w', encoding='UTF8', newline='') as googleFile:
		writer = csv.writer(googleFile)
		# Write rows using data from import data
		writer.writerows(googleCSV)

def infoForTrainers(dictionary):
	with open('sendToTrainer.txt', 'w') as file:
		for key in dictionary:
			file.write("Name: " + dictionary[key][1] + " " + dictionary[key][2] + "\n" + "Username: " + dictionary[key][0] + "\n" + "Password: " + dictionary[key][3] + "\n" + "\n")
		

main()
		