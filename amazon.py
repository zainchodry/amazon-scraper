from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time
import random



options = Options()
options.add_argument("--headless")  
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                     "AppleWebKit/537.36 (KHTML, like Gecko) "
                     "Chrome/120.0.0.0 Safari/537.36")


driver = webdriver.Chrome(options=options)


url = "https://www.amazon.com/s?k=airpods"

print("Opening Amazon...")
driver.get(url)


time.sleep(random.uniform(3, 5))


soup = BeautifulSoup(driver.page_source, "html.parser")


driver.quit()


data = {
    "brand": [],
    "rating": [],
    "information": [],
    "price": []
}


products = soup.select("div.s-main-slot div.s-result-item")

print("Scraping products...")
for product in products:
    
    title_tag = product.select_one("h2 span")
    if not title_tag:
        continue  
    information = title_tag.get_text(strip=True)

    
    brand_tag = product.select_one("span.a-size-base-plus")
    brand = brand_tag.get_text(strip=True) if brand_tag else "Unknown"

    
    rating_tag = product.select_one("i span.a-icon-alt")
    rating = rating_tag.get_text(strip=True) if rating_tag else "No rating"

    
    price_whole = product.select_one("span.a-price-whole")
    price_fraction = product.select_one("span.a-price-fraction")
    if price_whole and price_fraction:
        price = f"${price_whole.get_text(strip=True)}.{price_fraction.get_text(strip=True)}"
    else:
        price = "Price not available"

    
    data["brand"].append(brand)
    data["rating"].append(rating)
    data["information"].append(information)
    data["price"].append(price)

    
    print("Brand:", brand)
    print("Rating:", rating)
    print("Info:", information)
    print("Price:", price)
    print("-" * 50)


df = pd.DataFrame(data)
df.to_csv("Amazon.csv", index=False)
df.to_excel("Amazon.xlsx", index=False)

print("✅ Scraping Completed Successfully. Data saved in Amazon.csv and Amazon.xlsx.")
