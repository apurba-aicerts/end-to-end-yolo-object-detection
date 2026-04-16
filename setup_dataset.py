import os

BASE_DIR = "dataset"

STRUCTURE = [
    "raw_images",
    "auto_labels/images",
    "auto_labels/labels",
    "review/images",
    "review/labels",
    "final_dataset/images",
    "final_dataset/labels"
]

def create_structure():
    for path in STRUCTURE:
        full_path = os.path.join(BASE_DIR, path)
        os.makedirs(full_path, exist_ok=True)
        print(f"Created: {full_path}")

    # Create classes.txt if not exists
    classes_file = os.path.join(BASE_DIR, "classes.txt")
    if not os.path.exists(classes_file):
        with open(classes_file, "w") as f:
            f.write("earbuds\ncell phone\nlaptop\nbook\ntv\nhead phone\n")
        print(f"Created: {classes_file}")
    else:
        print(f"Already exists: {classes_file}")

if __name__ == "__main__":
    create_structure()