# 📝 Task Manager API (Django + JWT)

I was surfing through the [Django Docs](https://docs.djangoproject.com/) and honestly got a bit bored 🧷‍♂️, so instead of just reading, I decided to build something practical.
This is a simple **Task Manager API** built with **Django REST Framework** and **JWT Authentication**.

---

## 🚀 Features

* User Registration & Login (JWT-based authentication using `djangorestframework-simplejwt`)
* Create, Read, Update, Delete (CRUD) tasks
* Each task is **user-specific** (you only see your own tasks)
* Authentication required for task endpoints
* Clean REST API ready for frontend or mobile integration

---

## ⚙️ Tech Stack

* **Backend:** Django, Django REST Framework
* **Auth:** JWT (via `djangorestframework-simplejwt`)
* **Database:** SQLite (default, can be swapped for PostgreSQL/MySQL)
* **Tools:** Postman for testing

---

## 📂 Project Structure

```
taskmanager/
│
├── tasks/                # App for tasks API
│   ├── models.py         # Task model
│   ├── serializers.py    # Serializers for Task & User
│   ├── views.py          # Task CRUD APIs
│   ├── auth_views.py     # User registration & auth
│   └── urls.py           # Endpoints for tasks & auth
│
├── taskmanager/          # Project settings & config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── db.sqlite3            # Local database
```

---

## 🔑 Authentication

This project uses **JWT tokens**.

### Register

`POST /api/register/`

```json
{
  "username": "john",
  "email": "john@example.com",
  "password": "mypassword"
}
```

### Get Token

`POST /api/token/`

```json
{
  "username": "john",
  "password": "mypassword"
}
```

Response:

```json
{
  "refresh": "your_refresh_token",
  "access": "your_access_token"
}
```

### Use Token

Add this to **Authorization header**:

```
Authorization: Bearer <access_token>
```

---

## 📌 Tasks API

### Get All Tasks

`GET /tasks/`

### Create Task

`POST /tasks/`

```json
{
  "title": "Finish Django Project",
  "description": "Complete the task manager with JWT auth",
  "completed": false
}
```

### Get Task by ID

`GET /tasks/<id>/`

### Update Task

`PUT /tasks/<id>/`

### Delete Task

`DELETE /tasks/<id>/`

---

## 🛠️ Installation & Run Locally

```bash
git clone https://github.com/your-username/task-manager-django.git
cd task-manager-django
python -m venv venv
source venv/bin/activate   # (Windows: venv\Scripts\activate)
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
```

---

## ✨ Why I Built This

Instead of just reading Django docs, I wanted to **get my hands dirty**.
This project helped me understand:

* How DRF handles authentication
* How to restrict tasks per user
* How JWT works with Django REST Framework

So yeah — boredom turned into a small, useful project 😊

---

## 🔮 Future Improvements

* Add task categories / deadlines
* Add refresh token rotation
* Deploy on Heroku or Railway
* Build a React frontend for it

---

## 📜 License

MIT License
