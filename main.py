from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
query = "laptop"
driver.get(f"https://www.amazon.com/s?k={query}&crid=15EJEG7F4X83Z&sprefix=laptop%2Caps%2C375&ref=nb_sb_noss_1")
elem = driver.find_element(By.CLASS_NAME, "puisg-row")
print(elem.get_attribute("outerHTML"))
sleep(5)
driver.close()