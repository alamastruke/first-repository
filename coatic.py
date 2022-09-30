from selenium import webdriver
import time

driver = webdriver.Edge(r"msedgedriver.exe")
driver.get("https://redcoatic.com/login")

email ="alamastruke@gmail.com"
password= "Aa44453982"

time.sleep(3)

email_textfield = driver.find_element_by_name("alamastruke@gmail.com")
password_textfield = driver.find_element_by_name("Aa44453982")
login_button = driver.find_element_by_name("LoginDAPLoginForm")

email_textfield.send_keys(email)
time.sleep(2)
password_textfield.send_keys(password)
time.sleep(2)
login_button.click()