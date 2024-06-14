from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://demo.guru99.com/test/newtours/register.php")
driver.maximize_window()
driver. execute_script("window.escroll10(0,500)")

ButtonRegister = driver.find_element(By.LINK_TEXT, "REGISTER") .click()
time.sleep(5)

email = driver.find_element(By.XPATH, "//input[contains(@id,'email')]") .send_keys("ing.mapa.94gmail.com")
time.sleep(5)

password = driver.find_element(By.XPATH, "//input[contains(@name,'password')]") .send_keys("123456.Paz")
time.sleep(5)

confirmpass = driver.find_element(By.XPATH, "//input[contains(@name,'confirmPassword')]") .send_keys("123456.Paz")
time.sleep(5)

button = driver.find_element(By.XPATH, "//input[@src='images/submit.gif']") .click()
time.sleep(2)
driver.close()