import os
from pyunpack import Archive
from ultralytics import YOLO

# Dataset paths
dataset_path = r"C:\path\to\dataset.rar"   # Update path
extract_path = r"C:\path\to\dataset_root"  # Update path
dataset_dir  = os.path.join(extract_path, "DATASET_FOLDER")  # Update folder name

# Extract dataset
os.makedirs(extract_path, exist_ok=True)
print("Extracting dataset...")
Archive(dataset_path).extractall(extract_path)
print("Extraction complete!")

# Fix data.yaml paths
data_yaml_path = os.path.join(dataset_dir, "data.yaml")
with open(data_yaml_path, "r") as f:
    yaml_content = f.read()
yaml_content = yaml_content.replace("..", dataset_dir.replace('\\','/'))
with open(data_yaml_path, "w") as f:
    f.write(yaml_content)

print("Corrected data.yaml:")
print(yaml_content)

# Train model
model = YOLO("yolov5l.pt")
results = model.train(
    data=data_yaml_path,
    epochs=100,
    patience=10,
    imgsz=640,
    batch=16,
    name="yolov5l_run",
    project="./runs2",
    plots=True
)

print("Training completed!")
metrics = model.val()
print("Validation metrics:", metrics)
