import urllib.request
import os
from PIL import Image

output_dir = r"c:\Users\Asus\Downloads\uma\UMA-Enterprises\assets\generated-images"

downloads = [
    {
        "url": "https://upload.wikimedia.org/wikipedia/commons/e/ed/Researchers_from_NASA_and_JAXA_tested_a_scale_model_of_the_X-59_experimental_aircraft_in_a_supersonic_wind_tunnel_located_in_Chofu%2C_Japan.jpg",
        "target": "wind-tunnel-models.webp",
        "crop": (0.1, 0.1, 0.9, 0.9)
    },
    {
        "url": "https://upload.wikimedia.org/wikipedia/commons/8/8c/A350-900_full_flight_simulator_cockpit_VHHH.jpg",
        "target": "cockpit-simulator-shells.webp",
        "crop": (0.05, 0.1, 0.95, 0.95)
    },
    {
        "url": "https://upload.wikimedia.org/wikipedia/commons/4/4c/Navy-Radome.jpg",
        "target": "composite-radomes.webp",
        "crop": (0.1, 0.1, 0.9, 0.9)
    },
    {
        "url": "https://upload.wikimedia.org/wikipedia/commons/9/9e/5_Axis_Scanning_Coordinate_Measurement_Machine_%28CMM%29.png",
        "target": "quality-inspection.webp",
        "crop": (0.1, 0.05, 0.9, 0.95)
    },
    {
        "url": "https://upload.wikimedia.org/wikipedia/commons/c/cf/%22_13_Fiat-Chrysler_-_Safety_-_Body_Exterior_Carbon_Fiber_Composite_Roof_Assembly_SRT_Viper.jpg",
        "target": "automotive-components.webp",
        "crop": (0.1, 0.15, 0.9, 0.85)
    },
    {
        "url": "https://upload.wikimedia.org/wikipedia/commons/d/d1/CFTF_tour_%2817102789780%29.jpg",
        "target": "infrastructure-facility.webp",
        "crop": (0.05, 0.1, 0.95, 0.9)
    }
]

for d in downloads:
    dest = os.path.join(output_dir, d["target"])
    print(f"Downloading {d['target']}...")
    try:
        req = urllib.request.Request(d["url"], headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        temp_file = dest + ".temp"
        with urllib.request.urlopen(req, timeout=30) as resp, open(temp_file, "wb") as f:
            f.write(resp.read())
        
        with Image.open(temp_file) as im:
            im = im.convert("RGB")
            w, h = im.size
            crop_box = (int(w * d["crop"][0]), int(h * d["crop"][1]), int(w * d["crop"][2]), int(h * d["crop"][3]))
            im_cropped = im.crop(crop_box)
            # Resize maintaining 16:10 or 16:9 ratio
            im_resized = im_cropped.resize((1600, 1000), Image.Resampling.LANCZOS)
            im_resized.save(dest, "WEBP", quality=90)
        
        if os.path.exists(temp_file):
            os.remove(temp_file)
        print(f"Successfully processed {d['target']} ({os.path.getsize(dest)} bytes)")
    except Exception as e:
        print(f"Failed {d['target']}: {e}")
