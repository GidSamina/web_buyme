import select
import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.edge.options import Options


#A. Registration screen
# login to site
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.get('https://buyme.co.il/')
sleep(30)

#register to user

login_button = driver.find_element(By.XPATH, '//*[@id="ember1143"]/div/ul[1]/li[3]/a')
login_button.click()
print(f'my {login_button}')
sleep(5)

# open a new mail
element = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[1]/div[2]/div/div[2]/div[2]/div[2]/div/div[2]')
element.click()
sleep(2)

# add mail address

email_box = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[1]/div[2]/div/div[2]/div[3]/div/form/div/label/input')
email_box.send_keys('gidonnew.samina@gmail.com')
sleep(2)

# press enter

press_enter = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[1]/div[2]/div/div[2]/div[3]/div/form/button')
press_enter.click()
sleep(30) # wait 30 second to user to add the password send to mail

# for first login add a full name

# full_name = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[1]/div[2]/div/div[2]/div[2]/form/div[1]/label/input')
# full_name.send_keys('Gideon Samian ')
# sleep(3)

# add a cell phone
# phon_num = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[1]/div[2]/div/div[2]/div[2]/form/div[2]/div/div/div/label/input')
# phon_num.send_keys('528342715')
# sleep(4)

# select I am agree option

# agree_to_register = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[1]/div[2]/div/div[2]/div[2]/form/div[3]/div')
# agree_to_register.click()
# sleep(2)

# press enter to register
#
# press_to_register = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[1]/div[2]/div/div[2]/div[2]/form/button')
# press_to_register.click()
# sleep(2)
