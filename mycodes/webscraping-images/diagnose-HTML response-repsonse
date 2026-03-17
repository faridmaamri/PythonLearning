# this code is used to diagnose the code of the above function (get_images_url) to see why it does not return any url
def diagnose(keyword):
    query = quote(keyword)                              # Line 1
    url = (
        f"https://www.google.com/search?"
        f"q={query}&tbm=isch&start=0"
    )

    response = requests.get(url, headers=HEADERS)      # Line 2

    # ---- CHECK 1: Did Google respond? ----
    print(f"Status code: {response.status_code}")      # Line 3

    # ---- CHECK 2: Are we getting a CAPTCHA? ----
    if "captcha" in response.text.lower():             # Line 4
        print("❌ Google returned a CAPTCHA page!")
    else:
        print("✅ No CAPTCHA detected")

    # ---- CHECK 3: Save raw HTML to inspect it ----
    with open("debug_response.html", "w",              # Line 5
              encoding="utf-8") as f:
        f.write(response.text)
    print("📄 Raw HTML saved to debug_response.html")

    # ---- CHECK 4: Try different regex patterns ----
    patterns = {                                        # Line 6
        "Original"  : r'"(https?://[^"]+\.(?:jpg|jpeg|png|gif|webp))"',
        "Loose URL" : r'(https?://\S+\.(?:jpg|jpeg|png))',
        "Google encoded" : r'imgurl=(https?[^&]+)',
    }

    for name, pattern in patterns.items():             # Line 7
        found = re.findall(pattern, response.text)
        print(f"  Pattern '{name}': {len(found)} matches")
        if found:
            print(f"    👉 Sample: {found[0][:80]}")  # Line 8

# ---- RUN IT ----
diagnose(keyword)
