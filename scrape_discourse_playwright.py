from playwright.sync_api import sync_playwright
import time

def scrape_after_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        # Open page
        page = context.new_page()
        page.goto("https://discourse.onlinedegree.iitm.ac.in/login")

        # ✅ Pause to manually log in
        print("🔐 Please log in manually, then press ENTER here to continue...")
        input(">> Waiting for manual login...")

        # ✅ Save storage state (cookies, localStorage) for reuse
        context.storage_state(path="auth.json")

        # Continue scraping here (e.g., navigate to topics list)
        page.goto("https://discourse.onlinedegree.iitm.ac.in/latest")
        print("✅ Logged in and on latest page.")

        # Example: take screenshot or start parsing posts
        page.screenshot(path="after_login.png")

        browser.close()

if __name__ == "__main__":
    scrape_after_login()
