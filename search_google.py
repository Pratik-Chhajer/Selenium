from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys 

# for chrome (giving browser name)
browser = webdriver.Chrome()

# to provide link to open
browser.get('https://www.google.com')

# threshold time till google.com is loaded
time.sleep(3)

# enter your search query here
query = "IMDB rating"

# to find input feild by name
elem = browser.find_element_by_name('q')
# to enter search query and hit enter
elem.send_keys(query + "\n")

# after long time
time.sleep(500000)

#close the browser :)
browser.close()