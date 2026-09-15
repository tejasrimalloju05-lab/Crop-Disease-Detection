from PIL import Image
import os
from collections import Counter

DATASET_DIR = "dataset"

valid_extensions = {".jpg", ".jpeg", ".png"}

total = 0
corrupted = 0
small_files = []
dimensions = Counter()
formats = Counter()

print("=" * 60)
print("DATASET ANALYSIS")
print("=" * 60)

for root, _, files in os.walk(DATASET_DIR):

    for file in files:
        ext = os.path.splitext(file)[1].lower()

        if ext not in valid_extensions:
            continue

        total += 1
        path = os.path.join(root, file)

        try:
            file_size = os.path.getsize(path)

            with Image.open(path) as img:
                width, height = img.size
                dimensions[(width, height)] += 1
                formats[ext] += 1

            # Flag extremely small files
            if file_size < 10 * 1024:
                small_files.append((path, file_size, width, height))

        except Exception:
            corrupted += 1

print("\nTotal valid image files:", total)
print("Corrupted/unreadable:", corrupted)

print("\nImage formats:")
for fmt, count in formats.items():
    print(f"{fmt}: {count}")

print("\nMost common image dimensions:")
for size, count in dimensions.most_common(20):
    print(f"{size}: {count}")

print("\nVery small images (<10 KB):", len(small_files))

if small_files:
    print("\nSmall image files:")
    for path, size, width, height in small_files:
        print(f"{size} bytes | {width}x{height} | {path}")

print("\n" + "=" * 60)
print("ANALYSIS COMPLETE")
print("=" * 60)