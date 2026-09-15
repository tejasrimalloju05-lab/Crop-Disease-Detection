import os
from collections import defaultdict
from PIL import Image

DATASET_DIR = "clean_dataset"

counts = defaultdict(int)
total = 0
corrupted = 0

for root, _, files in os.walk(DATASET_DIR):
    for file in files:
        if file.lower().endswith((".jpg", ".jpeg", ".png")):
            path = os.path.join(root, file)

            try:
                with Image.open(path) as img:
                    img.verify()

                parts = os.path.normpath(path).split(os.sep)

                crop = parts[-3]
                category = parts[-2]

                counts[(crop, category)] += 1
                total += 1

            except:
                corrupted += 1

print("\n========== CLEAN DATASET ==========")

crops = ["Citrus", "Potato", "Rice", "Tomato", "Wheat"]
classes = ["Diseased", "Healthy", "Symptomised"]

for crop in crops:
    print(f"\n{crop}")

    crop_total = 0

    for category in classes:
        count = counts[(crop, category)]
        crop_total += count
        print(f"  {category}: {count}")

    print(f"  Total: {crop_total}")

print("\n-----------------------------------")
print(f"Total valid images: {total}")
print(f"Corrupted images: {corrupted}")
print("===================================")