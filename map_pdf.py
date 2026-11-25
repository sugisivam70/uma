import fitz, json

pdf_path = r'C:/Users/Asus/Downloads/uma/unzipped/UMA ENTERPRISES - Profile_compressed.pdf'
doc = fitz.open(pdf_path)

# Map pages to their text headings to understand what images are on which pages
pages_summary = []
for i in range(len(doc)):
    page = doc.load_page(i)
    txt = page.get_text("text").strip()
    imgs = len(page.get_images(full=True))
    first_lines = " | ".join([l.strip() for l in txt.splitlines() if l.strip()][:4])
    if imgs > 0 or first_lines:
        pages_summary.append({"page": i+1, "imgs": imgs, "text": first_lines[:180]})

with open(r'C:/Users/Asus/Downloads/uma/pdf_map.json', 'w', encoding='utf-8') as f:
    json.dump(pages_summary, f, indent=2, ensure_ascii=False)
print(f"Mapped {len(pages_summary)} pages")
