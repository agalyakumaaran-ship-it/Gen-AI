
from playwright.sync_api import sync_playwright
from datetime import datetime

print("Starting the Playwright automation script...")
print(f"Script started at: {datetime.now()}")

# Daily Weather Report Bot
# Chromium -> Weather site -> Extract report -> Screenshot -> Final text

with sync_playwright() as p:
    browser = None

    try:
        print("Launching the Chromium browser...")
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        print("Navigating to the AccuWeather website...")
        page.goto(
            "https://www.accuweather.com/en/in/bengaluru/204108/weather-forecast/204108",
            wait_until="domcontentloaded",
            timeout=60000
        )

        # Allow the page content to load
        page.wait_for_timeout(5000)

        print("Taking a screenshot...")
        page.screenshot(path="accuweather.png", full_page=True)
        print("Screenshot saved as accuweather.png")

        print("Extracting the weather report...")

        # Print the page title
        print("Page title:", page.title())

        # Extract visible page text
        weather_report = page.locator("body").inner_text()

        print("\nWeather page content:")
        print(weather_report[:3000])

    except Exception as e:
        print("An error occurred:", e)

    finally:
        print("Closing the browser...")
        if browser is not None:
            browser.close()

print(f"Script completed at: {datetime.now()}")