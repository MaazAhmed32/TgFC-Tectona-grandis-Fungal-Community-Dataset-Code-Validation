# 🌿 TgFC: Tectona grandis Fungal Community Dataset – Code & Validation

This repository provides scripts and baseline experiments for validating the **Tectona grandis Fungal Community (TgFC) dataset**, a curated microscopic image dataset of fungal spores associated with *Tectona grandis* (teak).
It includes **nine YOLO variants** (YOLOv5s/m/l, YOLOv8s/m/l, YOLOv11s/m/l) to benchmark detection performance.

---

## 📂 Dataset Overview

The TgFC dataset contains **5,236 images** of three fungal taxa collected from teak leaves in Bangladesh:

| Class | Total Images | Train (80%) | Validation (10%) | Test (10%) |
|-------|--------------|-------------|------------------|------------|
| *Olivea tectonae*         | 2,219 | 1,787 | 224 | 208 |
| *Neopestalotiopsis* sp.   | 1,688 | 1,350 | 169 | 169 |
| *Colletotrichum siamense* | 1,329 | 1,077 | 119 | 133 |
| **Total** | **5,236** | **4,214** | **512** | **510** |

- Mixed-class test images were reserved for challenging evaluation.  
- Data are annotated in YOLO format (`images/`, `labels/`, `data.yaml`).  

---

## 🧪 Training & Validation Setup

- **Splits**: 80% train / 10% validation / 10% test  
- **Epochs**: 100  
- **Batch size**: 32  
- **Learning rate**: 0.01 (constant)  
- **Patience**: 10 (early stopping)  
- **Image size**: 640 × 640  
- **Metrics**: Precision, Recall, F1-Score, mAP@0.5  

---

## 📊 Baseline Results (Table 3 from paper)

| Model    | Precision | Recall | F1-Score | mAP@0.5 |
|----------|-----------|--------|----------|---------|
| YOLOv5s  | 0.881 | 0.945 | 0.912 | 0.899 |
| YOLOv5m  | 0.867 | 0.949 | 0.906 | 0.907 |
| YOLOv5l  | 0.882 | 0.949 | 0.914 | 0.903 |
| YOLOv8s  | 0.874 | 0.928 | 0.900 | 0.893 |
| YOLOv8m  | 0.880 | 0.928 | 0.903 | 0.895 |
| YOLOv8l  | 0.868 | 0.943 | 0.904 | 0.900 |
| YOLO11s  | 0.883 | 0.944 | 0.913 | 0.896 |
| YOLO11m  | 0.865 | 0.956 | 0.908 | 0.909 |
| YOLO11l  | 0.875 | 0.959 | 0.915 | 0.907 |

➡️ **YOLO11l** achieved the strongest performance, with balanced precision and recall across all three fungal taxa.  

---

## 🔍 Visual Results

### Figure 7 — Confusion Matrix (YOLO11l)

The YOLO11l model achieved >90% correct classification for *Olivea tectonae* and *Colletotrichum siamense*, and 93% for *Neopestalotiopsis*.  

![Figure 7: Confusion Matrix](fig7_confusion_matrix.png)  
*Replace with actual confusion matrix figure from the paper or training output*  

---

### Figure 8 — Qualitative Detection Examples (YOLO11l)

YOLO11l detections across test images:  
- High-confidence predictions (>90%) for single-class spores  
- Correct multi-class detection in mixed spore images  

![Figure 8: Detection Examples](fig8_detection_examples.png)  
*Replace with actual detection example figure from the paper or training output*  

---

## ⚙️ Repository Usage

### Dependencies
```bash
pip install ultralytics pyunpack patool pyyaml
```
- Windows: install [7-Zip](https://www.7-zip.org/) and add it to PATH for `.rar` extraction  
- Linux/macOS: install `unrar` or `p7zip`  

### Scripts Included
- `run_yolov5s.py`, `run_yolov5m.py`, `run_yolov5l.py`  
- `run_yolov8s.py`, `run_yolov8m.py`, `run_yolov8l.py`  
- `run_yolo11s.py`, `run_yolo11m.py`, `run_yolo11l.py`  

### How to Run
1. Edit dataset paths in each script (`dataset_path`, `extract_path`, `dataset_dir`).  
2. Run any script, e.g.:  
```bash
python run_yolov8s.py
python run_yolo11l.py
```

Each script will:
- (Optionally) extract `.rar`  
- Fix `data.yaml` paths  
- Train YOLO model (patience=10)  
- Validate and print metrics  

---

## 🚀 Use Cases

- Enables automated spore identification from foliar samples, reducing manual effort.
- Improves airborne spore detection using pre-labeled data for machine learning models.
- Integrates with real-time monitoring systems for early disease intervention.
- Allows spore quantification from air samples for outbreak prediction.
- Applicable beyond teak, as included fungi are common in other ecosystems.
- Open-access format allows future expansion with more annotated images.
- Suitable for training and benchmarking deep learning models like YOLO and CNNs.
- Supports transfer learning across fungal species and imaging conditions.
- Useful for developing portable, field-ready diagnostic tools.

---

## 📑 Citation

If you use this dataset or validation scripts, please cite:  
- **The TgFC dataset paper**  
- **Ultralytics YOLO**  

---
## 📬 Contact

For questions or collaborations, please contact:  

- **Maaz Ahmed** – <ahmedmaaz.maaz@gmail.com>
- **Syeda Munjiba Islam** - <islammunjiba@gmail.com>
- **Md. Faysal Ahamed** - <faysal.ahamed@ece.ruet.ac.bd>

---

## 📝 License

This project is licensed under the **MIT License**.


✨ This repository provides **transparent and reproducible baselines** for fungal spore detection, aligning dataset publication with modern YOLO validation pipelines.  
