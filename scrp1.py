import requests
from bs4 import BeautifulSoup

import requests
from bs4 import BeautifulSoup

url = 'https://stackoverflow.com/questions/tagged/python'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Use class_='s-link'
links = soup.find_all('class', class_='s-link')

print("🔗 All s-link Titles and URLs:")
if not links:
    print("❌ No links found.")
else:
    for i, link in enumerate(links, 1):
        text = link.get_text(strip=True)
        href = link.get('href')
        full_url = 'https://stackoverflow.com' + href if href.startswith('/') else href
        print(f"{i}. {text}\n   🔗 {full_url}")


