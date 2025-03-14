import mysql.connector
import random
import names

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Cognizant",
    port=3307
)
cursor = conn.cursor()

# tables are created.

# cursor.execute("""
# create table if not exists departments(
#     id int primary key not null auto_increment,
#     dept_name varchar(255) not null
# )
# """)

# cursor.execute("""
# create table if not exists employees(
#     id int primary key not null auto_increment,
#     name varchar(255) not null,
#     dept_id int,
#     salary int not null,
#     foreign key (dept_id) references departments(id) on delete cascade
# )
# """)

# Create departments
departments = [
    "Engineering",
    "Sales",
    "Marketing",
    "Human Resources",
    "Finance",
    "Operations",
    "Research",
    "Customer Support",
    "Legal",
    "Product Management"
]

# Insert departments
for dept in departments:
    cursor.execute("INSERT INTO departments (dept_name) VALUES (%s)", (dept,))

# Generate 100 employees

# Get department IDs
cursor.execute("SELECT id FROM departments")
dept_ids = [row[0] for row in cursor.fetchall()]

# Insert employees
for _ in range(100):
    name = names.get_full_name()
    dept_id = random.choice(dept_ids)
    salary = random.randint(40000, 150000)
    cursor.execute("""
        INSERT INTO employees (name, dept_id, salary)
        VALUES (%s, %s, %s)
    """, (name, dept_id, salary))

print("Data inserted successfully")

conn.commit()

# Verify data insertion
cursor = conn.cursor()

# Check departments
print("\nDepartments:")
cursor.execute("SELECT * FROM departments")
departments = cursor.fetchall()
for dept in departments:
    print(f"ID: {dept[0]}, Name: {dept[1]}")

# Check some employees
print("\nSample Employees:")
cursor.execute("""
    SELECT e.id, e.name, d.dept_name, e.salary 
    FROM employees e 
    JOIN departments d ON e.dept_id = d.id 
    LIMIT 5
""")
employees = cursor.fetchall()
for emp in employees:
    print(f"ID: {emp[0]}, Name: {emp[1]}, Department: {emp[2]}, Salary: ${emp[3]:,}")

cursor.close()
conn.close()