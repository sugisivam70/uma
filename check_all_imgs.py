import os
import re

base = r"c:\Users\Asus\Downloads\uma\UMA-Enterprises"
for f in sorted(os.listdir(base)):
    if f.endswith(".html"):
        path = os.path.join(base, f)
        with open(path, "r", encoding="utf-8") as fl:
            content = fl.read()
        imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>', content)
        print(f"\n=== {f} ({len(imgs)} images) ===")
        for img in imgs:
            print("  ", img)
