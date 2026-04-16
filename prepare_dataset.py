import os
import shutil

# =========================
# PATHS
# =========================
BASE_DIR = os.path.abspath(os.getcwd())

REVIEW_DIR = os.path.join(BASE_DIR, "dataset/review")
FINAL_DIR = os.path.join(BASE_DIR, "dataset/final_dataset")

REVIEW_IMAGES = os.path.join(REVIEW_DIR, "images")
REVIEW_LABELS = os.path.join(REVIEW_DIR, "labels")

FINAL_IMAGES = os.path.join(FINAL_DIR, "images")
FINAL_LABELS = os.path.join(FINAL_DIR, "labels")

IMAGE_EXTS = [".jpg", ".jpeg", ".png"]

# =========================
# CREATE FINAL DATASET
# =========================
def create_final_dataset():
    print("Preparing final dataset...")

    # remove old dataset if exists
    if os.path.exists(FINAL_DIR):
        shutil.rmtree(FINAL_DIR)

    os.makedirs(FINAL_IMAGES, exist_ok=True)
    os.makedirs(FINAL_LABELS, exist_ok=True)

    total = 0

    for img_file in os.listdir(REVIEW_IMAGES):
        base, ext = os.path.splitext(img_file)

        if ext.lower() not in IMAGE_EXTS:
            continue

        total += 1

        src_img = os.path.join(REVIEW_IMAGES, img_file)
        dst_img = os.path.join(FINAL_IMAGES, img_file)

        src_label = os.path.join(REVIEW_LABELS, base + ".txt")
        dst_label = os.path.join(FINAL_LABELS, base + ".txt")

        # copy image
        shutil.copy(src_img, dst_img)

        # copy label (must exist now)
        if os.path.exists(src_label):
            shutil.copy(src_label, dst_label)
        else:
            raise Exception(f"Missing label for {img_file}")

    print(f"✅ Final dataset created with {total} images")


if __name__ == "__main__":
    create_final_dataset()