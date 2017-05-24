from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys 

# for chrome (giving browser name)
browser = webdriver.Chrome()

# to provide link to open
browser.get('https://www.facebook.com')

# threshold time till google.com is loaded
time.sleep(3)

# reading log in credentials from fb_credentials.txt
file = open('fb_credentials.txt', 'r')

# first line is email
email = file.readline()

# removing \n from end
email = email[:-1]

# second line is password
password = file.readline()

# to find input feild by name
email_element = browser.find_element_by_name('email')

# to enter search query and hit enter
email_element.send_keys(email)

# to find input feild by name
password_element = browser.find_element_by_name('pass')

# to enter search query and hit enter
password_element.send_keys(password + '\n')

# after long time
time.sleep(500000)

#close the browser :)
browser.close()