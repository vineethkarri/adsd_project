# application.py

import sqlite3
from bottle import Bottle, route, run, template, request

app = Bottle()

# Connect to SQLite database
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

# Create a table named 'employees_table'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees_table (
        employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_name TEXT,
        department_id INTEGER,
        FOREIGN KEY (department_id) REFERENCES departments_table(department_id)
    )
''')

# Create a table named 'departments_table'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS departments_table (
        department_id INTEGER PRIMARY KEY AUTOINCREMENT,
        department_name TEXT
    )
''')

# Save (commit) the changes
conn.commit()


@app.route('/')
def index():
    # Fetch data from both tables using a JOIN
    cursor.execute('''
        SELECT employees_table.employee_id, employees_table.employee_name,
               departments_table.department_name
        FROM employees_table
        LEFT JOIN departments_table ON employees_table.department_id = departments_table.department_id
    ''')
    data = cursor.fetchall()

    # Fetch all departments for dropdown
    cursor.execute('SELECT * FROM departments_table')
    departments = cursor.fetchall()

    return template('index', data=data, departments=departments)


@app.route('/add_employee', method='POST')
def add_employee():
    # Insert data into 'employees_table'
    employee_name = request.forms.get('employee_name')
    department_id = request.forms.get('department_id')
    cursor.execute('INSERT INTO employees_table (employee_name, department_id) VALUES (?, ?)', (employee_name, department_id))
    conn.commit()

    return index()


@app.route('/add_department', method='POST')
def add_department():
    # Insert data into 'departments_table'
    department_name = request.forms.get('department_name')
    cursor.execute('INSERT INTO departments_table (department_name) VALUES (?)', (department_name,))
    conn.commit()

    return index()


# ...

# ...

@app.route('/update_employee/<employee_id>', method='GET')
def update_employee(employee_id):
    # Fetch data for updating employee
    cursor.execute('SELECT * FROM employees_table WHERE employee_id = ?', (employee_id,))
    employee_data = cursor.fetchone()

    # Fetch all departments for dropdown
    cursor.execute('SELECT * FROM departments_table')
    departments = cursor.fetchall()

    return template('update_employee', employee_data=employee_data, departments=departments)

# ...

# ...


@app.route('/update_department/<department_id>', method='POST')
def update_department(department_id):
    # Update data in 'departments_table'
    new_name = request.forms.get('new_name')
    cursor.execute('UPDATE departments_table SET department_name = ? WHERE department_id = ?', (new_name, department_id))
    conn.commit()

    return index()


@app.route('/delete_employee/<employee_id>', method='GET')
def delete_employee(employee_id):
    # Delete data from 'employees_table'
    cursor.execute('DELETE FROM employees_table WHERE employee_id = ?', (employee_id,))
    conn.commit()

    return index()


@app.route('/delete_department/<department_id>', method='GET')
def delete_department(department_id):
    # Delete data from 'departments_table'
    cursor.execute('DELETE FROM departments_table WHERE department_id = ?', (department_id,))
    conn.commit()

    return index()


if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True)
