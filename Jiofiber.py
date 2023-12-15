from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

print('Provide few details of your fiber pannel: 192.168.29.1')
Fiber_usrnm = input('Type your fiber pannel Username : ')
fiber_pwd  =  input('Type your fiber pannel password : ')
sleep_time = time.sleep

driver = webdriver.Firefox()
driver.get("http://192.168.29.1")
elem = driver.find_element(By.NAME, 'users.username')
elem.send_keys(Fiber_usrnm)
elem = driver.find_element(By.NAME, 'users.password')
elem.send_keys(fiber_pwd)
elem.send_keys(Keys.RETURN)
sleep_time(2)

Administration = driver.find_element(By.ID, "mainMenu5")
Administration.send_keys(Keys.RETURN)
sleep_time(1)

Maintenance  = driver.find_element(By.ID, "tf1_administration_backupRestore")
Maintenance.send_keys(Keys.RETURN)
sleep_time(2)

Reboot = driver.find_element(By.NAME, "button.reboot.statusPage")
Reboot.send_keys(Keys.RETURN)
sleep_time(2)
alert = driver.switch_to.alert
alert.accept()
sleep_time(5)
driver.close()
print('Your Job completed')