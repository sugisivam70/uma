import os
from PIL import Image, ImageEnhance, ImageOps

src_dir = r'C:/Users/Asus/Downloads/uma/assets'
dest_base = r'C:/Users/Asus/Downloads/uma/UMA-Enterprises/assets'
extra = {
    'page2_img1.jpeg': 'infrastructure/facility-hero.webp',
    'page3_img1.jpeg': 'infrastructure/composite-bay.webp',
    'page4_img1.jpeg': 'infrastructure/fabrication-floor.webp',
    'page60_img1.jpeg': 'projects/aewc-drdo-display.webp',
    'page75_img1.jpeg': 'components/wind-tunnel-blade-detail.webp',
    'page81_img1.jpeg': 'projects/a330-awacs-model.webp',
    'page106_img2.jpeg': 'projects/c295-mmma.webp',
    'page115_img2.jpeg': 'projects/tejas-lsp7-cockpit.webp',
}
for s_name, rel in extra.items():
    s = os.path.join(src_dir, s_name)
    d = os.path.join(dest_base, rel)
    if os.path.exists(s):
        os.makedirs(os.path.dirname(d), exist_ok=True)
        with Image.open(s) as img:
            img = ImageOps.exif_transpose(img).convert('RGB')
            img = ImageEnhance.Contrast(img).enhance(1.06)
            img = ImageEnhance.Sharpness(img).enhance(1.12)
            w, h = img.size
            if max(w, h) > 1400:
                sc = 1400 / max(w, h)
                img = img.resize((int(w * sc), int(h * sc)), Image.Resampling.LANCZOS)
            img.save(d, 'WEBP', quality=86, method=6)
print('Extra WebP images saved.')
