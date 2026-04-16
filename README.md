🚀 PHASE 1 — Setup (Do this first, no shortcuts)
🔷 1. Define your final classes

Create:

classes.txt
person
phone
laptop
book
calculator

👉 This file will be used by:

YOLO mapping script
LabelImg
Training
🔷 2. Create folder structure
dataset/
│
├── raw_images/
├── auto_labels/
│   ├── images/
│   ├── labels/
│
├── review/
│   ├── images/
│   ├── labels/
│
├── final_dataset/
│   ├── images/
│   ├── labels/
│
└── classes.txt
🚀 PHASE 2 — YOLO Auto Labeling

We’ll use YOLO object detection model

🔷 3. Run YOLO inference

Example (Ultralytics):

yolo predict \
  model=yolov8n.pt \
  source=dataset/raw_images \
  save_txt=True \
  save_conf=True \
  project=dataset/auto_labels \
  name=run1

👉 Output:

auto_labels/run1/images/
auto_labels/run1/labels/
🚀 PHASE 3 — Filtering + Class Mapping (CRITICAL STEP)

Now we write your first real script

🔷 4. Mapping Script (IMPORTANT)

Create: filter_labels.py

import os

# YOLO COCO → YOUR CLASSES
YOLO_TO_CUSTOM = {
    0: 0,   # person
    67: 1,  # phone
    63: 2   # laptop
}

INPUT_LABEL_DIR = "dataset/auto_labels/run1/labels"
INPUT_IMAGE_DIR = "dataset/auto_labels/run1/images"

OUTPUT_LABEL_DIR = "dataset/review/labels"
OUTPUT_IMAGE_DIR = "dataset/review/images"

os.makedirs(OUTPUT_LABEL_DIR, exist_ok=True)
os.makedirs(OUTPUT_IMAGE_DIR, exist_ok=True)

for file in os.listdir(INPUT_LABEL_DIR):
    if not file.endswith(".txt"):
        continue

    input_path = os.path.join(INPUT_LABEL_DIR, file)
    output_path = os.path.join(OUTPUT_LABEL_DIR, file)

    new_lines = []

    with open(input_path, "r") as f:
        lines = f.readlines()

    for line in lines:
        parts = line.strip().split()
        cls_id = int(parts[0])

        if cls_id in YOLO_TO_CUSTOM:
            new_cls = YOLO_TO_CUSTOM[cls_id]
            new_line = [str(new_cls)] + parts[1:]
            new_lines.append(" ".join(new_line))

    # Save only if relevant objects exist
    if new_lines:
        with open(output_path, "w") as f:
            f.write("\n".join(new_lines))

        # copy corresponding image
        img_name = file.replace(".txt", ".jpg")
        src_img = os.path.join(INPUT_IMAGE_DIR, img_name)
        dst_img = os.path.join(OUTPUT_IMAGE_DIR, img_name)

        if os.path.exists(src_img):
            import shutil
            shutil.copy(src_img, dst_img)
🔥 What this script does

✔ Removes unwanted classes
✔ Converts class IDs
✔ Copies only useful images
✔ Prepares clean review dataset

🚀 PHASE 4 — Manual Review
🔷 5. Open LabelImg correctly
labelImg dataset/review/images dataset/classes.txt
🔷 6. Your job during review

For each image:

✔ Fix wrong boxes
✔ Add missing objects (VERY IMPORTANT)
✔ Delete incorrect detections

👉 Save → updates same .txt

🚀 PHASE 5 — Final Dataset Creation
🔷 7. Move reviewed data

Simple:

dataset/review → dataset/final_dataset

OR script:

import shutil
shutil.copytree("dataset/review", "dataset/final_dataset", dirs_exist_ok=True)
🚀 PHASE 6 — Training Ready

Now your dataset is:

final_dataset/
  images/
  labels/
classes.txt

👉 Ready for training 🚀

🧠 OPTIONAL (But Powerful)
Add confidence filtering

Modify script:

conf = float(parts[-1])  # if saved

if conf < 0.4:
    continue
💡 EXTRA (Future Upgrade)

Later you can:

Auto-send only low-confidence images to review
Skip high-confidence ones