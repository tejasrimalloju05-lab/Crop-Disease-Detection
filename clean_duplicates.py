import os
import shutil

DATASET_DIR = "dataset"
CLEAN_DIR = "clean_dataset"
REVIEW_DIR = "duplicate_review"

# Files to remove from the training copy:
# We keep the Diseased copy and quarantine the Symptomised duplicate.
remove_files = [
    r"Citrus\Symptomised\000002.jpg",

    r"Potato\Symptomised\000003.jpg",
    r"Potato\Symptomised\000006.jpg",
    r"Potato\Symptomised\000002.jpg",
    r"Potato\Symptomised\000019.jpg",
    r"Potato\Symptomised\000016.jpg",
    r"Potato\Symptomised\000001.jpg",

    r"Rice\Symptomised\000001.jpg",
    r"Rice\Symptomised\000003.jpg",
    r"Rice\Symptomised\000004.jpg",
    r"Rice\Symptomised\000010.jpg",
    r"Rice\Symptomised\000005.jpg",
    r"Rice\Symptomised\000007.jpg",
    r"Rice\Symptomised\000008.jpg",

    r"Tomato\Symptomised\000001.jpg",
    r"Tomato\Symptomised\000002.jpg",
    r"Tomato\Symptomised\000003.jpg",
    r"Tomato\Symptomised\000005.jpg",
    r"Tomato\Symptomised\000008.jpg",
    r"Tomato\Symptomised\000011.jpg",
    r"Tomato\Symptomised\000014.jpg",
    r"Tomato\Symptomised\000027.jpg",
    r"Tomato\Symptomised\000036.jpg",
    r"Tomato\Symptomised\000021.jpg",
    r"Tomato\Symptomised\000022.jpg",

    r"Wheat\Symptomised\000003.jpg",
    r"Wheat\Symptomised\000028.jpg",
    r"Wheat\Symptomised\000018.jpg",
    r"Wheat\Symptomised\000009.jpg",
    r"Wheat\Symptomised\000007.jpg",
    r"Wheat\Symptomised\000014.jpg",
]

# Special case:
# Potato Diseased 000032 and Tomato Symptomised 000015
# are duplicates but belong to different crops.
# We will quarantine the Tomato copy for manual review.
remove_files.append(r"Tomato\Symptomised\000015.jpg")

# Copy the complete original dataset first
if os.path.exists(CLEAN_DIR):
    print("clean_dataset already exists.")
    print("Delete it manually only if you want to recreate it.")
    exit()

shutil.copytree(DATASET_DIR, CLEAN_DIR)

print("Created clean_dataset copy.")

# Quarantine selected duplicate files
os.makedirs(REVIEW_DIR, exist_ok=True)

moved = 0

for relative_path in remove_files:
    source = os.path.join(CLEAN_DIR, relative_path)
    
    if os.path.exists(source):
        review_path = os.path.join(REVIEW_DIR, relative_path)
        os.makedirs(os.path.dirname(review_path), exist_ok=True)

        shutil.move(source, review_path)
        moved += 1
        print("Quarantined:", relative_path)
    else:
        print("NOT FOUND:", relative_path)

print("\n===================================")
print("Original dataset: UNTOUCHED")
print("Clean dataset created:", CLEAN_DIR)
print("Files quarantined:", moved)
print("Review folder:", REVIEW_DIR)
print("===================================")