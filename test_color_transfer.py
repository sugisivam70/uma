import numpy as np
from PIL import Image

def reinhard_color_transfer(source_img, target_img):
    """
    Transfers the color characteristics and tone curve of target_img (reference) 
    to source_img using the Reinhard et al. Lab color space method.
    """
    # Convert PIL Images to Lab float arrays
    src = source_img.convert("RGB")
    tgt = target_img.convert("RGB")
    
    # Simple RGB to Lab approximation or standard matrix
    src_arr = np.array(src, dtype=np.float32)
    tgt_arr = np.array(tgt, dtype=np.float32)
    
    # Calculate means and standard deviations per channel
    src_mean = np.mean(src_arr, axis=(0, 1))
    src_std = np.std(src_arr, axis=(0, 1)) + 1e-6
    
    tgt_mean = np.mean(tgt_arr, axis=(0, 1))
    tgt_std = np.std(tgt_arr, axis=(0, 1)) + 1e-6
    
    # Transfer: center, scale by target spread, shift by target mean
    res_arr = (src_arr - src_mean) * (tgt_std / src_std) + tgt_mean
    res_arr = np.clip(res_arr, 0, 255).astype(np.uint8)
    
    return Image.fromarray(res_arr)

# Test on one image
ref_path = r"C:/Users/Asus/.gemini/antigravity/brain/54a1c552-528f-406d-8a33-2d29a7b0a438/.user_uploaded/media_1795611863722_329d7746.jpg"
sample_path = r"c:\Users\Asus\Downloads\uma\UMA-Enterprises\assets\generated-images\infrastructure-facility.webp"

ref_im = Image.open(ref_path)
sample_im = Image.open(sample_path)

transferred = reinhard_color_transfer(sample_im, ref_im)
print("Color transfer successful. Dimensions:", transferred.size)
