from selenium import webdriver.com

driver = webdriver.Chrome()
driver.get("https://demoqa.com")

print(driver.title)
driver.close()