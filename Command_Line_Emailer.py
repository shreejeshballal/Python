# Import the necessary modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


# Variable
fromEmail = "name.cs20@sahyadri.edu.in"                # Variable stores Email
password = "*******"                               # Variable stores password
# Variable stores Recipient's email
to_email = ['example123@gmail.com', 'example@']
emailSubject = "Your_Subject"
mainMessage = "This is a test email sent using Selenium and Python."


# Set up the new driver for chrome
newDriver = webdriver.Chrome()

# Open Gmail using get method
newDriver.get('https://gmail.com')
newDriver.maximize_window()

time.sleep(2)
username = newDriver.find_element("id", "identifierId")
username.send_keys(fromEmail)
username.send_keys(Keys.ENTER)

time.sleep(5)
userPassword = newDriver.find_element('name', 'Passwd')
userPassword.send_keys(password)
userPassword.send_keys(Keys.ENTER)

newDriver.implicitly_wait(10)
time.sleep(5)

print("Page Running...")

for i in to_email:

    # Click on "compose" button to create a new email

    compose = newDriver.find_element(
        By.CSS_SELECTOR, 'div[class="T-I T-I-KE L3"]')
    compose.click()

    time.sleep(3)
    toInput = newDriver.find_element(By.CSS_SELECTOR, 'input[class="agP aFw"]')
    toInput.send_keys(i)
    time.sleep(2)
    subjectInput = newDriver.find_element(
        By.CSS_SELECTOR, 'input[class="aoT"]')
    subjectInput.send_keys(emailSubject)
    time.sleep(2)
    bodyInput = newDriver.find_element(
        By.CSS_SELECTOR, 'div[class="Am Al editable LW-avf tS-tW"]')
    bodyInput.send_keys(mainMessage)
    time.sleep(2)
    sendBtn = newDriver.find_element(
        By.CSS_SELECTOR, 'div[class="T-I J-J5-Ji aoO v7 T-I-atl L3"]')
    sendBtn.click()

    time.sleep(4)

# Quit browser window

newDriver.quit()
