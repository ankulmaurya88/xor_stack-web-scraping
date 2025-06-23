from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# Set up headless Chrome
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')

# Start the browser and open the page
driver = webdriver.Chrome(options=options)
driver.get("https://stackoverflow.com/questions/tagged/python")

# Wait for page to load
time.sleep(5)

# Parse the page
soup = BeautifulSoup(driver.page_source, 'html.parser')
print(soup)
# Extract only question titles
titles = soup.select('h3.s-post-summary--content-title a')

print(titles)
# Print the questions
print(f"Found {len(titles)} questions.")
for title in titles:
    print(title.text.strip())

# Close the browser
driver.quit()
