from PIL import Image
import os

def compress_image(input_path, output_path, target_size_kb):
    image = Image.open(input_path)
    
    quality = 95  # Start with high quality
    while True:
        image.save(output_path, "JPEG", quality=quality)
        if os.path.getsize(output_path) <= target_size_kb * 1024 or quality <= 10:
            break
        quality -= 5  # Reduce quality gradually

    print(f"Final size: {os.path.getsize(output_path) / 1024:.2f} KB")

# Example usage
input_image = "SA_SIGNATURE.jpg"
output_image = "output_compressed.jpg"
target_size_kb = 50 # Change this to your desired size (10-50 KB)

compress_image(input_image, output_image, target_size_kb)
