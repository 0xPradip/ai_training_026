# 🤖 AI Camera - Emotion Detection & Finger Counting

A real-time AI Camera application built with **Python 3.11.9**, **OpenCV**, **MediaPipe**, and **DeepFace**.

> **Important:** This project was developed and tested using **Python 3.11.9**. It is **not recommended** to use the latest Python versions (such as Python 3.13 or 3.14) because some required libraries (especially MediaPipe and TensorFlow) may not yet support them.

---

## 📌 Features

- 😀 Real-time Emotion Detection
- ✋ Hand Detection
- 👍 Finger Counting
- 📷 Live Webcam Feed
- ⚡ Fast Real-time Processing

---

# 🛠 Requirements

- Python **3.11.9**
- Git
- Webcam

---

# 📥 Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

Go inside the project folder:

```bash
cd YOUR_REPOSITORY
```

---

# 🐍 Step 2: Verify Python Version

Check available Python versions:

```bash
py -0
```

or

```bash
py --list
```

You should see something similar to:

```
 -V:3.11 * Python 3.11.9
```

---

# 📦 Step 3: Create Virtual Environment (Python 3.11)

Create a virtual environment using Python **3.11**:

```bash
py -3.11 -m venv venv
```

---

# ▶️ Step 4: Activate the Virtual Environment

### Windows (Command Prompt)

```bash
venv\Scripts\activate
```

### Windows (PowerShell)

```powershell
venv\Scripts\Activate.ps1
```

### Git Bash

```bash
source venv/Scripts/activate
```

After activation, your terminal should look like:

```
(venv) C:\YourProject>
```

---

# ⬆️ Step 5: Upgrade pip

```bash
python -m pip install --upgrade pip
```

---

# 📚 Step 6: Install All Required Libraries

Install every dependency listed in **requirements.txt** with a single command:

```bash
pip install -r requirements.txt
```

This will install:

- OpenCV
- MediaPipe
- DeepFace
- TensorFlow
- tf-keras
- protobuf
- numpy

---

# ▶️ Step 7: Run the Application

```bash
python app.py
```

The webcam window will open automatically.

---

# ❌ Exit the Application

Press:

```
Q
```

to close the application.

---

# 📂 Project Structure

```
AI-Camera/
│
├── app.py
├── requirements.txt
├── README.md
└── venv/
```

---

# 🧰 Troubleshooting

## MediaPipe or TensorFlow Installation Error

Make sure you are using **Python 3.11.9**.

Check your version:

```bash
python --version
```

Expected output:

```
Python 3.11.9
```

---

## Virtual Environment Not Activating

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate again:

```powershell
venv\Scripts\Activate.ps1
```

---

## Webcam Not Opening

- Ensure no other application is using the webcam.
- Verify your webcam permissions are enabled.
- Restart the application.

---

# 📄 Requirements

The project uses the following package versions:

```
opencv-python==4.11.0.86
mediapipe==0.10.14
deepface==0.0.93
tensorflow==2.16.1
tf-keras==2.16.0
protobuf==4.25.3
numpy==1.26.4
```

---

# 👨‍💻 Developed With

- Python 3.11.9
- OpenCV
- MediaPipe
- DeepFace
- TensorFlow

---

# ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub.

Happy Coding! 🚀