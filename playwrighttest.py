from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # make it visible
    page = browser.new_page()
    page.goto("https://discourse.onlinedegree.iitm.ac.in/")
    input("Press Enter after checking the page...")
    browser.close()
