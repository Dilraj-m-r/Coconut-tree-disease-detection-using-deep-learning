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


📊 Results

Input size: 150x150 RGB images

Optimizer: Adam | Loss: Categorical Crossentropy

Output: 4 disease classes with probability scores

Accuracy: 70%

📜 License
This project is licensed under the MIT License.

👨‍💻 Author: Dilraj M R | Final Year CSE Student | AI & Web Developer
