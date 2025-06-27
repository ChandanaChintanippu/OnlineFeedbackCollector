# 📝 Online Feedback Collector with Admin Dashboard

A full-stack web application to collect and manage user feedback with a modern interface and an insightful admin dashboard. Built using **Flask**, **SQLite**, **Bootstrap**, and **Chart.js**.

---

## 🚀 Features

### 🧑 User Interface
- Clean and responsive feedback form
- Fields: Name, Email, Rating (1–5), Comments

### 🛡️ Admin Dashboard
- Secure admin login system
- View all submitted feedback
- Display total responses and average rating
- Visualize feedback trends using pie chart
- Export all feedback to CSV with one click

---

## ⚙️ Tech Stack

| Layer     | Technology                          |
|-----------|--------------------------------------|
| Frontend  | HTML, CSS, JavaScript, Bootstrap     |
| Backend   | Python, Flask                        |
| Database  | SQLite                               |
| Charts    | Chart.js                             |
| Export    | CSV download                         |

---

## 🔐 Admin Login Credentials

```txt
Username: admin  
Password: admin123
```

You can modify these credentials in the `app.py` file.

---

## 📦 Installation & Running

### 1️⃣ Clone the repository

```bash
git clone https://github.com/ChandanaChintanippu/OnlineFeedbackCollector.git
cd OnlineFeedbackCollector
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the application

```bash
python app.py
```

Then open your browser and visit:  
🌐 http://localhost:5000

---

## 📤 Export Feedback

Access the **admin dashboard** and click `⬇ Export as CSV` to download all responses in `.csv` format.

---

## 📌 Future Enhancements

- 🔐 Password hashing using Flask-Bcrypt  
- 👤 Admin registration functionality  
- 📄 Pagination and sorting for feedback table  
- 🔍 Search and filtering by rating or keyword  
- 🚀 One-click deployment on PythonAnywhere or Render  

---

## 👩‍💻 Developed By

**Chintanippu Chandana**  
🎓 Python Development Internship Project – June 2025  
🔗 GitHub: [@ChandanaChintanippu](https://github.com/ChandanaChintanippu)
