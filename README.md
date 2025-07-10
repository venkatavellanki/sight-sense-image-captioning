# 🧠 SIGHT SENSE: Automated Captioning of Visual Data

SIGHT SENSE is a deep learning-based system for generating meaningful, context-aware captions for images. Developed using CNN-LSTM architecture, the model integrates VGG16 and EfficientNetB7 for visual feature extraction and an LSTM with attention mechanism for sequence prediction.

---

## 🚀 Features

- 📷 Image preprocessing with VGG16 and EfficientNetB7
- 🧠 Language generation using LSTM with attention
- 🔁 Data augmentation for robust training
- 📊 Evaluation via BLEU score
- 🏅 Presented at ICIOT 2025 (Paper ID: 460)
- 🧩 Journal publication accepted by AIP Conference Proceedings

---

## 📂 Dataset

The system uses the **Flickr8k** dataset:
- 8,000 images
- 5 human-written captions per image
- Augmented to 40,000+ images via rotation, shift, flip

---

## 🛠️ Tech Stack

- Python
- TensorFlow / Keras
- NumPy, OpenCV, NLTK, Matplotlib
- Jupyter Notebook

---

## 📦 Installation

# Clone the repository
```bash
git clone https://github.com/venkatavellanki/sight-sense-image-captioning.git
```

# Navigate to the project folder
```bash
cd sight-sense-image-captioning
```

# Install dependencies
```bash
pip install -r requirements.txt
```
---

## 📊 Evaluation

Evaluation is done using the BLEU score, comparing model-generated captions with human-written references.

---

## 📁 Folder Structure

sight-sense-image-captioning/
├── src/
├── data/
├── models/
├── notebooks/
├── requirements.txt
├── .gitignore
└── README.md

---

## 📌 Disclaimer

This project was developed as part of my final year academic coursework in the 8th semester (2025).  
While the repository is public for educational insight and viewing, **reproduction, distribution, or commercial use is strictly prohibited**.

© 2025 **Venkat Aditya Vellanki**. All rights reserved.
