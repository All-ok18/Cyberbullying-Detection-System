# AI Cyberbullying Detection System

## Project Description

This project is an AI-powered Cyberbullying Detection Web Application developed using:

- Machine Learning
- Flask
- MySQL
- HTML
- CSS
- JavaScript

The system detects whether a sentence contains cyberbullying or not.

---

# Technologies Used

Frontend:
- HTML
- CSS
- JavaScript

Backend:
- Flask (Python)

Machine Learning:
- TF-IDF Vectorizer
- Logistic Regression

Database:
- MySQL

---

# Folder Structure

cyberbullying-project-main/

│
├── backend/
│   ├── app.py
│   ├── train_model.py
│   ├── model.pkl
│   ├── vectorizer.pkl
│   ├── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
│   ├── style.css
│   ├── script.js
│
├── Dataset.json
├── README.md

---

# Software Requirements

Install:

1. Python 3.11
2. VS Code
3. MySQL
4. Live Server Extension (VS Code)

---

# Step 1 - Extract ZIP File

Extract the project ZIP file.

Open project folder in VS Code.

---

# Step 2 - Install Python Libraries

Open terminal in VS Code.

Run:

```bash
pip install -r backend/requirements.txt
```

---

# Step 3 - Create MySQL Database

Open MySQL Workbench or phpMyAdmin.

Run:

```sql
CREATE DATABASE cyberbullyingDB;
```

Use database:

```sql
USE cyberbullyingDB;
```

Create users table:

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100),
    password VARCHAR(100)
);
```

Create history table:

```sql
CREATE TABLE history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    text_data TEXT,
    result VARCHAR(100)
);
```

---

# Step 4 - Train ML Model

Open terminal.

Go to backend folder:

```bash
cd backend
```

Run:

```bash
python train_model.py
```

This generates:

- model.pkl
- vectorizer.pkl

---

# Step 5 - Run Backend Server

Inside backend folder run:

```bash
python app.py
```

Server runs on:

```text
http://127.0.0.1:5000
```

---

# Step 6 - Run Frontend

Open frontend folder.

Open:

```text
index.html
```

OR use Live Server extension.

---

# Application Flow

1. Signup
2. Login
3. Enter Text
4. Predict Cyberbullying
5. View Result

---

# Features

- User Authentication
- AI-based Detection
- Prediction History
- Responsive UI
- MySQL Database Integration
- Flask REST API

---

# Developed Using

- Python
- Flask
- Machine Learning
- MySQL
- HTML/CSS/JS