import asyncio
from playwright.async_api import async_playwright
from datetime import datetime
import os

URL = "https://dkarpliuk.github.io/tv-chart/chart.html"

OUTPUT_DIR = "screenshots"

async def take_screenshot():
    timestamp = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(OUTPUT_DIR, f"screenshot_{timestamp}.png")
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(URL)
        page.wait_for_load_state("networkidle")
        await page.screenshot(path=filename, full_page=True)
        await browser.close()

    print(f"✅ Screenshot saved: {filename}")

if __name__ == "__main__":
    asyncio.run(take_screenshot())
