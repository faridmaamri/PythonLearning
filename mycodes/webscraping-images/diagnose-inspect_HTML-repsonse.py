# this code is used to diagnose the code of the above function (get_images_url) to see why it does not return any url
# this code must be run after running the fucntion  diagnose-HTML reponse-response.py
def inspect_html():
    with open("debug_response.html", "r",
              encoding="utf-8") as f:
        content = f.read()                              # Line 1

    # ---- CHECK 1: Look for gstatic (Google image CDN) ----
    gstatic = re.findall(                               # Line 2
        r'https://encrypted-tbn\d+\.gstatic\.com[^"\'\\]+',
        content
    )
    print(f"\n🔎 encrypted-tbn gstatic URLs: {len(gstatic)}")
    if gstatic:
        print(f"   Sample: {gstatic[0][:100]}")

    # ---- CHECK 2: Look for data inside JSON blobs ----
    json_imgs = re.findall(                             # Line 3
        r'\["(https?://[^"]+)",[0-9]+,[0-9]+\]',
        content
    )
    print(f"\n🔎 JSON blob image URLs: {len(json_imgs)}")
    if json_imgs:
        print(f"   Sample: {json_imgs[0][:100]}")

    # ---- CHECK 3: Look for base64 embedded images ----
    base64_imgs = re.findall(                           # Line 4
        r'data:image/[^;]+;base64,[^"\']{20,}',
        content
    )
    print(f"\n🔎 Base64 embedded images: {len(base64_imgs)}")

inspect_html()
