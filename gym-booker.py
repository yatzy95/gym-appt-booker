import time
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions

CLIENT_EMAIL = os.environ.get('CLIENT_EMAIL')
CLIENT_PASSWORD = os.environ.get('CLIENT_PASSWORD')

book_time = input('What time would you like to book for the gym today? (format XX:XXAM or XX:XXPM)\n')

options = webdriver.ChromeOptions()
options.binary_location = "/home/john/.local/chrome-linux/chrome"
chrome_driver_path = "/home/john/projects/gym-booking/myenv/bin/chromedriver"

driver = webdriver.Chrome(chrome_driver_path, options=options)
driver.get('https://www.myasfaccount.com/Mylogin.aspx')
time.sleep(3)
driver.find_element_by_id('emailAddr').send_keys(CLIENT_EMAIL)
time.sleep(1)
driver.find_element_by_id('pin').send_keys(CLIENT_PASSWORD)
time.sleep(1)
driver.find_element_by_id('signin').click()
time.sleep(1)
driver.find_element_by_class_name('ptsched').click()
window2 = driver.window_handles[1]
driver.switch_to.window(window2)
driver.find_element_by_id('gvTrainAtt_chkRow_0').click()
time.sleep(1)
time_list = driver.find_elements_by_class_name('fc-event-time')

for available_time in time_list:
    try:
        if book_time in available_time.text:
            available_time.click()
    except exceptions.StaleElementReferenceException:
        pass

time.sleep(1)
driver.find_element_by_id('butBook').click()


