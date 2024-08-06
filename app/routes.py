from flask import Blueprint, render_template, request, redirect, url_for
from .models import db, Student, Course, Teacher

main = Blueprint('main', __name__)

@main.route('/')
def index():
    total_students = Student.query.count()
    total_teachers = Teacher.query.count()
    total_courses = Course.query.count()
    return render_template('index.html', total_students=total_students, total_teachers=total_teachers, total_courses=total_courses)


@main.route('/students')
def student_list():
    try:
        students = Student.query.all()
        print(f"Fetched students: {students}")  # Debugging statement
        return render_template('student_list.html', students=students)
    except Exception as e:
        print(f"An error occurred: {e}")
        return "An error occurred", 500

@main.route('/students/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        student = Student(name=name, age=age)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('main.student_list'))
    return render_template('add_student.html')

@main.route('/courses')
def course_list():
    courses = Course.query.all()
    return render_template('course_list.html', courses=courses)

@main.route('/courses/add', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        name = request.form['name']
        code = request.form['code']
        course = Course(name=name, code=code)
        db.session.add(course)
        db.session.commit()
        return redirect(url_for('main.course_list'))
    return render_template('add_course.html')

@main.route('/teachers')
def teacher_list():
    teachers = Teacher.query.all()
    return render_template('teacher_list.html', teachers=teachers)

@main.route('/teachers/add', methods=['GET', 'POST'])
def add_teacher():
    if request.method == 'POST':
        name = request.form['name']
        subject = request.form['subject']
        teacher = Teacher(name=name, subject=subject)
        db.session.add(teacher)
        db.session.commit()
        return redirect(url_for('main.teacher_list'))
    return render_template('add_teacher.html')
