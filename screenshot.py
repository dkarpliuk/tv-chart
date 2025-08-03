import asyncio
from playwright.async_api import async_playwright
from datetime import datetime
import os
import json

with open("config.json") as f:
    config = json.load(f)

symbol = config.get("symbol")
interval = config.get("interval")
screenshot_width = config.get("screenshot_width")
screenshot_height = config.get("screenshot_height")

URL = f"https://dkarpliuk.github.io/tv-chart/chart.html?symbol={symbol}&interval={interval}"
OUTPUT_DIR = "screenshots"

async def take_screenshot():
    timestamp = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(OUTPUT_DIR, f"screenshot_{timestamp}.png")
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.set_viewport_size({"width": screenshot_width, "height": screenshot_height})
        await page.goto(URL)
        await page.wait_for_load_state("networkidle")
        await page.screenshot(path=filename)
        await browser.close()

    print(f"Screenshot saved: {filename}")

if __name__ == "__main__":
    asyncio.run(take_screenshot())
