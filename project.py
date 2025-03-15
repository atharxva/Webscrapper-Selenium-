from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

query = "laptop"
file = 0
for i in range(1, 3):  # Loops through the first two pages
    driver.get(f"https://www.amazon.com/s?k={query}&page={i}&crid=15EJEG7F4X83Z&sprefix=laptop%2Caps%2C375&ref=nb_sb_noss_1")
    elems = driver.find_elements(By.CLASS_NAME, "sg-col-inner")  # Find product elements using the class name
    for elem in elems:
        d = elem.get_attribute("outerHTML")  # Get the outer HTML of the product element
        with open(f"data/{query}_{file}.html", "w", encoding="utf-8") as f:
            f.write(d)  # Write the HTML of the product to a file
            file += 1  # Increment the file count
    sleep(5)  # Pause for 5 seconds before moving to the next page
    print(f"{len(elems)} items found")
driver.close()
