from PIL import Image
import os

def preprocess_images_to_new_folder(input_dir, output_dir, size=(224, 224)):
    for root, _, files in os.walk(input_dir):
        # Create corresponding output path
        relative_path = os.path.relpath(root, input_dir)
        target_path = os.path.join(output_dir, relative_path)
        os.makedirs(target_path, exist_ok=True)

        for file in files:
            input_path = os.path.join(root, file)
            output_path = os.path.join(target_path, file)
            try:
                # Open the image and check if it can be processed
                img = Image.open(input_path).convert('RGB')
                
                # If it's a valid image, resize it
                img = img.resize(size)
                
                # Save it to the new folder
                img.save(output_path)
                
                # Log success
                print(f"✅ Processed and saved: {input_path}")
            
            except (OSError, IOError) as e:
                # Log corrupted images
                print(f"⚠️ Skipped corrupted image: {input_path}")
                # Optional: Remove the corrupted file from the source folder
                # os.remove(input_path)

# This block ensures it runs when executing the script
if __name__ == "__main__":
    preprocess_images_to_new_folder("dataset", "preprocessed_dataset")
