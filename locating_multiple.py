from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

query = "laptop"
for i in range(1,20):
    driver.get(f"https://www.amazon.com/s?k={query}&page={i}&crid=15EJEG7F4X83Z&sprefix=laptop%2Caps%2C375&ref=nb_sb_noss_1")
    elems = driver.find_elements(By.CLASS_NAME, "s-main-slot .s-result-item")
    for elem in elems:
        print(elem.text)
        print("---------------------------------------------------")
    sleep(5)
    print(f"{len(elems)} items found")
driver.close()
