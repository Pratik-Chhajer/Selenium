from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys 

# for chrome (giving browser name)
browser = webdriver.Chrome()

# to provide link to open
browser.get('http://en.savefrom.net/')

# threshold time till google.com is loaded
time.sleep(3)

# video link
video_link = 'https://www.youtube.com/watch?v=Fl4KQJ7o3ps'

# to find input feild by name
search_element = browser.find_element_by_name('sf_url')

# to enter search query and hit enter
search_element.send_keys(video_link + '\n')

time.sleep(5)

downlaod_button = browser.find_element_by_xpath('//*[@id="sf_result"]/div/div[1]/div[2]/div[2]/div[1]/a')
downlaod_button.click()

# after long time
time.sleep(500000)

#close the browser :)
browser.close()