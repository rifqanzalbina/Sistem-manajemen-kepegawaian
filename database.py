import sqlite3

def create_database():
    conn = sqlite3.connect('employee.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id TEXT PRIMARY KEY,
            name TEXT,
            position TEXT,
            salary TEXT,
            address TEXT,
            phone TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_employee(id, name, position, salary, address="", phone=""):
    conn = sqlite3.connect('employee.db')
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO employees VALUES (?,?,?,?,?,?)", (id, name, position, salary, address, phone))
        conn.commit()
    except sqlite3.IntegrityError:
        raise Exception("ID Pegawai sudah ada")
    finally:
        conn.close()

def update_employee(id, name, position, salary, address, phone):
    conn = sqlite3.connect('employee.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE employees SET name=?, position=?, salary=?, address=?, phone=? WHERE id=?", (name, position, salary, address, phone, id))
    conn.commit()
    conn.close()

def delete_employee(id):
    conn = sqlite3.connect('employee.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employees WHERE id=?", (id,))
    conn.commit()
    conn.close()

def fetch_all_employees():
    conn = sqlite3.connect('employee.db')
    cursor = conn.cursor()
    result = cursor.execute("SELECT * FROM employees")
    employees = result.fetchall()
    conn.close()
    return employees

def search_employees(query):
    conn = sqlite3.connect('employee.db')
    cursor = conn.cursor()
    result = cursor.execute("SELECT * FROM employees WHERE id LIKE ? OR name LIKE ? OR position LIKE ?", 
                            (f'%{query}%', f'%{query}%', f'%{query}%'))
    employees = result.fetchall()
    conn.close()
    return employees

def fetch_employee_by_id(id):
    conn = sqlite3.connect('employee.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees WHERE id=?", (id,))
    employee = cursor.fetchone()
    conn.close()
    return employee