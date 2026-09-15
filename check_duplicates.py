import os
from PIL import Image
import hashlib

DATASET_DIR = "dataset"

def get_hash(image_path):
    try:
        with Image.open(image_path) as img:
            img = img.convert("RGB")
            img.thumbnail((32, 32))
            return hashlib.md5(img.tobytes()).hexdigest()
    except:
        return None

hashes = {}
duplicates = []

for root, _, files in os.walk(DATASET_DIR):
    for file in files:
        if file.lower().endswith((".jpg", ".jpeg", ".png")):
            path = os.path.join(root, file)
            image_hash = get_hash(path)

            if image_hash is None:
                continue

            if image_hash in hashes:
                duplicates.append((path, hashes[image_hash]))
            else:
                hashes[image_hash] = path

print("\n========== DUPLICATE CHECK ==========")
print(f"Total images checked: {len(hashes)}")
print(f"Duplicates found: {len(duplicates)}")

if duplicates:
    print("\nDuplicate images:")
    for duplicate, original in duplicates:
        print(f"\nDuplicate: {duplicate}")
        print(f"Same as : {original}")
else:
    print("\nNo duplicates found.")

print("\n======================================")