from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time

def fetch_questions():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set to True if you don't want to see the browser
        page = browser.new_page()
        
        print("🔄 Opening Stack Overflow...")
        page.goto("https://stackoverflow.com/questions/tagged/python", timeout=60000)
        page.wait_for_load_state("networkidle")  # Wait for full load

        # Extra wait just in case
        time.sleep(5)

        # Log page title for confirmation
        print("📄 Page title:", page.title())

        # Parse the page
        html = page.content()
        soup = BeautifulSoup(html, "html.parser")

        # Correct selector: 'h3.s-post-summary--content-title > a'
        titles = soup.select("h3.s-post-summary--content-title > a")

        print("\n🔎 Extracted Questions:")
        if not titles:
            print("❌ No questions found. StackOverflow layout may have changed or blocked rendering.")
        else:
            for idx, a in enumerate(titles[:15], 1):
                print(f"{idx}. {a.text.strip()}")

        browser.close()

if __name__ == "__main__":
    fetch_questions()
