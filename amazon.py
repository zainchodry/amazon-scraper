from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

# Setup Chrome options
options = Options()
options.add_argument("--headless")  # Run in background
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                     "AppleWebKit/537.36 (KHTML, like Gecko) "
                     "Chrome/120.0.0.0 Safari/537.36")

# Initialize driver
driver = webdriver.Chrome(options=options)

# Target URL
url = "https://www.amazon.com/s?k=airpods"

print("Opening Amazon...")
driver.get(url)

# Random sleep to mimic human
time.sleep(random.uniform(3, 5))

# Parse page
soup = BeautifulSoup(driver.page_source, "html.parser")

# Close browser
driver.quit()

# Prepare storage
data = {
    "brand": [],
    "rating": [],
    "information": [],
    "price": []
}

# Find all product blocks
products = soup.select("div.s-main-slot div.s-result-item")

print("Scraping products...")
for product in products:
    # Information (title)
    title_tag = product.select_one("h2 span")
    if not title_tag:
        continue  # Skip non-product blocks
    information = title_tag.get_text(strip=True)

    # Brand
    brand_tag = product.select_one("span.a-size-base-plus")
    brand = brand_tag.get_text(strip=True) if brand_tag else "Unknown"

    # Rating
    rating_tag = product.select_one("i span.a-icon-alt")
    rating = rating_tag.get_text(strip=True) if rating_tag else "No rating"

    # Price
    price_whole = product.select_one("span.a-price-whole")
    price_fraction = product.select_one("span.a-price-fraction")
    if price_whole and price_fraction:
        price = f"${price_whole.get_text(strip=True)}.{price_fraction.get_text(strip=True)}"
    else:
        price = "Price not available"

    # Store data
    data["brand"].append(brand)
    data["rating"].append(rating)
    data["information"].append(information)
    data["price"].append(price)

    # Print
    print("Brand:", brand)
    print("Rating:", rating)
    print("Info:", information)
    print("Price:", price)
    print("-" * 50)

# Save to files
df = pd.DataFrame(data)
df.to_csv("Amazon.csv", index=False)
df.to_excel("Amazon.xlsx", index=False)

print("✅ Scraping Completed Successfully. Data saved in Amazon.csv and Amazon.xlsx.")
