🌴 Coconut Disease Detection using Deep Learning 🧠📷

Coconut Disease Detection is a Deep Learning-based image classification project that identifies four major coconut tree diseases. The project applies Convolutional Neural Networks (CNNs) along with data augmentation techniques to build a robust model for plant disease recognition, helping farmers and researchers monitor tree health effectively.

💻 Tech Stack & Tools

Programming Language: Python 🐍

Deep Learning Framework: Keras, TensorFlow

Data Processing: NumPy, Pandas, OpenCV, scikit-learn

Visualization: Matplotlib

Augmentation: Keras ImageDataGenerator, Augmentor

IDE & Tools: VS Code, Jupyter Notebook

🧩 Features

1️⃣ Image Preprocessing – Resizing coconut disease images to 150x150 pixels for uniformity
2️⃣ Data Augmentation – Online augmentation (rotation, zoom, shear, shifts) and offline augmentation (flip, skew, grayscale) for dataset expansion
3️⃣ Deep CNN Model – 5 convolutional blocks with pooling, batch normalization, and dropout layers for better generalization
4️⃣ Classification – Detects and classifies images into 4 categories:

🕷️ Eriophyid Mite

🪲 Red Palm Weevil

🐞 Rhinoceros Beetle

🌀 Rugose Spiraling Whitefly

5️⃣ Model Saving – Trained model exported as trained_model_coconut.h5 (⚠️ excluded from repo due to GitHub size limits)
6️⃣ Training & Validation – Accuracy and loss metrics tracked using validation split
7️⃣ Practical Application – Supports agricultural disease monitoring and early detection

📂 Project Structure

CoconutDisease/
│── coconut_train.py        # Training script for CNN
│── augmentation.py         # Data augmentation using Augmentor
│── dataset/                # Image dataset (by disease class)
│── trained_model_coconut.h5 (ignored due to size >100MB)
│── README.md               # Project documentation


⚙️ Setup Instructions

Clone the repository:

git clone https://github.com/Dilraj-m-r/Coconut-tree-disease-detection-using-deep-learning.git
cd CoconutDisease


Install dependencies:

pip install -r requirements.txt


(Optional) Generate augmented images:

python augmentation.py


Train the model:

python coconut_train.py

SCREENSHOTS
REGISTER

<img width="1919" height="1023" alt="Screenshot 2025-09-17 160600" src="https://github.com/user-attachments/assets/a44fe23b-f6e8-487c-85f4-6470b1b8e409" />

SIGIN

<img width="1919" height="1020" alt="Screenshot 2025-09-17 160539" src="https://github.com/user-attachments/assets/ddd3c623-f91a-49e3-8ff9-23b89f474c6a" />

UPLOAD

<img width="1919" height="1014" alt="Screenshot 2025-09-17 160627" src="https://github.com/user-attachments/assets/4cebc31c-f4bd-4693-8a44-f87fdff22bc8" />

🕷️ Eriophyid Mite

<img width="1919" height="1013" alt="Screenshot 2025-09-17 160651" src="https://github.com/user-attachments/assets/c32c164d-58e2-4e82-9866-2a2d40f0fcd7" />

🪲 Red Palm Weevil

<img width="1913" height="1012" alt="Screenshot 2025-09-17 160800" src="https://github.com/user-attachments/assets/0ea2ec62-1930-4f5d-b4d8-2099f86741b5" />

🐞 Rhinoceros Beetle

<img width="1893" height="1012" alt="Screenshot 2025-09-17 160722" src="https://github.com/user-attachments/assets/e7d72326-290a-477a-857c-b30c68032730" />

🌀 Rugose Spiraling Whitefly

<img width="1895" height="1006" alt="Screenshot 2025-09-17 160919" src="https://github.com/user-attachments/assets/122fa03c-a233-4f75-8f62-ef59a38ff3f8" />


📊 Results

Input size: 150x150 RGB images

Optimizer: Adam | Loss: Categorical Crossentropy

Output: 4 disease classes with probability scores

Accuracy: 70%

⚠️ Note on Model File

The trained model file (trained_model_coconut.h5) is ~170 MB and cannot be uploaded to GitHub due to size limits.
Download it here: https://drive.google.com/file/d/1I4yFShd1tvodWeEyas98pKCUnEVIwiA0/view?usp=sharing

📜 License
This project is licensed under the MIT License.

👨‍💻 Author: Dilraj M R | Final Year CSE Student | AI & Web Developer
