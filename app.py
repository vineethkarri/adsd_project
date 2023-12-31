from bottle import route, post, run, template, redirect, request
import database

# Call set_up_database to create tables and insert sample data in the database 
database.set_up_database()

@route("/")
def get_index():
    redirect("/list")

@route("/list")
def get_list():
    # we are fetching data from both tables using a JOIN
    items = database.get_courses_and_students()
    return template("list.tpl", data=items)

@route("/search")
def search():
    department = request.query.get("department", "")
    search_results = database.search_by_department(department)
    return template("list.tpl", data=search_results)

@route("/add")
def get_add():
    return template("add_course_student.tpl")

@post("/add")
def post_add():
    student_name = request.forms.get("student_name")
    course_name = request.forms.get("course_name")
    department = request.forms.get("department")
    credits = request.forms.get("credits")

    # Add course and student in the database
    database.add_course_and_student(student_name, course_name, department, credits)
    redirect("/list")

@route("/update/<id>")
def get_update(id):
    items = database.get_courses_and_students(id)
    return template("update_course_student.tpl", item=items[0])

@post("/update")
def post_update():
    student_name = request.forms.get("student_name")
    course_name = request.forms.get("course_name")
    department = request.forms.get("department")
    credits = request.forms.get("credits")
    id = request.forms.get("id")

    # Update course and student in the database
    database.update_course_and_student(id, student_name, course_name, department, credits)
    redirect("/list")

@route("/delete/<id>")
def get_delete(id):
    # Delete course and related students you want to do 
    database.delete_course_and_student(id)
    redirect("/list")

run(host='localhost', port=8080)
