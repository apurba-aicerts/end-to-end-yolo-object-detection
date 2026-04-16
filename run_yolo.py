import os
from ultralytics import YOLO

# =========================
# FIXED BASE PATH
# =========================
BASE_DIR = os.path.abspath(os.getcwd())

MODEL_PATH = "yolov8n.pt"
SOURCE_DIR = os.path.join(BASE_DIR, "dataset/raw_images")
OUTPUT_DIR = os.path.join(BASE_DIR, "dataset/auto_labels")
RUN_NAME = "yolov8n_1"

def run_inference():
    print(f"Base Dir: {BASE_DIR}")
    print("Loading YOLO model...")

    model = YOLO(MODEL_PATH)

    print("Running inference...")
    model.predict(
        source=SOURCE_DIR,
        save=True,
        save_txt=True,
        save_conf=True,
        project=OUTPUT_DIR,
        name=RUN_NAME,
        exist_ok=True
    )

    label_path = os.path.join(OUTPUT_DIR, RUN_NAME, "labels")

    print(f"Checking labels at: {label_path}")

    if os.path.exists(label_path):
        files = os.listdir(label_path)
        print(f"✅ Found {len(files)} label files")
    else:
        print("❌ ERROR: Labels not found in expected location")

if __name__ == "__main__":
    run_inference()