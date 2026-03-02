# Student Management System

A Flask-based web application for managing student records, including features to add, edit, and delete student data. This application uses **Flask-SQLAlchemy** for database management and is ready for deployment with **Gunicorn**. 

---

## 🚀 Features

* **Secure Admin Login**: Restrict access to student data via an admin authentication gate.
* **Student Dashboard**: View a complete list of all registered students.
* **Full CRUD Operations**:
* **Add**: Register new students with unique IDs, names, courses, and marks.
* **Edit**: Update existing student information.
* **Delete**: Remove student records from the database.


* 
**Persistent Storage**: Powered by an SQLite database. 



---

## 🛠️ Technology Stack

* 
**Backend**: Flask 3.1.2 


* 
**Database**: SQLite with Flask-SQLAlchemy 


* 
**Server**: Gunicorn 25.1.0 


* 
**Templating**: Jinja2 



---

## 📂 Project Structure

```text
├── app.py              # Main application logic and routes
├── config.py           # Configuration settings (Secret keys, DB paths)
├── database.db         # SQLite database file
├── requirements.txt    # Python dependencies
├── Procfile            # Deployment instructions for production
├── .gitignore          # Files excluded from version control
└── templates/          # HTML templates (login, dashboard, add, edit)

```

---

## ⚙️ Installation & Setup

### 1. Prerequisites

Ensure you have Python installed on your system.

### 2. Install Dependencies

Install the required packages using the `requirements.txt` file: 

```bash
pip install -r requirements.txt

```

### 3. Database Initialization

The application is configured to create the database tables automatically upon the first run. The `Student` model includes the following fields:

* `id`: Primary Key
* `student_id`: Unique Identifier
* `name`: Student Name
* `course`: Enrolled Course
* `marks`: Academic Marks

### 4. Running the App

Start the development server:

```bash
python app.py

```

The app will be accessible at `http://127.0.0.1:5000`.

---

## 🔐 Credentials

To access the dashboard and management features, use the default admin credentials:

* **Username**: `admin`
* **Password**: `admin`

---

## 🌐 Deployment

The project includes a **Procfile** for deployment on platforms like Heroku or Render. It uses Gunicorn to serve the application: 

```text
web: gunicorn app:app

```

Would you like me to generate the **HTML templates** (login, dashboard, etc.) for this application so you can have a fully functional project?
