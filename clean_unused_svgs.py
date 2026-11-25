import os, re

base = r"c:\Users\Asus\Downloads\uma\UMA-Enterprises"
img_dir = os.path.join(base, "assets", "generated-images")

html_files = [os.path.join(base, f) for f in os.listdir(base) if f.endswith(".html")]
all_html = ""
for hf in html_files:
    with open(hf, "r", encoding="utf-8") as f:
        all_html += f.read()

svgs = [f for f in os.listdir(img_dir) if f.endswith(".svg")]
for s in svgs:
    count = all_html.count(s)
    print(f"{s}: referenced {count} times")
    if count == 0:
        os.remove(os.path.join(img_dir, s))
        print(f"  -> Deleted unused {s}")
