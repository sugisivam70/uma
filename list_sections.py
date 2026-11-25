import os, re

base_dir = r"c:\Users\Asus\Downloads\uma\UMA-Enterprises"
pages = ["index.html", "about.html", "capabilities.html", "industries.html", "infrastructure.html", "projects.html", "contact.html"]

for page in pages:
    path = os.path.join(base_dir, page)
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
    print(f"\n==================== {page} ====================")
    # Find sections with titles and images
    sections = re.findall(r'<section[^>]*>(.*?)</section>', html, re.DOTALL)
    for s in sections:
        sec_id = re.search(r'id=["\']([^"\']+)["\']', s)
        heading = re.search(r'<h[1-3][^>]*>(.*?)</h[1-3]>', s, re.DOTALL)
        imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*alt=["\']([^"\']+)["\']', s)
        h_text = re.sub(r'<[^>]+>', '', heading.group(1)).strip() if heading else "No heading"
        s_id = sec_id.group(1) if sec_id else "No ID"
        print(f"Section: [{s_id}] - '{h_text}'")
        for src, alt in imgs:
            print(f"    -> Image: {src} | Alt: {alt}")
