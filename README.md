# SIGHT SENSE: Automated Captioning of Visual Data

This is a major final-year academic project developed at SRM Institute of Science and Technology. The system uses a deep learning architecture combining VGG16, EfficientNetB7, and LSTM to generate accurate, context-aware captions for images. It was presented at ICIOT 2025 and accepted for publication in the AIP Conference Proceedings.

---

## 🔍 Overview

- Uses CNNs (VGG16, EfficientNetB7) for image feature extraction
- Employs LSTM for sequential caption generation
- Trained on the Flickr8k dataset (augmented to 40k)
- Generates captions in natural language using attention mechanisms
- Evaluated using BLEU score for linguistic similarity

---

## 🧠 Technologies Used

- Python
- TensorFlow / Keras
- OpenCV
- NumPy, Pandas
- NLTK
- Matplotlib
- gTTS (for optional voice output)

---

## 📁 Project Structure

sight-sense-image-captioning/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── final_report/
│ └── SIGHT_SENSE_Final_Report.md
├── data/
│ └── README.md
├── notebook/
│ └── model_training_and_testing.ipynb
├── assets/
│ ├── demo.png
│ ├── conference_certificate.png
│ └── training_validation.png
├── src/
│ ├── preprocessing.py
│ ├── feature_extraction.py
│ ├── caption_generator.py
│ ├── evaluate.py
│ └── app.py


---

## 🧪 Dataset

- Base dataset: Flickr8k
- Each image has 5 captions
- Data augmentation techniques used:
  - Horizontal flip
  - Rotation (up to 10°)
  - Width and height shift (10%)
  - Nearest fill mode
- Augmented to a total of 40,000 images

---

## 📊 Evaluation Metrics

- BLEU Score used to measure caption quality
- Classification report included for caption tokens
- Training and validation accuracy converged around 95%
- Training and validation loss decreased smoothly to < 0.2

---

## 🏆 Achievements

- Accepted and presented at ICIOT 2025 (SRM Institute of Science and Technology)
- Paper ID: 460 | Plagiarism Score: 1%
- Published in AIP Conference Proceedings (2025)
- Received excellent feedback from review panel

---

## 📌 Notes

- This repository is made public for viewing and academic inspiration only
- Reproduction, redistribution, or reuse of the code or content is strictly prohibited
- Please refer to the LICENSE file for detailed restrictions

---

## 👨‍💻 Developer

Venkat Aditya Vellanki  
Final Year B.Tech CSE  
SRM Institute of Science and Technology  

---

---

## 🔒 Disclaimer

This project, **SIGHT SENSE: Automated Captioning of Visual Data**, was developed as part of the author's **final semester (8th Semester, 2025)** undergraduate curriculum at SRM Institute of Science and Technology.

The repository is made public **solely for academic reference, learning, and inspiration purposes**.  
**Commercial use, reproduction, redistribution, or derivative works based on the contents of this repository are strictly prohibited without explicit written permission.**

All contents including code, models, results, and documentation are protected under **All Rights Reserved**.  
Ownership remains with the original creator.

© 2025 **Venkat Aditya Vellanki**. All Rights Reserved.
