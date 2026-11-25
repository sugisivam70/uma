import fitz, os, json, sys
pdf_path = r'C:/Users/Asus/Downloads/uma/unzipped/UMA ENTERPRISES - Profile_compressed.pdf'
out_dir = r'C:/Users/Asus/Downloads/uma/assets'
os.makedirs(out_dir, exist_ok=True)

doc = fitz.open(pdf_path)
info = {
    'page_count': doc.page_count,
    'metadata': doc.metadata,
    'toc': doc.get_toc()
}
images = []
for page_num in range(doc.page_count):
    page = doc.load_page(page_num)
    img_list = page.get_images(full=True)
    for img_index, img in enumerate(img_list):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image['image']
        ext = base_image['ext']
        img_filename = f'page{page_num+1}_img{img_index+1}.{ext}'
        img_path = os.path.join(out_dir, img_filename)
        with open(img_path, 'wb') as f:
            f.write(image_bytes)
        images.append({'page': page_num+1, 'index': img_index+1, 'filename': img_filename, 'ext': ext})
print(json.dumps({'info': info, 'total_images': len(images), 'sample_images': images[:5]}, ensure_ascii=False))
