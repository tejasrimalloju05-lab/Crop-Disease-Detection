from PIL import Image
import glob
import os

root = r"C:\Users\TEJASRI\Downloads\AI crop detection project\crop detection\dataset"

images = [
    f for f in glob.glob(root + r"\**\*", recursive=True)
    if os.path.isfile(f)
    and os.path.splitext(f)[1].lower() in [".jpg", ".jpeg", ".png"]
]

bad = []

for file in images:
    try:
        with Image.open(file) as img:
            img.verify()
    except Exception:
        bad.append(file)

print("Total images checked:", len(images))
print("Corrupted images:", len(bad))

if bad:
    print("\nCorrupted files:")
    for file in bad:
        print(file)
else:
    print("All images are valid.")