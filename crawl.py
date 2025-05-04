from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

# https://www.facebook.com/groups/miaigroup/posts/1775605586544039/

browser = webdriver.Chrome()

browser.get("http://facebook.com")

txtUser = browser.find_element(By.ID, "email")
txtUser.send_keys("lechianh04@gmail.com")

txtPass = browser.find_element(By.ID, "pass")
txtPass.send_keys("0857466551")

txtPass.send_keys(Keys.ENTER)

sleep(8)

browser.close()

print("success")
