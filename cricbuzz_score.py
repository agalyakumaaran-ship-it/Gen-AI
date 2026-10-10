from playwright.sync_api import (
    sync_playwright,
    TimeoutError as PlaywrightTimeoutError
)
from datetime import datetime

print(f"Script started at: {datetime.now()}")

with sync_playwright() as p:
    print("Launching the browser...")

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    try:
        print("Navigating to Cricbuzz...")

        page.goto(
            "https://www.cricbuzz.com/cricket-match/live-scores",
            wait_until="domcontentloaded",
            timeout=60000
        )

        # Wait for the page body, not networkidle
        page.locator("body").wait_for(
            state="visible",
            timeout=15000
        )

        print("Cricbuzz page opened.")

        # Extract the visible page text
        page_text = page.locator("body").inner_text()

        print("\n========== CRICKET PAGE OUTPUT ==========")
        print(page_text[:8000])

        # Save a screenshot
        page.screenshot(
            path="cricbuzz_screenshot.png",
            full_page=True,
            timeout=30000
        )
        print("\nScreenshot saved as cricbuzz_screenshot.png")

    except PlaywrightTimeoutError as e:
        print(f"Playwright timed out: {e}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        browser.close()
        print(f"Script completed at: {datetime.now()}")
