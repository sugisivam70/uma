import fitz, json, re, os, sys
pdf_path = r'C:/Users/Asus/Downloads/uma/unzipped/UMA ENTERPRISES - Profile_compressed.pdf'
output_path = r'C:/Users/Asus/Downloads/uma/UMA-Enterprises/assets/pdf_text.txt'

doc = fitz.open(pdf_path)
full_text = ''
for page in doc:
    full_text += page.get_text()
# Remove confidential sections containing the phrase "Details of Purchase Order"
clean_text = re.sub(r'(?s)Details of Purchase Order.*?(?=\n\n)', '', full_text)
# also drop any lines with purchase order numbers (simple heuristic: lines containing "PO" or "Purchase Order")
clean_lines = []
for line in clean_text.splitlines():
    if re.search(r'\bPO\b|Purchase Order', line, re.I):
        continue
    clean_lines.append(line)
clean_text = '\n'.join(clean_lines)
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(clean_text)
print(json.dumps({'status':'extracted','chars':len(clean_text)}, ensure_ascii=False))
