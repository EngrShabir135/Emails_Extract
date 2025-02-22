# Email Extractor - Streamlit App

This project is a **Streamlit web application** that allows users to **upload an image** and **extract email addresses** using **OCR (Optical Character Recognition)** with `pytesseract`.

## 🚀 Features
- Upload an image containing text
- Extract email addresses from the image
- Display emails one per line in the output
- User-friendly Streamlit UI

## 📦 Installation
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/YourUsername/email-extractor.git
cd email-extractor
```

### **2️⃣ Create a Virtual Environment (Optional but Recommended)**
```sh
python -m venv venv  # Create virtual environment
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Install Tesseract OCR**
- **Windows**: Download from [Tesseract](https://github.com/UB-Mannheim/tesseract/wiki) and add it to PATH.
- **Linux/macOS**:
```sh
sudo apt install tesseract-ocr  # Ubuntu
brew install tesseract  # macOS
```

## ▶️ Running the App Locally
```sh
streamlit run app.py
```

This will open the app in your browser.

## 🚀 Deployment on Streamlit Cloud
1. Push your code to GitHub:
```sh
git add .
git commit -m "Initial commit"
git push origin main
```
2. Go to [Streamlit Cloud](https://share.streamlit.io/)
3. Click "New App", connect your GitHub repository, and set the `app.py` file.
4. Click "Deploy" to make it live!

## 📄 File Structure
```
email-extractor/
│── app.py                # Main Streamlit App
│── requirements.txt      # Dependencies
│── README.md             # Project Documentation
```

## 🛠 Technologies Used
- **Python**
- **Streamlit**
- **pytesseract** (Tesseract OCR)
- **PIL (Pillow)**
- **OpenCV**

## 📬 Contact
For any questions, feel free to reach out!

Happy Coding! 🚀

