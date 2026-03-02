from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "supersecretkey"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ------------------ DATABASE MODEL ------------------

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(20), nullable=False, unique=True)
    name = db.Column(db.String(100), nullable=False)
    course = db.Column(db.String(100), nullable=False)
    marks = db.Column(db.Integer, nullable=False)

# ------------------ LOGIN PAGE ------------------

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == "admin" and password == "admin":
            session['admin'] = True
            return redirect('/dashboard')
        else:
            return render_template('login.html', error="Invalid Credentials")

    return render_template('login.html')

# ------------------ DASHBOARD ------------------

@app.route('/dashboard')
def dashboard():
    if 'admin' not in session:
        return redirect('/')
    students = Student.query.all()
    return render_template('dashboard.html', students=students)

# ------------------ LOGOUT ------------------

@app.route('/logout')
def logout():
    session.pop('admin', None)
    return redirect('/')

# ------------------ ADD STUDENT ------------------

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if 'admin' not in session:
        return redirect('/')

    if request.method == 'POST':
        new_student = Student(
            student_id=request.form['student_id'],
            name=request.form['name'],
            course=request.form['course'],
            marks=int(request.form['marks'])
        )
        db.session.add(new_student)
        db.session.commit()
        return redirect('/dashboard')

    return render_template('add_student.html')

# ------------------ EDIT STUDENT ------------------

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    if 'admin' not in session:
        return redirect('/')

    student = Student.query.get_or_404(id)

    if request.method == 'POST':
        student.student_id = request.form['student_id']
        student.name = request.form['name']
        student.course = request.form['course']
        student.marks = int(request.form['marks'])

        db.session.commit()
        return redirect('/dashboard')

    return render_template('edit_student.html', student=student)

# ------------------ DELETE STUDENT ------------------

@app.route('/delete/<int:id>')
def delete_student(id):
    if 'admin' not in session:
        return redirect('/')

    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return redirect('/dashboard')

# ------------------ MAIN ------------------

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)