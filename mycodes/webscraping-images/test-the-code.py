 ---- TEST: just fetch URLs, don't download yet ----
print("🧪 Running validation test...\n")
test_urls = get_images_urls('teddy bear', max_images=5)

print(f"\n✅ Found {len(test_urls)} URLs")
for i, url in enumerate(test_urls):
    print(f"  [{i+1}] {url[:80]}")
