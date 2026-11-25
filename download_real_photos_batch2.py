import urllib.request
import os
import time
from PIL import Image, ImageEnhance, ImageFilter

output_dir = r"c:\Users\Asus\Downloads\uma\UMA-Enterprises\assets\generated-images"

downloads = [
    {
        "url": "https://upload.wikimedia.org/wikipedia/commons/9/9e/5_Axis_Scanning_Coordinate_Measurement_Machine_%28CMM%29.png",
        "target": "quality-inspection.webp",
        "crop": (0.05, 0.05, 0.95, 0.95)
    },
    {
        "url": "https://upload.wikimedia.org/wikipedia/commons/c/cf/%22_13_Fiat-Chrysler_-_Safety_-_Body_Exterior_Carbon_Fiber_Composite_Roof_Assembly_SRT_Viper.jpg",
        "target": "automotive-components.webp",
        "crop": (0.05, 0.1, 0.95, 0.85)
    },
    {
        "url": "https://upload.wikimedia.org/wikipedia/commons/d/d1/CFTF_tour_%2817102789780%29.jpg",
        "target": "infrastructure-facility.webp",
        "crop": (0.05, 0.05, 0.95, 0.95)
    },
    {
        "url": "https://upload.wikimedia.org/wikipedia/commons/9/95/Kelly_Ayotte_Safran_Aerospace_Components_12110032_1005794079493391_7548560883654395141_o.jpg",
        "target": "hero-aerospace-composite.webp",
        "crop": (0.1, 0.15, 0.9, 0.85)
    },
    {
        "url": "https://upload.wikimedia.org/wikipedia/commons/e/e9/NASA%27s_Cleanroom_Receives_the_Webb_Mirrors_%288009332691%29.jpg",
        "target": "aerospace-components.webp",
        "crop": (0.05, 0.1, 0.95, 0.9)
    },
    {
        "url": "https://upload.wikimedia.org/wikipedia/commons/1/1a/Fraunhofer_-_Dresden_-_FEP_-_IFAM_-_IKTS_-_IWS.jpg",
        "target": "about-timeline.webp",
        "crop": (0.05, 0.1, 0.95, 0.85)
    }
]

for d in downloads:
    dest = os.path.join(output_dir, d["target"])
    print(f"Waiting 5s before downloading {d['target']}...")
    time.sleep(5)
    try:
        req = urllib.request.Request(
            d["url"], 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
        )
        temp_file = dest + ".temp"
        with urllib.request.urlopen(req, timeout=30) as resp, open(temp_file, "wb") as f:
            f.write(resp.read())
        
        with Image.open(temp_file) as im:
            im = im.convert("RGB")
            w, h = im.size
            crop_box = (int(w * d["crop"][0]), int(h * d["crop"][1]), int(w * d["crop"][2]), int(h * d["crop"][3]))
            im_cropped = im.crop(crop_box)
            # Resize to clean 1600x1000
            im_resized = im_cropped.resize((1600, 1000), Image.Resampling.LANCZOS)
            # Subtle minimal aesthetic grading: slightly cool, natural contrast
            enhancer = ImageEnhance.Contrast(im_resized)
            im_graded = enhancer.enhance(1.05)
            im_graded.save(dest, "WEBP", quality=90)
        
        if os.path.exists(temp_file):
            os.remove(temp_file)
        print(f"Successfully processed {d['target']} ({os.path.getsize(dest)} bytes)")
    except Exception as e:
        print(f"Failed {d['target']}: {e}")
