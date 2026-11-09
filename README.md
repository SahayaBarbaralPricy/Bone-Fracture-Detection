# 🦴 Bone Fracture Detection System

An AI-powered web application that uses Convolutional Neural Networks (CNN) and EfficientNetB0 with Transfer Learning to classify bone X-ray images as **Fractured** or **Normal**.

## 📌 Project Overview

The Bone Fracture Detection System is a web-based application developed to assist in the classification of bone fractures from X-ray images.

The application uses a pre-trained EfficientNetB0 deep learning model with Transfer Learning to analyze uploaded X-ray images and predict whether a fracture is present.

It provides a user-friendly interface for image uploads, prediction results, prediction history, user profile management, and PDF report generation.

## ✨ Features

- User Registration and Login
- Secure User Authentication
- X-ray Image Upload
- AI-Based Bone Fracture Prediction
- Fractured / Normal Classification
- Prediction History
- User Profile Management
- PDF Report Generation and Download
- Responsive Web Interface
- MySQL Database Integration

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Flask

### Artificial Intelligence and Deep Learning
- TensorFlow
- Keras
- Convolutional Neural Network (CNN)
- EfficientNetB0
- Transfer Learning

### Image Processing
- OpenCV
- Pillow
- NumPy

### Database
- MySQL

### Additional Tools
- ReportLab
- Git
- GitHub
- Visual Studio Code

## 🧠 Deep Learning Model

The project uses **EfficientNetB0**, a pre-trained convolutional neural network architecture, with Transfer Learning.

### Model Workflow

1. Collect and organize bone X-ray images.
2. Preprocess images before model training.
3. Load the pre-trained EfficientNetB0 architecture.
4. Apply Transfer Learning for fracture classification.
5. Train and validate the model using labeled X-ray images.
6. Save the trained model.
7. Load the trained model into the Flask application.
8. Predict the class of uploaded X-ray images.

### Classification Categories

| Class | Description |
|---|---|
| Fracture | X-ray image classified as fractured |
| Normal | X-ray image classified as normal |

**Trained Model:** `bone_fracture_model.h5`

**Model Architecture:** EfficientNetB0

## 📂 Project Structure

```text
Bone-Fracture-Detection/
│
├── app.py
├── config.py
├── database.sql
├── requirements.txt
├── README.md
│
├── database/
│   ├── db.py
│   └── queries.py
│
├── model/
│   ├── bone_fracture_model.h5
│   ├── predict.py
│   └── preprocess.py
│
├── routes/
│   ├── __init__.py
│   ├── auth.py
│   ├── dashboard.py
│   ├── upload.py
│   ├── prediction.py
│   ├── history.py
│   ├── profile.py
│   └── report.py
│
├── static/
│   ├── css/
│   └── images/
│
├── templates/
│
└── utils/
    └── auth.py
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/SahayaBarbaralPricy/Bone-Fracture-Detection.git
```

### 2. Navigate to the Project Folder

```bash
cd Bone-Fracture-Detection
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

## 🗄️ Database Configuration

1. Install and start MySQL using MySQL Server or XAMPP.
2. Open phpMyAdmin or MySQL Command Line.
3. Import the `database.sql` file.
4. Verify that the database `bone_fracture_db` has been created.

### Environment Variables

Create a `.env` file in the project root directory.

Add your own configuration:

```env
SECRET_KEY=your_secret_key

MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=
MYSQL_DB=bone_fracture_db
```

Replace the example values with your local configuration.

**Important:** Never upload your `.env` file or actual credentials to GitHub.

## ▶️ Run the Application

After configuring the database and installing the dependencies, execute:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

Register or log in to access the application.

## 🔄 Application Workflow

```text
User Registration / Login
          |
          v
      Dashboard
          |
          v
    Upload X-ray Image
          |
          v
    Image Preprocessing
          |
          v
    EfficientNetB0 Model
          |
          v
    Fracture Prediction
          |
          v
    Display Prediction
          |
          v
    Save Prediction History
          |
          v
    Generate PDF Report
```

## 🔐 Security

- Environment variables are used for sensitive configuration.
- Uploaded files are restricted to supported image formats.
- Maximum upload size is configured to 16 MB.
- User authentication is provided.
- Generated files and uploaded images are excluded from Git tracking.

## 🚀 Future Enhancements

- Improve model accuracy through additional training and evaluation.
- Support more bone fracture categories.
- Add advanced visualization of prediction results.
- Deploy the application to a cloud hosting platform.
- Improve prediction performance and scalability.

## ⚠️ Disclaimer

This project is developed for educational and research purposes. Its predictions are not a substitute for professional medical diagnosis. All X-ray interpretations should be reviewed by qualified healthcare professionals.

## 👩‍💻 Developer

**Sahaya Barbaral Pricy M**

MCA Graduate | Python Developer | AI/ML Enthusiast

### GitHub Repository

[Bone-Fracture-Detection](https://github.com/SahayaBarbaralPricy/Bone-Fracture-Detection)

---

⭐ If you find this project interesting, consider giving the repository a star!
