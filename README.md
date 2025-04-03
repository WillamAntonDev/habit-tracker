# 🧠 Habit Tracker

A simple, elegant Django app to help you build better habits — one day at a time.

---

## 🚀 Features

- ✅ User registration & login
- 📋 Add habits with optional descriptions
- 🔁 Daily habit reset logic
- 📆 Track completion per day
- ✏️ Edit and delete habits
- 🎨 Clean UI with responsive styling
- 🧠 Organized codebase (views, models, templates, static)

---

## 🛠️ Tech Stack

- Python 3.11
- Django 5.1
- SQLite (default)
- HTML + CSS (custom styling)
- Django Templates
- FontAwesome (optional icons)

---

## 🔧 Setup Instructions

1. **Clone the repo**

```bash
git clone https://github.com/WillamAntonDev/habit-tracker.git
cd habit-tracker
```

2. **Create and activate a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Apply migrations**

```bash
python manage.py migrate
```

5. **Run the server**

```bash
python manage.py runserver
```

---

## 👤 Admin Access (optional)

To create a superuser for admin access:

```bash
python manage.py createsuperuser
```

Then visit: `http://127.0.0.1:8000/admin/`

---

## ✨ Customization Ideas

- Add **categories** (e.g., Fitness, Work, Personal)
- Add **progress charts** with Chart.js
- Email or SMS reminders
- Mobile responsiveness tweaks

---

## 📸 Screenshots

_Add screenshots here to showcase UI_

---

## 📜 License

MIT © William Anton

---

## 🙌 Acknowledgments

Created by William Anton — a personal project from my coding bootcamp to build consistent daily habits using Django.

