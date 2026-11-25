import os
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter

base_dir = r"c:\Users\Asus\Downloads\uma\UMA-Enterprises\assets\generated-images"
ref_path = r"C:/Users/Asus/.gemini/antigravity/brain/54a1c552-528f-406d-8a33-2d29a7b0a438/.user_uploaded/media_1795611863722_329d7746.jpg"

ref_img = Image.open(ref_path).convert("RGB")
ref_arr = np.array(ref_img, dtype=np.float32)
ref_mean = np.mean(ref_arr, axis=(0, 1))
ref_std = np.std(ref_arr, axis=(0, 1)) + 1e-6

def apply_ref_grading(img, strength=0.75):
    """Blends Reinhard color transfer from the reference image with original colors"""
    src_arr = np.array(img.convert("RGB"), dtype=np.float32)
    src_mean = np.mean(src_arr, axis=(0, 1))
    src_std = np.std(src_arr, axis=(0, 1)) + 1e-6
    
    graded_arr = (src_arr - src_mean) * (ref_std / src_std) + ref_mean
    graded_arr = np.clip(graded_arr, 0, 255)
    
    # Blend with original for natural look
    blended_arr = (1 - strength) * src_arr + strength * graded_arr
    blended_arr = np.clip(blended_arr, 0, 255).astype(np.uint8)
    
    res = Image.fromarray(blended_arr)
    # Slight contrast enhancement to match crisp reference image
    res = ImageEnhance.Contrast(res).enhance(1.08)
    res = ImageEnhance.Sharpness(res).enhance(1.15)
    return res

specs = {
    # 16:9 Hero
    "hero-aerospace-composite.webp": (1920, 1080),
    
    # 4:3 Manufacturing & Infrastructure
    "infrastructure-facility.webp": (1600, 1200),
    "composite-moulding-process.webp": (1600, 1200),
    "fiberglass-manufacturing.webp": (1600, 1200),
    "component-finishing.webp": (1600, 1200),
    "quality-inspection.webp": (1600, 1200),
    "about-timeline.webp": (1600, 1200),
    
    # 1:1 Individual Component Photography
    "wind-tunnel-models.webp": (1200, 1200),
    "cockpit-simulator-shells.webp": (1200, 1200),
    "composite-radomes.webp": (1200, 1200),
    "aerospace-components.webp": (1200, 1200),
    "automotive-components.webp": (1200, 1200),
    "industrial-enclosures.webp": (1200, 1200),
    "raw-composite-materials.webp": (1200, 1200),
    "custom-engineered-composites.webp": (1200, 1200)
}

for filename, (tw, th) in specs.items():
    p = os.path.join(base_dir, filename)
    if not os.path.exists(p):
        print(f"Skipping {filename}: not found")
        continue
    
    im = Image.open(p).convert("RGB")
    sw, sh = im.size
    
    # Center crop to target aspect ratio
    target_aspect = tw / th
    source_aspect = sw / sh
    
    if source_aspect > target_aspect:
        # Source is wider than target: crop width
        new_w = int(sh * target_aspect)
        offset = (sw - new_w) // 2
        crop_box = (offset, 0, offset + new_w, sh)
    else:
        # Source is taller than target: crop height
        new_h = int(sw / target_aspect)
        offset = (sh - new_h) // 2
        crop_box = (0, offset, sw, offset + new_h)
        
    cropped = im.crop(crop_box)
    resized = cropped.resize((tw, th), Image.Resampling.LANCZOS)
    
    # Apply reference photography color grading
    graded = apply_ref_grading(resized, strength=0.7)
    
    # Save optimized WebP
    graded.save(p, "WEBP", quality=92, method=6)
    print(f"Processed {filename} -> {tw}x{th} ({os.path.getsize(p)} bytes)")
