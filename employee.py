
from database import connect

# Add Employee
def add_employee(id, name, salary, age):
    db = connect()
    cursor = db.cursor()

    query = "INSERT INTO employees VALUES (%s, %s, %s, %s)"
    values = (id, name, salary, age)

    cursor.execute(query, values)
    db.commit()

    cursor.close()
    db.close()


# Remove Employee
def remove_employee(id):
    db = connect()
    cursor = db.cursor()

    query = "DELETE FROM employees WHERE id = %s"
    cursor.execute(query, (id,))

    db.commit()
    result = cursor.rowcount

    cursor.close()
    db.close()

    return result


# Update Employee
def update_employee(id, name, salary, age):
    db = connect()
    cursor = db.cursor()

    query = """
    UPDATE employees
    SET name = %s, salary = %s, age = %s
    WHERE id = %s
    """
    values = (name, salary, age, id)

    cursor.execute(query, values)
    db.commit()

    result = cursor.rowcount

    cursor.close()
    db.close()

    return result


# Get Single Employee
def get_employee(id):
    db = connect()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM employees WHERE id = %s", (id,))
    employee = cursor.fetchone()

    cursor.close()
    db.close()

    return employee


# Get All Employees
def get_all_employees():
    db = connect()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()

    cursor.close()
    db.close()

    return employees
