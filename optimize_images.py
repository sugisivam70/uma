import os
from PIL import Image, ImageEnhance, ImageOps

src_dir = r'C:/Users/Asus/Downloads/uma/assets'
dest_base = r'C:/Users/Asus/Downloads/uma/UMA-Enterprises/assets'

mapping = {
    # Projects
    'page29_img1.jpeg': 'projects/uav-mockup.webp',
    'page65_img1.jpeg': 'projects/stealth-wing-mockup.webp',
    'page88_img1.jpeg': 'projects/aewc-aircraft-model.webp',
    'page100_img1.jpeg': 'projects/hansa-ng-model.webp',
    'page154_img1.jpeg': 'projects/aewc-mk2-model.webp',
    'page171_img1.jpeg': 'projects/c295-wind-tunnel.webp',
    'page121_img1.jpeg': 'projects/g280-simulator.webp',
    'page162_img1.jpeg': 'projects/gantry-dome-sulur.webp',
    'page164_img1.jpeg': 'projects/f10x-simulator.webp',
    'page165_img1.jpeg': 'projects/su30-cockpit.webp',
    'page169_img1.jpeg': 'projects/dome-9m.webp',
    'page142_img1.jpeg': 'projects/cfrp-reflector-segmented.webp',
    'page183_img1.jpeg': 'projects/kuband-reflector.webp',
    # Components
    'page43_img1.jpeg': 'components/wind-tunnel-vssc.webp',
    'page64_img1.jpeg': 'components/amca-wind-tunnel.webp',
    'page74_img1.jpeg': 'components/wind-tunnel-blade.webp',
    'page153_img1.jpeg': 'components/cats-wind-tunnel.webp',
    'page174_img1.jpeg': 'components/automotive-wind-tunnel.webp',
    'page40_img2.jpeg': 'components/cockpit-tejas.webp',
    'page50_img1.jpeg': 'components/saras-cockpit.webp',
    'page71_img1.jpeg': 'components/gulfstream-cockpit.webp',
    'page66_img1.jpeg': 'components/cfrp-reflector-600.webp',
    'page67_img1.jpeg': 'components/cfrp-reflector-4600.webp',
    'page83_img1.jpeg': 'components/awacs-dome.webp',
    'page144_img1.jpeg': 'components/blade-radome.webp',
    'page178_img1.jpeg': 'components/antenna-radome-enclosure.webp',
    'page35_img2.jpeg': 'components/hvac-rooftop-unit.webp',
    'page42_img1.jpeg': 'components/cnc-gfrp-enclosure.webp',
    'page49_img1.jpeg': 'components/wind-turbine-mould.webp',
    'page70_img1.jpeg': 'components/anechoic-cylinder.webp',
    'page159_img1.jpeg': 'components/truck-ac-cover.webp',
    # Infrastructure
    'page141_img1.jpeg': 'infrastructure/simulator-dome-6m.webp',
}

def optimize_image(src_path, dst_path, max_dim=1400):
    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
    with Image.open(src_path) as img:
        img = ImageOps.exif_transpose(img).convert('RGB')
        # Subtle industrial clarity enhancement
        img = ImageEnhance.Contrast(img).enhance(1.06)
        img = ImageEnhance.Sharpness(img).enhance(1.12)
        w, h = img.size
        if max(w, h) > max_dim:
            scale = max_dim / max(w, h)
            img = img.resize((int(w * scale), int(h * scale)), Image.Resampling.LANCZOS)
        img.save(dst_path, 'WEBP', quality=86, method=6)

count = 0
for src_name, rel_dst in mapping.items():
    s = os.path.join(src_dir, src_name)
    d = os.path.join(dest_base, rel_dst)
    if os.path.exists(s):
        optimize_image(s, d)
        count += 1

# Also create transparent PNG + favicon from logo.png
logo_src = os.path.join(dest_base, 'logo', 'logo.png')
if os.path.exists(logo_src):
    with Image.open(logo_src) as logo:
        logo = logo.convert('RGBA')
        datas = logo.getdata()
        new_data = []
        for item in datas:
            # Make near-white background transparent
            if item[0] > 240 and item[1] > 240 and item[2] > 240:
                new_data.append((255, 255, 255, 0))
            else:
                new_data.append(item)
        logo.putdata(new_data)
        # Trim transparent borders
        bbox = logo.getbbox()
        if bbox:
            logo = logo.crop(bbox)
        logo.save(os.path.join(dest_base, 'logo', 'logo-transparent.png'), 'PNG')
        fav = logo.resize((64, 64), Image.Resampling.LANCZOS)
        fav.save(os.path.join(dest_base, 'logo', 'favicon.png'), 'PNG')

print(f"Optimized {count} images and processed transparent logo + favicon.")
