# 🌿 TgFC: Tectona grandis Fungal Community Dataset – Code & Validation

This repository contains the official source code and supplementary materials for the **Tectona grandis Fungal Community (TgFC)** dataset project. The TgFC dataset supports automated detection, classification, and quantification of fungal spores, enabling AI-assisted diagnostics, bioaerosol surveillance, and plant disease monitoring. This resource is applicable to forestry and agricultural ecosystems, with a focus on improving disease management, enhancing surveillance systems, and supporting research on fungal pathogens across diverse environments.

---

## 📦 Dataset Overview

The TgFC dataset includes **5,236 microscopic images** (640 × 640 pixels), categorized into three fungal taxa:

| Fungal Taxon             | Spore Type     | Image Count |
|--------------------------|----------------|-------------|
| *Olivea tectonae*        | Urediniospores | 2,219       |
| *Neopestalotiopsis* sp.  | Conidia        | 1,688       |
| *Colletotrichum siamense*| Conidia        | 1,329       |

All images were captured using microscopy with **no preprocessing**, preserving natural morphology. This approach ensures that trained AI models generalize effectively to raw data and diverse environments.

---

## 🧠 Repository Contents

```bash
├── models/
├── LICENSE
└── README.md
```

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

## 📊 Technical Validation

Model evaluation is performed using:

- Precision, Recall, F1-score  
- Normalized confusion matrices  
- Visual explanations using EigenCAM  

---

## 🛠️ Requirements

- Python 3.9+  
- PyTorch  
- OpenCV  
- Ultralytics
- Matplotlib, NumPy, Pandas

---

## 📜 Citation

Citation coming soon. Please check back after publication.  
If you use the dataset or code, please consider citing the original paper once available.

---

## 📬 Contact

For questions or collaborations, please contact:  

- **Maaz Ahmed** – <ahmedmaaz.maaz@gmail.com>
- **Syeda Munjiba Islam** - <islammunjiba@gmail.com>
- **Md. Faysal Ahamed** - <faysalahamedjishan@gmail.com>

---

## 📝 License

This project is licensed under the **MIT License**.
