import os
import yaml
from ultralytics import YOLO

# =========================
# PATHS
# =========================
BASE_DIR = os.path.abspath(os.getcwd())

FINAL_DIR = os.path.join(BASE_DIR, "dataset/final_dataset")
DATA_YAML = os.path.join(BASE_DIR, "dataset/data.yaml")

# 👇 Custom output directory
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
RUN_NAME = "yolov8n_exp1"

# =========================
# CREATE DATA YAML
# =========================
def create_yaml():
    data = {
        "path": FINAL_DIR,
        "train": "images",
        "val": "images",
        "names": {
            0: "phone",
            1: "laptop",
            2: "book",
            3: "tv",
            4: "headphone",
            5: "earbuds"
        }
    }

    with open(DATA_YAML, "w") as f:
        yaml.dump(data, f)

    print("✅ data.yaml created")


# =========================
# TRAIN MODEL
# =========================
def train():
    print("Starting training...")

    model = YOLO("yolov8n.pt")

    model.train(
        data=DATA_YAML,
        epochs=50,
        imgsz=640,
        project=OUTPUT_DIR,   # 👈 controls base output dir
        name=RUN_NAME,       # 👈 experiment name
        exist_ok=True        # 👈 overwrite if exists
    )

    print("🔥 Training complete")


# =========================
if __name__ == "__main__":
    create_yaml()
    train()