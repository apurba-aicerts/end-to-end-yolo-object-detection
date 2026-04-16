import os

BASE_DIR = os.path.abspath(os.getcwd())

IMAGES_DIR = os.path.join(BASE_DIR, "dataset/review/images")
LABELS_DIR = os.path.join(BASE_DIR, "dataset/review/labels")

IMAGE_EXTS = [".jpg", ".jpeg", ".png"]

missing_labels = []
empty_labels = []
total_images = 0
created_labels = 0

# 🔧 Toggle this to auto-fix missing labels
AUTO_CREATE_EMPTY = True

for img_file in os.listdir(IMAGES_DIR):
    base, ext = os.path.splitext(img_file)

    if ext.lower() not in IMAGE_EXTS:
        continue

    total_images += 1

    label_path = os.path.join(LABELS_DIR, base + ".txt")

    if not os.path.exists(label_path):
        missing_labels.append(img_file)

        if AUTO_CREATE_EMPTY:
            open(label_path, "w").close()
            created_labels += 1
    else:
        if os.path.getsize(label_path) == 0:
            empty_labels.append(img_file)

print("\n===== DATASET REPORT =====")
print(f"Total Images: {total_images}")
print(f"Missing Labels: {len(missing_labels)}")
print(f"Empty Labels: {len(empty_labels)}")

if AUTO_CREATE_EMPTY:
    print(f"Auto-created empty labels: {created_labels}")

if missing_labels:
    print("\nImages missing labels:")
    for img in missing_labels:
        print(f" - {img}")

if empty_labels:
    print("\nImages with empty labels (valid but check):")
    for img in empty_labels:
        print(f" - {img}")