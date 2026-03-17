# Install the required modules: pip install request BeautifulSoup4
# imports the required libraries
import requests
from bs4 import BeautifulSoup
import os
import time
import re
from urllib.request import urlretrieve
from urllib.parse import quote
from pathlib import Path
import codecs

# Setting

keyword ="grizzly bears"
max_images = 50
save_folder = Path('/content/grizzly')
if  not save_folder.exists():
  save_folder.mkdir()
# ---- HEADERS (mimic a real browser) ----
HEADERS =  header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://duckduckgo.com/',
    "Connection": "keep-alive",
    'Sec-Ch-Ua': '"Not(A:Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Upgrade-Insecure-Requests': '1',}

# define function to serach for images and returm list of URLS
def get_images_urls(keyword, max_images):
    image_urls = []
    start = 0

    while len(image_urls) < max_images:

        # ---- Build URL ----
        query = quote(keyword)
        search_url = (
            f"https://www.google.com/search?"
            f"q={query}&tbm=isch&start={start}"
        )

        # ---- Fetch page ----
        response = requests.get(search_url, headers=HEADERS)

        # ---- Decode unicode escapes in raw HTML ----
        decoded = codecs.decode(                        # Line 2
            response.text, 'unicode_escape'
        )

        # ---- Extract using JSON blob pattern ----
        found = re.findall(                             # Line 3
            r'\["(https?://[^"]+)",[0-9]+,[0-9]+\]',
            decoded
        )

        # ---- Filter only real image URLs ----
        filtered = [                                    # Line 4
            url for url in found
            if not "gstatic.com" in url                # skip Google UI icons
            and not "google.com" in url                # skip Google assets
        ]

        if not filtered:                               # Line 5
            print("⚠️ No new images on this page. Stopping.")
            break

        # ---- Add unique URLs only ----
        before = len(image_urls)                       # Line 6
        for url in filtered:
            if url not in image_urls:
                image_urls.append(url)
                if len(image_urls) >= max_images:
                    break

        after = len(image_urls)                        # Line 7
        print(f"  🔎 Page start={start} → "
              f"+{after - before} new | "
              f"Total: {after}/{max_images}")

        if after == before:                            # Line 8
            print("⚠️ No new unique images found. Stopping.")
            break

        start += 20                                    # Line 9
        time.sleep(1.5)

    return image_urls
# define function that download images from url returned by get_images_urls()

def download_images(image_urls, folder):
    os.makedirs(folder, exist_ok=True)

    total      = len(image_urls)
    downloaded = 0
    skipped    = 0

    print(f"📦 Starting download of {total} images → '{folder}/'\n")

    for i, url in enumerate(image_urls):
        try:
            # Extract file extension safely
            ext      = url.split(".")[-1].split("?")[0][:4].lower()
            if ext not in ["jpg","jpeg","png","gif","webp"]: # Line A
                ext = "jpg"                                  # default fallback

            filename = os.path.join(folder, f"image_{i+1}.{ext}")

            urlretrieve(url, filename)
            downloaded += 1

            # Progress indicator every 10 images
            if downloaded % 10 == 0:                         # Line B
                print(f"  ✅ {downloaded}/{total} downloaded...")

        except Exception as e:
            skipped += 1
            print(f"  ❌ Skipped image {i+1}: {e}")

        time.sleep(0.3)                                      # polite delay

    # ---- Final Summary ----
    print(f"""
╔═════════════════════════════════════╗
║         DOWNLOAD COMPLETE           ║
╠═════════════════════════════════════╣
║  ✅ Downloaded : {downloaded:<17} ║
║  ❌ Skipped   : {skipped:<17}  ║
║  📁 Saved to  : {folder:<17}  ║
╚════════════════════════════════════╝
   """ )
