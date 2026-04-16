# 📦 End-to-End YOLO Object Detection Pipeline

This project builds a complete pipeline for creating a custom object detection model using YOLOv8 — from raw images to training and evaluation.

---

# 🚀 Project Overview

This pipeline includes:

1. Auto-labeling using pretrained YOLO
2. Filtering only required classes
3. Manual annotation for missing objects
4. Dataset validation
5. Final dataset preparation
6. Model training using YOLOv8
7. Evaluation and inference

---

# 📁 Project Structure

```
project_root/
│
├── dataset/
│   ├── raw_images/              # Original images
│   ├── auto_labels/             # YOLO auto-generated labels
│   ├── review/                  # Filtered + manually corrected data
│   │   ├── images/
│   │   ├── labels/
│   │
│   ├── final_dataset/           # Final dataset for training
│       ├── images/
│       ├── labels/
│
├── outputs/                     # Training outputs
│
├── run_yolo.py                  # Auto-labeling script
├── filter_labels.py             # Class filtering script
├── validate_dataset.py          # Dataset validation
├── create_dataset.py            # Final dataset creation
├── train.py                     # Training script
│
└── README.md
```

---

# ⚙️ Setup Instructions

## 1. Create Environment

```bash
python -m venv label_env_39
source label_env_39/bin/activate
```

## 2. Install Dependencies

```bash
pip install ultralytics opencv-python
```

---

# 🎯 Classes Used

```
0 → phone
1 → laptop
2 → book
3 → tv
4 → headphone
5 → earbuds
```

---

# 🔄 Step-by-Step Pipeline

## Step 1: Auto Labeling

Run YOLO on raw images:

```bash
python run_yolo.py
```

Output:

```
dataset/auto_labels/run1/
```

---

## Step 2: Filter Required Classes

Filter only selected classes from YOLO output:

```bash
python filter_labels.py
```

Output:

```
dataset/review/
├── images/
├── labels/
```

---

## Step 3: Manual Annotation

Use LabelImg tool:

```bash
labelImg dataset/review/images dataset/classes.txt
```

Instructions:

* Open `dataset/review/images`
* Set save directory → `dataset/review/labels`
* Add missing objects (headphone, earbuds, etc.)
* Do NOT overwrite existing correct labels

---

## Step 4: Validate Dataset

Check dataset quality:

```bash
python validate_dataset.py
```

Checks:

* Missing labels
* Empty labels

---

## Step 5: Create Final Dataset

Prepare clean dataset for training:

```bash
python create_dataset.py
```

Output:

```
dataset/final_dataset/
├── images/
├── labels/
```

---

## Step 6: Train Model

```bash
python train.py
```

This will:

* Create `data.yaml`
* Start training
* Save outputs in:

```
outputs/yolov8n_exp1/
```

---

# 📊 Training Output

Key files:

```
outputs/yolov8n_exp1/
├── weights/
│   ├── best.pt
│   ├── last.pt
├── results.png
├── labels.jpg
```

---

# 🔍 Inference (Testing)

```python
from ultralytics import YOLO

model = YOLO("outputs/yolov8n_exp1/weights/best.pt")
model.predict(source="test_images/", save=True)
```

---

# ⚠️ Important Notes

* Small dataset (41 images) → model may overfit
* Always test on unseen images
* Improve dataset for better generalization

---

# 📈 Improvement Suggestions

* Add more images
* Increase variation (lighting, angles)
* Balance classes
* Create train/val split

---

# 🧠 Pipeline Summary

```
Raw Images
   ↓
YOLO Auto Label
   ↓
Filter Classes
   ↓
Manual Labeling
   ↓
Validation
   ↓
Final Dataset
   ↓
Training
   ↓
Model
```

---

# ✅ Status

✔ End-to-end pipeline completed
✔ Model trained successfully
✔ Ready for improvement / deployment

---

# 🚀 Next Steps

* Dataset expansion
* Model optimization (ONNX / TensorRT)
* Deployment (API / Streamlit / Triton)

---

**Author:** Apurba
