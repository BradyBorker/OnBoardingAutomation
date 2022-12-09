#!/usr/bin/env python3

import pyautogui, time, csv, random, string

class Users_Container:
  user_ids = 0

  def __init__(self, users={}):
    self.users = users

  def add_user(self, user_information):
    self.users[self.user_ids] = user_information
    self.users[self.user_ids]['FullName'] = ' '.join([self.users[self.user_ids]['First']] + [self.users[self.user_ids]['Last']])
    self.users[self.user_ids]['Password'] = create_password()

    self.user_ids += 1

  def set_user_names(self):
    for id in self.users.keys():
      if self.users[id]['Status'] == 'BPO':
        self.users[id]['UserName'] = '.'.join(self.users[id]['FullName'].lower().split(' ')) + '_' + self.users[id]['Location'].lower()
      else:
        self.users[id]['UserName'] = '.'.join(self.users[id]['FullName'].lower().split(' '))

  def set_emails(self):
    for id in self.users.keys():
      self.users[id]['Email'] = self.users[id]['UserName'] + '@id.me'

def read_users_from_csv(users):
  with open('BPO_Hires.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    for row in csv_reader:
      users.add_user(row)

def create_password(password_length=16):
	source = string.ascii_letters + string.digits + random.choice('!@#$%^&()')
	password = random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase) + random.choice(string.digits) + random.choice('!@#$%^&()')
	for i in range(password_length-len(password)):
		password += random.choice(source)
	return password

def fill_authority_form(user_data):
  # New User
  pyautogui.moveTo(3623, 222, duration=.5)
  pyautogui.click()
  pyautogui.click()
  time.sleep(1)
  # Fill out form: Name, Email, Username
  pyautogui.moveTo(2262, 407, duration=.5)
  pyautogui.click()
  pyautogui.typewrite(user_data['FullName'])
  pyautogui.typewrite(["tab"])
  pyautogui.typewrite(user_data['Email'])
  pyautogui.typewrite(["tab"])
  pyautogui.typewrite(user_data["UserName"])
  pyautogui.typewrite(["tab"])
  random_password = create_password()
  pyautogui.typewrite(random_password)
  pyautogui.typewrite(["tab"])
  pyautogui.typewrite(random_password)
  pyautogui.moveTo(1911, 855)
  pyautogui.click()

def main():
  users = Users_Container()
  read_users_from_csv(users)
  users.set_user_names()
  users.set_emails()
  #for id in users.users.keys():
  #  fill_authority_form(users.users[id])
  fill_authority_form(users.users[0])

main()
