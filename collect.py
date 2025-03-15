from bs4 import BeautifulSoup
import os
import pandas as pd
import csv

d = {"title": [], "price": [], "link": []}  # Dictionary to store extracted data

# Loop through all files in the 'data' folder
for file in os.listdir("data"):
    with open(f"data/{file}") as f:
        html_doc = f.read()
    soup = BeautifulSoup(html_doc, 'html.parser')

    t = soup.find("h2")  # Find the title (assuming it's in an 'h2' tag)
    if t:
        title = t.get_text()  # Extract text from the 'h2' tag
        d["title"].append(title)
    else:
        d["title"].append("No Title Found")

    price = soup.find("span", class_="price")  # Example class name
    if price:
        d["price"].append(price.get_text())
    else:
        d["price"].append("No Price Found")

    link = soup.find("a", href=True)  # Find the first 'a' tag with an 'href' attribute
    if link:
        d["link"].append(link["href"])
    else:
        d["link"].append("No Link Found")

# Convert the extracted data into a pandas DataFrame
df = pd.DataFrame(d)

# Optionally save the data to a CSV file with improved formatting
df.to_csv("output.csv")

# Print the DataFrame to the console
print(df)
