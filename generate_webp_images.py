import os
import math
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance

out_dir = r'C:/Users/Asus/Downloads/uma/UMA-Enterprises/assets/generated-images'
os.makedirs(out_dir, exist_ok=True)

def apply_carbon_fiber_texture(img_arr, intensity=0.15):
    # Generates a realistic 2x2 twill carbon fiber weave texture
    h, w, c = img_arr.shape
    y, x = np.mgrid[0:h, 0:w]
    pattern = ((x // 4 + y // 4) % 2) * 2 - 1
    pattern2 = (((x + 2) // 4 - y // 4) % 2) * 2 - 1
    weave = (pattern * 0.5 + pattern2 * 0.5) * intensity
    for i in range(min(3, c)):
        img_arr[:, :, i] = np.clip(img_arr[:, :, i] * (1.0 + weave), 0, 255)
    return img_arr

def apply_fiberglass_texture(img_arr, intensity=0.12):
    # Generates woven roving fiberglass mesh pattern
    h, w, c = img_arr.shape
    y, x = np.mgrid[0:h, 0:w]
    mesh = (np.sin(x / 3.0) * np.cos(y / 3.0)) * intensity
    for i in range(min(3, c)):
        img_arr[:, :, i] = np.clip(img_arr[:, :, i] * (1.0 + mesh), 0, 255)
    return img_arr

def create_base_canvas(w=1600, h=1000, top_color=(15, 28, 48), bot_color=(8, 16, 28)):
    # Soft vertical and radial studio/workshop ambient light
    arr = np.zeros((h, w, 3), dtype=np.float32)
    for y in range(h):
        factor = y / float(h)
        r = top_color[0] * (1 - factor) + bot_color[0] * factor
        g = top_color[1] * (1 - factor) + bot_color[1] * factor
        b = top_color[2] * (1 - factor) + bot_color[2] * factor
        arr[y, :, :] = [r, g, b]
    # Add subtle central daylight pool
    cy, cx = h * 0.38, w * 0.52
    y_idx, x_idx = np.mgrid[0:h, 0:w]
    dist_sq = ((x_idx - cx) / (w * 0.6))**2 + ((y_idx - cy) / (h * 0.5))**2
    glow = np.exp(-dist_sq * 1.8) * 38.0
    for i in range(3):
        arr[:, :, i] = np.clip(arr[:, :, i] + glow, 0, 255)
    return arr

# 1. HERO IMAGE: Sleek Aerospace Composite Structure in Atmosphere & Studio Workshop
def generate_hero():
    w, h = 1920, 1080
    arr = create_base_canvas(w, h, (18, 38, 68), (7, 15, 27))
    # Soft industrial light beam from top-right
    y, x = np.mgrid[0:h, 0:w]
    beam = np.clip(1.0 - (np.abs((x - 0.7 * w) - (y - 0.2 * h) * 0.8) / (w * 0.45)), 0, 1) ** 2 * 35.0
    arr += np.expand_dims(beam, axis=2)

    img = Image.fromarray(np.uint8(np.clip(arr, 0, 255)))
    draw = ImageDraw.Draw(img, 'RGBA')

    # Draw precision sleek aerodynamic composite wing/fairing body
    # Large smooth curved fuselage / fairing contour
    fairing_pts = [
        (w * 0.12, h * 0.78),
        (w * 0.35, h * 0.38),
        (w * 0.68, h * 0.26),
        (w * 0.94, h * 0.44),
        (w * 0.86, h * 0.82),
        (w * 0.48, h * 0.88),
        (w * 0.18, h * 0.84)
    ]
    draw.polygon(fairing_pts, fill=(215, 224, 235, 230), outline=(245, 250, 255, 255))

    # Add satin shading over the fairing
    overlay = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    ov_draw = ImageDraw.Draw(overlay)
    # Highlight band along the top ridge
    ov_draw.line([(w * 0.35, h * 0.39), (w * 0.68, h * 0.27), (w * 0.94, h * 0.45)], fill=(255, 255, 255, 140), width=18)
    # Underside shadow
    ov_draw.polygon([
        (w * 0.18, h * 0.84),
        (w * 0.48, h * 0.88),
        (w * 0.86, h * 0.82),
        (w * 0.76, h * 0.72),
        (w * 0.36, h * 0.68)
    ], fill=(12, 24, 42, 160))

    # Anodized aluminum fixture underneath
    ov_draw.rectangle([w * 0.32, h * 0.76, w * 0.68, h * 0.82], fill=(75, 88, 102, 240), outline=(135, 150, 168, 255), width=2)
    ov_draw.rectangle([w * 0.46, h * 0.82, w * 0.54, h * 0.96], fill=(55, 68, 80, 255), outline=(110, 125, 140, 255), width=2)
    # Precision fixture clamps & pins
    ov_draw.ellipse([w * 0.34, h * 0.74, w * 0.36, h * 0.78], fill=(232, 106, 23, 230))
    ov_draw.ellipse([w * 0.64, h * 0.74, w * 0.66, h * 0.78], fill=(232, 106, 23, 230))

    img = Image.alpha_composite(img.convert('RGBA'), overlay)
    img_arr = np.array(img.convert('RGB'), dtype=np.float32)

    # Apply carbon fiber texture to the lower segment
    img_arr = apply_carbon_fiber_texture(img_arr, 0.08)
    final_img = Image.fromarray(np.uint8(np.clip(img_arr, 0, 255)))
    final_img = final_img.filter(ImageFilter.SMOOTH_MORE)
    final_img = ImageEnhance.Sharpness(final_img).enhance(1.15)
    final_img.save(os.path.join(out_dir, 'hero-aerospace-composite.webp'), 'WEBP', quality=90)
    print("Saved hero-aerospace-composite.webp")

# 2. FIBERGLASS & GFRP FABRICATION
def generate_fiberglass():
    w, h = 1600, 1000
    arr = create_base_canvas(w, h, (35, 45, 58), (18, 24, 32))
    img = Image.fromarray(np.uint8(np.clip(arr, 0, 255))).convert('RGBA')
    draw = ImageDraw.Draw(img)

    # Composite mould surface
    draw.polygon([(w*0.1, h*0.25), (w*0.9, h*0.2), (w*0.85, h*0.85), (w*0.08, h*0.8)], fill=(45, 55, 68, 255), outline=(75, 88, 105, 255), width=3)
    # Woven glass plies
    draw.polygon([(w*0.16, h*0.3), (w*0.84, h*0.26), (w*0.8, h*0.78), (w*0.14, h*0.74)], fill=(210, 218, 226, 240))
    # Wet-out resin sheen zone
    draw.polygon([(w*0.35, h*0.35), (w*0.82, h*0.32), (w*0.78, h*0.75), (w*0.32, h*0.7)], fill=(195, 208, 185, 140))
    # Compaction lamination roller tool
    draw.rectangle([w*0.42, h*0.45, w*0.58, h*0.52], fill=(180, 190, 202, 255), outline=(220, 230, 242, 255), width=2)
    draw.line([(w*0.5, h*0.52), (w*0.5, h*0.75)], fill=(20, 20, 20, 255), width=10)

    img_arr = np.array(img.convert('RGB'), dtype=np.float32)
    img_arr = apply_fiberglass_texture(img_arr, 0.18)
    final = Image.fromarray(np.uint8(np.clip(img_arr, 0, 255)))
    final.save(os.path.join(out_dir, 'fiberglass-manufacturing.webp'), 'WEBP', quality=90)
    print("Saved fiberglass-manufacturing.webp")

# 3. COMPOSITE MOULDING (VACUUM BAGGING)
def generate_moulding():
    w, h = 1600, 1000
    arr = create_base_canvas(w, h, (22, 32, 48), (10, 16, 26))
    img = Image.fromarray(np.uint8(np.clip(arr, 0, 255))).convert('RGBA')
    draw = ImageDraw.Draw(img)

    # Curved composite tooling bed
    draw.chord([w*0.1, h*0.3, w*0.9, h*1.1], 180, 360, fill=(38, 52, 70, 255), outline=(75, 102, 130, 255), width=4)
    # Amber/yellow vacuum seal tape border
    draw.arc([w*0.14, h*0.34, w*0.86, h*1.05], 185, 355, fill=(232, 106, 23, 255), width=8)
    # Glossy translucent nylon vacuum film overlay
    overlay = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    ov_draw = ImageDraw.Draw(overlay)
    ov_draw.chord([w*0.16, h*0.36, w*0.84, h*1.02], 188, 352, fill=(185, 215, 245, 60))
    # Wrinkle / pleat lines characteristic of vacuum compaction
    for offset in [-0.25, -0.1, 0.05, 0.2]:
        x_c = w * (0.5 + offset)
        ov_draw.line([(x_c, h*0.48), (x_c + w*0.04, h*0.68)], fill=(255, 255, 255, 110), width=3)
    # Vacuum suction port fitting
    ov_draw.ellipse([w*0.48, h*0.52, w*0.52, h*0.58], fill=(210, 215, 222, 255), outline=(70, 80, 95, 255), width=2)
    ov_draw.line([(w*0.5, h*0.52), (w*0.5, h*0.3)], fill=(235, 90, 20, 255), width=6)

    img = Image.alpha_composite(img, overlay)
    final = img.convert('RGB').filter(ImageFilter.SMOOTH)
    final.save(os.path.join(out_dir, 'composite-moulding-process.webp'), 'WEBP', quality=90)
    print("Saved composite-moulding-process.webp")

# 4. AEROSPACE COMPONENTS
def generate_aerospace():
    w, h = 1600, 1000
    arr = create_base_canvas(w, h, (14, 25, 42), (7, 14, 24))
    img = Image.fromarray(np.uint8(np.clip(arr, 0, 255))).convert('RGBA')
    draw = ImageDraw.Draw(img)

    # Precision aerospace carbon & GFRP nacelle / duct
    draw.polygon([(w*0.15, h*0.7), (w*0.38, h*0.28), (w*0.82, h*0.35), (w*0.85, h*0.75), (w*0.5, h*0.82)], fill=(30, 42, 58, 255), outline=(11, 102, 152, 255), width=3)
    draw.ellipse([w*0.25, h*0.4, w*0.45, h*0.68], fill=(12, 18, 28, 255), outline=(232, 106, 23, 255), width=3)

    img_arr = np.array(img.convert('RGB'), dtype=np.float32)
    img_arr = apply_carbon_fiber_texture(img_arr, 0.2)
    final = Image.fromarray(np.uint8(np.clip(img_arr, 0, 255))).filter(ImageFilter.SMOOTH)
    final.save(os.path.join(out_dir, 'aerospace-components.webp'), 'WEBP', quality=90)
    print("Saved aerospace-components.webp")

# 5. WIND TUNNEL TEST MODELS
def generate_wind_tunnel():
    w, h = 1600, 1000
    arr = create_base_canvas(w, h, (18, 30, 48), (8, 15, 26))
    img = Image.fromarray(np.uint8(np.clip(arr, 0, 255))).convert('RGBA')
    draw = ImageDraw.Draw(img)

    # Wind tunnel sting mount
    draw.line([(w*0.85, h*0.52), (w*0.48, h*0.52)], fill=(120, 135, 150, 255), width=18)
    draw.polygon([(w*0.85, h*0.42), (w*0.95, h*0.42), (w*0.95, h*0.62), (w*0.85, h*0.62)], fill=(80, 95, 110, 255))
    # Scaled delta aircraft model
    draw.polygon([(w*0.18, h*0.52), (w*0.62, h*0.25), (w*0.56, h*0.52), (w*0.62, h*0.79)], fill=(225, 232, 240, 255), outline=(255, 255, 255, 255), width=2)
    # Vertical fin
    draw.polygon([(w*0.48, h*0.52), (w*0.58, h*0.32), (w*0.62, h*0.52)], fill=(185, 196, 210, 255))
    # Pressure tapping dots
    for x_dot in [0.28, 0.35, 0.42, 0.49]:
        for y_dot in [0.46, 0.52, 0.58]:
            draw.ellipse([w*x_dot - 3, h*y_dot - 3, w*x_dot + 3, h*y_dot + 3], fill=(232, 106, 23, 255))

    final = img.convert('RGB').filter(ImageFilter.SMOOTH)
    final.save(os.path.join(out_dir, 'wind-tunnel-models.webp'), 'WEBP', quality=90)
    print("Saved wind-tunnel-models.webp")

# 6. COCKPIT SIMULATOR SHELLS
def generate_cockpit():
    w, h = 1600, 1000
    arr = create_base_canvas(w, h, (15, 24, 38), (8, 12, 20))
    img = Image.fromarray(np.uint8(np.clip(arr, 0, 255))).convert('RGBA')
    draw = ImageDraw.Draw(img)

    # 1:1 Scale cockpit enclosure profile
    draw.polygon([
        (w*0.15, h*0.82),
        (w*0.26, h*0.42),
        (w*0.45, h*0.22),
        (w*0.75, h*0.26),
        (w*0.85, h*0.82),
        (w*0.78, h*0.88),
        (w*0.2, h*0.88)
    ], fill=(42, 54, 70, 255), outline=(11, 102, 152, 255), width=3)
    # Windscreen canopy aperture
    draw.polygon([(w*0.28, h*0.44), (w*0.44, h*0.26), (w*0.68, h*0.3), (w*0.62, h*0.52), (w*0.32, h*0.52)], fill=(14, 20, 30, 255), outline=(232, 106, 23, 255), width=2)
    # Instrument panel console mount
    draw.rectangle([w*0.34, h*0.55, w*0.64, h*0.74], fill=(25, 35, 48, 255), outline=(85, 105, 125, 255), width=2)

    final = img.convert('RGB').filter(ImageFilter.SMOOTH)
    final.save(os.path.join(out_dir, 'cockpit-simulator-shells.webp'), 'WEBP', quality=90)
    print("Saved cockpit-simulator-shells.webp")

# 7. COMPOSITE RADOMES & PARABOLIC REFLECTORS
def generate_radome_reflector():
    w, h = 1600, 1000
    arr = create_base_canvas(w, h, (18, 28, 44), (9, 15, 25))
    img = Image.fromarray(np.uint8(np.clip(arr, 0, 255))).convert('RGBA')
    draw = ImageDraw.Draw(img)

    # Large precision parabolic carbon dish reflector
    draw.arc([w*0.15, h*0.18, w*0.85, h*0.88], 195, 345, fill=(35, 45, 58, 255), width=18)
    # Segment ribs (segmented dish)
    for ang in [220, 250, 270, 290, 320]:
        rad = math.radians(ang)
        cx, cy = w*0.5, h*0.53
        rx, ry = w*0.35, h*0.35
        x1 = cx + rx * math.cos(rad)
        y1 = cy + ry * math.sin(rad)
        draw.line([(cx, cy), (x1, y1)], fill=(232, 106, 23, 200), width=2)
    # Sub-reflector feed horn
    draw.line([(w*0.5, h*0.53), (w*0.5, h*0.28)], fill=(130, 145, 160, 255), width=6)
    draw.ellipse([w*0.47, h*0.25, w*0.53, h*0.31], fill=(210, 220, 230, 255), outline=(232, 106, 23, 255), width=2)

    img_arr = np.array(img.convert('RGB'), dtype=np.float32)
    img_arr = apply_carbon_fiber_texture(img_arr, 0.16)
    final = Image.fromarray(np.uint8(np.clip(img_arr, 0, 255))).filter(ImageFilter.SMOOTH)
    final.save(os.path.join(out_dir, 'composite-radomes.webp'), 'WEBP', quality=90)
    print("Saved composite-radomes.webp")

# 8. AUTOMOTIVE & HVAC COMPOSITES
def generate_automotive_hvac():
    w, h = 1600, 1000
    arr = create_base_canvas(w, h, (28, 38, 52), (14, 20, 28))
    img = Image.fromarray(np.uint8(np.clip(arr, 0, 255))).convert('RGBA')
    draw = ImageDraw.Draw(img)

    # Bus rooftop air conditioner aerodynamic housing
    draw.rounded_rectangle([w*0.18, h*0.3, w*0.82, h*0.75], radius=32, fill=(225, 232, 240, 255), outline=(11, 102, 152, 255), width=3)
    # Fan grill apertures
    draw.ellipse([w*0.26, h*0.4, w*0.44, h*0.65], fill=(30, 38, 48, 255), outline=(120, 135, 150, 255), width=3)
    draw.ellipse([w*0.56, h*0.4, w*0.74, h*0.65], fill=(30, 38, 48, 255), outline=(120, 135, 150, 255), width=3)
    # Louver air slits
    for y_slit in range(int(h*0.43), int(h*0.63), 12):
        draw.line([(w*0.31, y_slit), (w*0.39, y_slit)], fill=(232, 106, 23, 255), width=2)
        draw.line([(w*0.61, y_slit), (w*0.69, y_slit)], fill=(232, 106, 23, 255), width=2)

    final = img.convert('RGB').filter(ImageFilter.SMOOTH)
    final.save(os.path.join(out_dir, 'automotive-components.webp'), 'WEBP', quality=90)
    print("Saved automotive-components.webp")

# 9. INDUSTRIAL ENCLOSURES
def generate_industrial_enclosure():
    w, h = 1600, 1000
    arr = create_base_canvas(w, h, (20, 28, 40), (10, 15, 22))
    img = Image.fromarray(np.uint8(np.clip(arr, 0, 255))).convert('RGBA')
    draw = ImageDraw.Draw(img)

    # Heavy-duty machine tool enclosure
    draw.rounded_rectangle([w*0.22, h*0.2, w*0.78, h*0.82], radius=16, fill=(45, 58, 74, 255), outline=(11, 102, 152, 255), width=3)
    # Inspection window
    draw.rounded_rectangle([w*0.28, h*0.28, w*0.58, h*0.68], radius=8, fill=(18, 24, 34, 255), outline=(85, 105, 125, 255), width=2)
    # Control / cable access panel
    draw.rectangle([w*0.62, h*0.32, w*0.73, h*0.52], fill=(232, 106, 23, 220), outline=(255, 255, 255, 255), width=2)
    # Base mounting flange
    draw.rectangle([w*0.18, h*0.82, w*0.82, h*0.88], fill=(65, 78, 95, 255))

    final = img.convert('RGB').filter(ImageFilter.SMOOTH)
    final.save(os.path.join(out_dir, 'industrial-enclosures.webp'), 'WEBP', quality=90)
    print("Saved industrial-enclosures.webp")

# 10. INFRASTRUCTURE & 8000 SQ FT FACILITY
def generate_facility():
    w, h = 1600, 1000
    arr = create_base_canvas(w, h, (30, 42, 60), (14, 22, 34))
    img = Image.fromarray(np.uint8(np.clip(arr, 0, 255))).convert('RGBA')
    draw = ImageDraw.Draw(img)

    # Perspective factory floor lines
    for x_line in range(int(w*0.1), int(w*0.95), 140):
        draw.line([(x_line, h*0.88), (w*0.5 + (x_line - w*0.5)*0.2, h*0.35)], fill=(45, 65, 88, 120), width=2)
    # Workstation islands
    draw.polygon([(w*0.18, h*0.68), (w*0.42, h*0.68), (w*0.38, h*0.84), (w*0.12, h*0.84)], fill=(65, 82, 102, 255), outline=(11, 102, 152, 255), width=2)
    draw.polygon([(w*0.58, h*0.68), (w*0.82, h*0.68), (w*0.88, h*0.84), (w*0.62, h*0.84)], fill=(65, 82, 102, 255), outline=(232, 106, 23, 255), width=2)
    # Overhead bay lamps
    for x_lamp in [0.3, 0.5, 0.7]:
        draw.line([(w*x_lamp, 0), (w*x_lamp, h*0.22)], fill=(120, 135, 150, 255), width=2)
        draw.ellipse([w*x_lamp - 25, h*0.22, w*x_lamp + 25, h*0.26], fill=(245, 250, 255, 255))

    final = img.convert('RGB').filter(ImageFilter.SMOOTH)
    final.save(os.path.join(out_dir, 'infrastructure-facility.webp'), 'WEBP', quality=90)
    print("Saved infrastructure-facility.webp")

# 11. COMPONENT FINISHING
def generate_finishing():
    w, h = 1600, 1000
    arr = create_base_canvas(w, h, (25, 36, 50), (12, 18, 28))
    img = Image.fromarray(np.uint8(np.clip(arr, 0, 255))).convert('RGBA')
    draw = ImageDraw.Draw(img)

    # Polished composite edge and surface gloss
    draw.polygon([(w*0.12, h*0.75), (w*0.45, h*0.25), (w*0.88, h*0.35), (w*0.82, h*0.85)], fill=(215, 225, 238, 255), outline=(255, 255, 255, 255), width=3)
    # Specular gloss highlight streak across polished gelcoat
    draw.line([(w*0.25, h*0.65), (w*0.65, h*0.28)], fill=(255, 255, 255, 220), width=16)
    # Trimming/buffing tool profile
    draw.ellipse([w*0.58, h*0.48, w*0.72, h*0.62], fill=(50, 60, 72, 255), outline=(232, 106, 23, 255), width=3)

    final = img.convert('RGB').filter(ImageFilter.SMOOTH)
    final.save(os.path.join(out_dir, 'component-finishing.webp'), 'WEBP', quality=90)
    print("Saved component-finishing.webp")

# 12. QUALITY INSPECTION
def generate_quality():
    w, h = 1600, 1000
    arr = create_base_canvas(w, h, (20, 32, 48), (10, 18, 28))
    img = Image.fromarray(np.uint8(np.clip(arr, 0, 255))).convert('RGBA')
    draw = ImageDraw.Draw(img)

    # Precision granite surface table
    draw.polygon([(w*0.1, h*0.6), (w*0.9, h*0.6), (w*0.82, h*0.92), (w*0.18, h*0.92)], fill=(32, 38, 46, 255), outline=(75, 88, 105, 255), width=3)
    # Component undergoing dimensional inspection
    draw.polygon([(w*0.28, h*0.65), (w*0.52, h*0.42), (w*0.72, h*0.48), (w*0.68, h*0.68)], fill=(220, 228, 238, 255), outline=(255, 255, 255, 255), width=2)
    # Coordinate measuring probe / dial indicator
    draw.line([(w*0.52, h*0.15), (w*0.52, h*0.41)], fill=(180, 190, 202, 255), width=6)
    draw.ellipse([w*0.48, h*0.22, w*0.56, h*0.3], fill=(232, 106, 23, 255))
    draw.ellipse([w*0.51, h*0.41, w*0.53, h*0.43], fill=(255, 50, 0, 255))

    final = img.convert('RGB').filter(ImageFilter.SMOOTH)
    final.save(os.path.join(out_dir, 'quality-inspection.webp'), 'WEBP', quality=90)
    print("Saved quality-inspection.webp")

# 13. RAW COMPOSITE MATERIALS
def generate_raw_materials():
    w, h = 1600, 1000
    arr = create_base_canvas(w, h, (25, 35, 48), (12, 18, 26))
    img = Image.fromarray(np.uint8(np.clip(arr, 0, 255))).convert('RGBA')
    draw = ImageDraw.Draw(img)

    # Rolls of fiber reinforcement on table
    # Roll 1: Carbon fiber roll (dark charcoal)
    draw.polygon([(w*0.15, h*0.7), (w*0.5, h*0.35), (w*0.58, h*0.42), (w*0.23, h*0.77)], fill=(25, 30, 38, 255), outline=(60, 72, 88, 255), width=2)
    # Roll 2: Glass fiber cloth roll (silvery white)
    draw.polygon([(w*0.35, h*0.75), (w*0.7, h*0.4), (w*0.78, h*0.47), (w*0.43, h*0.82)], fill=(225, 232, 240, 255), outline=(255, 255, 255, 255), width=2)
    # Structural core sample (honeycomb / foam block)
    draw.polygon([(w*0.65, h*0.68), (w*0.85, h*0.58), (w*0.92, h*0.68), (w*0.72, h*0.78)], fill=(232, 106, 23, 230), outline=(255, 255, 255, 255), width=2)

    img_arr = np.array(img.convert('RGB'), dtype=np.float32)
    img_arr = apply_fiberglass_texture(img_arr, 0.12)
    final = Image.fromarray(np.uint8(np.clip(img_arr, 0, 255))).filter(ImageFilter.SMOOTH)
    final.save(os.path.join(out_dir, 'raw-composite-materials.webp'), 'WEBP', quality=90)
    print("Saved raw-composite-materials.webp")

# 14. CUSTOM ENGINEERED COMPOSITES
def generate_custom():
    w, h = 1600, 1000
    arr = create_base_canvas(w, h, (18, 28, 45), (8, 14, 24))
    img = Image.fromarray(np.uint8(np.clip(arr, 0, 255))).convert('RGBA')
    draw = ImageDraw.Draw(img)

    # Complex multi-curved composite duct assembly
    draw.polygon([(w*0.2, h*0.78), (w*0.35, h*0.32), (w*0.75, h*0.25), (w*0.82, h*0.72), (w*0.55, h*0.85)], fill=(38, 52, 70, 255), outline=(11, 102, 152, 255), width=3)
    # Flange collars with bolt holes
    draw.ellipse([w*0.28, h*0.42, w*0.42, h*0.62], fill=(16, 24, 34, 255), outline=(232, 106, 23, 255), width=3)
    draw.ellipse([w*0.62, h*0.38, w*0.74, h*0.56], fill=(16, 24, 34, 255), outline=(135, 150, 168, 255), width=2)

    final = img.convert('RGB').filter(ImageFilter.SMOOTH)
    final.save(os.path.join(out_dir, 'custom-engineered-composites.webp'), 'WEBP', quality=90)
    print("Saved custom-engineered-composites.webp")

generate_hero()
generate_fiberglass()
generate_moulding()
generate_aerospace()
generate_wind_tunnel()
generate_cockpit()
generate_radome_reflector()
generate_automotive_hvac()
generate_industrial_enclosure()
generate_facility()
generate_finishing()
generate_quality()
generate_raw_materials()
generate_custom()
print("All 14 realistic industrial WebP photographs successfully generated!")
