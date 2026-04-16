import os
import shutil

# =========================
# PATHS
# =========================
BASE_DIR = os.path.abspath(os.getcwd())

INPUT_DIR = os.path.join(BASE_DIR, "dataset/auto_labels/yolov8n_1")
OUTPUT_DIR = os.path.join(BASE_DIR, "dataset/review")

INPUT_LABELS = os.path.join(INPUT_DIR, "labels")
INPUT_IMAGES = os.path.join(INPUT_DIR)

OUTPUT_LABELS = os.path.join(OUTPUT_DIR, "labels")
OUTPUT_IMAGES = os.path.join(OUTPUT_DIR, "images")

os.makedirs(OUTPUT_LABELS, exist_ok=True)
os.makedirs(OUTPUT_IMAGES, exist_ok=True)

# =========================
# CLASS MAPPING (YOLO → YOUR)
# =========================
YOLO_TO_CUSTOM = {
    67: 0,  # cell phone → phone
    63: 1,  # laptop
    73: 2,  # book
    62: 3   # tv
}

# =========================
# SUPPORTED IMAGE EXTENSIONS
# =========================
IMAGE_EXTS = [".jpg", ".jpeg", ".png"]

# =========================
# PROCESS
# =========================
total_images = 0
images_with_labels = 0
images_without_labels = 0

for img_file in os.listdir(INPUT_IMAGES):
    base_name, ext = os.path.splitext(img_file)

    if ext.lower() not in IMAGE_EXTS:
        continue

    total_images += 1

    input_img_path = os.path.join(INPUT_IMAGES, img_file)
    output_img_path = os.path.join(OUTPUT_IMAGES, img_file)

    label_file = base_name + ".txt"
    input_label_path = os.path.join(INPUT_LABELS, label_file)
    output_label_path = os.path.join(OUTPUT_LABELS, label_file)

    new_lines = []

    # =========================
    # IF LABEL EXISTS → PROCESS
    # =========================
    if os.path.exists(input_label_path):
        with open(input_label_path, "r") as f:
            lines = f.readlines()

        for line in lines:
            parts = line.strip().split()

            cls_id = int(parts[0])

            if cls_id in YOLO_TO_CUSTOM:
                new_cls = YOLO_TO_CUSTOM[cls_id]
                new_line = [str(new_cls)] + parts[1:5]
                new_lines.append(" ".join(new_line))

    # =========================
    # ALWAYS COPY IMAGE
    # =========================
    shutil.copy(input_img_path, output_img_path)

    # =========================
    # SAVE LABEL ONLY IF EXISTS
    # =========================
    if new_lines:
        with open(output_label_path, "w") as f:
            f.write("\n".join(new_lines))
        images_with_labels += 1
    else:
        images_without_labels += 1

# =========================
# SUMMARY
# =========================
print("\nFiltering Done")
print(f"Total Images: {total_images}")
print(f"Images with labels: {images_with_labels}")
print(f"Images without labels: {images_without_labels}")