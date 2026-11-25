import os, re

root = r'C:/Users/Asus/Downloads/uma/UMA-Enterprises'
html_files = sorted([f for f in os.listdir(root) if f.endswith('.html')])
missing = []
privacy_hits = []
banned = ['rlokre', '8317370398', '9448212168', 'Prakruthi', 'Anagalapura', '560077', 'PO No', 'GEMC-']

for hf in html_files:
    p = os.path.join(root, hf)
    with open(p, encoding='utf-8') as f:
        txt = f.read()
    for b in banned:
        if b.lower() in txt.lower():
            privacy_hits.append((hf, b))
    for attr in re.findall(r'(?:src|href)="([^"]+)"', txt):
        if attr.startswith(('http', 'mailto:', 'tel:', '#', 'data:')):
            continue
        target = os.path.join(root, attr.split('#')[0])
        if not os.path.exists(target):
            missing.append((hf, attr))

print('HTML files checked:', html_files)
print('Missing local refs:', missing)
print('Privacy hits:', privacy_hits)
