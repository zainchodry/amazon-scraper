# 🛍️ Amazon Web Scraper using Selenium & BeautifulSoup

This project is a Python-based Amazon web scraper that extracts product information such as brand, rating, title, and price for a specific search keyword (e.g., "airpods"). It uses **Selenium** to simulate a real browser and **BeautifulSoup** to parse the HTML.

---

## 🚀 Features

- Scrapes product details from Amazon search results
- Uses Selenium to bypass bot protection
- Exports data to both CSV and Excel formats
- Random delay to mimic human behavior
- Headless browser support

---

## 📦 Technologies Used

- Python 3.x
- [Selenium](https://pypi.org/project/selenium/)
- [BeautifulSoup (bs4)](https://pypi.org/project/beautifulsoup4/)
- [Pandas](https://pypi.org/project/pandas/)

---

## 📁 Project Structure

amazon-scraper/
├── scraper.py # Main scraping script
├── Amazon.csv # Output CSV file (auto-generated)
├── Amazon.xlsx # Output Excel file (auto-generated)
├── README.md # Project documentation
└── .gitignore # Files to ignore in Git



---

## 🧑‍💻 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/amazon-scraper.git
cd amazon-scraper


#Install Dependencies
pip freeze -r requirements.txt


#Run the Scraper
python3 amazon.py