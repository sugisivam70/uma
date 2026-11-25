import urllib.request
import os
import time
from PIL import Image

output_dir = r"c:\Users\Asus\Downloads\uma\UMA-Enterprises\assets\generated-images"

targets = [
    {
        "filename": "about-timeline.webp",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Fraunhofer_-_Dresden_-_FEP_-_IFAM_-_IKTS_-_IWS.jpg/1280px-Fraunhofer_-_Dresden_-_FEP_-_IFAM_-_IKTS_-_IWS.jpg"
    },
    {
        "filename": "industrial-enclosures.webp",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Industrieweg-West_outdoor_electrical_enclosure%2C_Oude_Pekela_%282020%29_04.jpg/1280px-Industrieweg-West_outdoor_electrical_enclosure%2C_Oude_Pekela_%282020%29_04.jpg"
    }
]

for t in targets:
    dest = os.path.join(output_dir, t["filename"])
    print(f"Fetching {t['filename']}...")
    time.sleep(3)
    try:
        req = urllib.request.Request(
            t["url"], 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
        )
        temp = dest + ".temp"
        with urllib.request.urlopen(req, timeout=20) as resp, open(temp, "wb") as f:
            f.write(resp.read())
        
        with Image.open(temp) as im:
            im = im.convert("RGB")
            im_resized = im.resize((1600, 1000), Image.Resampling.LANCZOS)
            im_resized.save(dest, "WEBP", quality=90)
        
        if os.path.exists(temp):
            os.remove(temp)
        print(f"Success: {t['filename']} ({os.path.getsize(dest)} bytes)")
    except Exception as e:
        print(f"Error {t['filename']}: {e}")
