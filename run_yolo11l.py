import os, sys, yaml
from ultralytics import YOLO
from pyunpack import Archive

already_extracted = False
rar_path     = r"C:\path\to\dataset.rar"       # Update
extract_path = r"C:\path\to\dataset_root"      # Update
dataset_dir  = r"C:\path\to\dataset_root\DATASET_FOLDER"  # Update

model_ckpt = "yolo11l.pt"
project_dir = "./runs_yolo11"

if not already_extracted:
    os.makedirs(extract_path, exist_ok=True)
    print("Extracting dataset...")
    Archive(rar_path).extractall(extract_path)
    print("Extraction complete!")

data_yaml_path = os.path.join(dataset_dir, "data.yaml")
if not os.path.isfile(data_yaml_path):
    print("[ERROR] data.yaml not found!")
    sys.exit(1)

with open(data_yaml_path, "r", encoding="utf-8") as f:
    data_cfg = yaml.safe_load(f)

def to_abs(p):
    return p if os.path.isabs(str(p)) else os.path.normpath(os.path.join(dataset_dir, str(p)))

for key in ["path","train","val","test"]:
    if key in data_cfg and data_cfg[key] is not None:
        data_cfg[key] = to_abs(data_cfg[key])

with open(data_yaml_path, "w", encoding="utf-8") as f:
    yaml.safe_dump(data_cfg, f, sort_keys=False)

print("Corrected data.yaml:")
print(yaml.safe_dump(data_cfg, sort_keys=False))

model = YOLO(model_ckpt)
results = model.train(
    data=data_yaml_path,
    epochs=100,
    patience=10,
    imgsz=640,
    batch=16,
    name="yolo11l_run",
    project=project_dir,
    plots=True
)
print("Training finished.")
metrics = model.val()
print("Validation metrics:", metrics)
