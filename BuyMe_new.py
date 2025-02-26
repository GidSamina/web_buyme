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
import pyperclip
import pyautogui


#A. Registration screen

#login to site
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.get('https://buyme.co.il/')
sleep(5)


#register to user
login_button = driver.find_element(By.XPATH, '//*[@id="ember1143"]/div/ul[1]/li[3]/a')
login_button.click()
sleep(10)


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
url = driver.current_url
with open("urls.txt", "a") as file:
    file.write(url + "\n")
sleep(3)


# for first login add a full name
# full_name = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[1]/div[2]/div/div[2]/div[2]/form/div[1]/label/input')
# full_name.send_keys('Gideon Samian ')
# sleep(3)


# for first login add a cell phone
# phon_num = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[1]/div[2]/div/div[2]/div[2]/form/div[2]/div/div/div/label/input')
# phon_num.send_keys('528342715')
# sleep(4)


# for first login select I am agree option
# agree_to_register = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[1]/div[2]/div/div[2]/div[2]/form/div[3]/div')
# agree_to_register.click()
# sleep(2)


# for first login press enter to register
# press_to_register = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[1]/div[2]/div/div[2]/div[2]/form/button')
# press_to_register.click()
# sleep(2)


#B. Home Screen

# login to the site
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.get('https://buyme.co.il/')
sleep(5)


# Pick a price point 300-400 ש"ח
dropdowns = driver.find_elements(By.XPATH, '//div[@role="combobox"]')
sleep(2)
dropdowns[0].click()
sleep(2)
option = driver.find_element(By.XPATH, "//li[@value='4']")
option.click()


# Pick the area דרןם
sleep(3)
dropdowns[1].click()
sleep(2)
option_1 = driver.find_element(By.XPATH, "//li[@value='12']")
option_1.click()
sleep(2)


# Pick the category המתנות האהובות של 2025
dropdowns[2].click()
sleep(2)
option_1 = driver.find_element(By.XPATH, "//li[@value='541']")
option_1.click()
sleep(3)
url = driver.current_url
with open("urls.txt", "a") as file:
    file.write(url + "\n")
sleep(3)


# Press the search button
press_serch = driver.find_element(By.XPATH, '//*[@id="ember1347"]')
press_serch.click()
sleep(3)
url = driver.current_url
with open("urls.txt", "a") as file:
    file.write(url + "\n")
sleep(2)

# C.Choose business screen

# Pick a business
sleep(2)
press_business = driver.find_element(By.XPATH, '//*[@id="ember2177"]')
press_business.click()
sleep(2)
url = driver.current_url
with open("urls.txt", "a") as file:
    file.write(url + "\n")
sleep(2)


# Type a price
type_price = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[1]/div/div/div[2]/div/ul/li/div/div/div[2]/form/div[1]/label')
type_price.send_keys('350')
sleep(3)


# press chose
type_chose = driver.find_element(By.XPATH , '/html/body/div[4]/div/div[2]/div[1]/div/div/div[2]/div/ul/li/div/div/div[2]/form/div[2]/button/span' )
type_chose.click()
sleep(3)
url = driver.current_url
with open("urls.txt", "a") as file:
    file.write(url + "\n")
sleep(3)


# D. Sender & Receiver information screen

# Enter the receiver name
receiver_name = driver.find_element(By.XPATH, '//*[@id="ember2439"]')
sleep(2)
receiver_name.send_keys('Gideon S')
sleep(2)


# Enter a blessing
blessing = driver.find_element(By.XPATH, '//*[@id="ember2446"]')
blessing.send_keys('מזל טוב ליום הולדת שפע ברכות')
sleep(2)


# Upload a picture
picture = driver.find_element(By.XPATH, '//*[@id="ember2454"]')
picture.click()
sleep(3)
pyperclip.copy(r'C:\Users\97252\PycharmProjects\PythonProject4\Site_test\cat.png')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
sleep(3)


# Pick the event (Wedding/birthday)
dropdowns = driver.find_elements(By.XPATH, '//div[@role="combobox"]')
sleep(2)
dropdowns[0].click()
sleep(3)
option = driver.find_element(By.XPATH, "//li[@value='10']")
option.click()
sleep(3)


# Pick Email / SMS option
press_continue  = driver.find_element(By.XPATH, '//*[@id="ember2456"]')
press_continue.click()
sleep(3)
sms_icon = driver.find_element(By.CSS_SELECTOR, '.method-icon')
sms_icon.click()
sleep(3)
sms_input_field = driver.find_element(By.XPATH, '//*[@id="sms"]')
sms_input_field.send_keys('0528342715')
sleep(3)
url = driver.current_url
with open("urls.txt", "a") as file:
    file.write(url + "\n")
sleep(3)