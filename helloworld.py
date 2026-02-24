"""
=====================================
PYTHON LESSON 1: VARIABLES & DATA TYPES
=====================================
Purpose: Learn the building blocks of data work
Real-world use: Storing and manipulating data
"""

# ===== CONCEPT 1: VARIABLES =====
# Variables are containers that store data
# Think of them as labeled boxes

# Integers (whole numbers) - used in data counting, IDs
age = 21
salary = 500000  # Your future salary in rupees!
employees = 150

print("=== INTEGERS ===")
print(f"Age: {age}")
print(f"Salary: {salary}")
print(f"Total Employees: {employees}")

# ===== CONCEPT 2: FLOATS (Decimal numbers) =====
# Used for precise measurements, percentages, prices

price = 99.99  # Price of your future watch!
height = 5.9
growth_rate = 7.5  # percentage

print("\n=== FLOATS ===")
print(f"Watch Price: ${price}")
print(f"Height: {height} feet")
print(f"Growth Rate: {growth_rate}%")

# ===== CONCEPT 3: STRINGS (Text) =====
# Used for names, descriptions, categories

name = "Omkar"
city = "India"
job_title = "Data Analyst"

print("\n=== STRINGS ===")
print(f"Name: {name}")
print(f"City: {city}")
print(f"Job: {job_title}")

# ===== CONCEPT 4: BOOLEANS (True/False) =====
# Used for conditions, yes/no questions

is_student = True
has_laptop = True
has_car = False  # Yet! You'll get one soon!

print("\n=== BOOLEANS ===")
print(f"Is Student: {is_student}")
print(f"Has Laptop: {has_laptop}")
print(f"Has Car: {has_car}")

# ===== REAL WORLD EXAMPLE: Employee Data =====
print("\n=== EMPLOYEE DATA (REAL WORLD) ===")

employee_name = "Omkar"
employee_age = 21
employee_salary = 500000
employee_department = "Data Analytics"
is_active = True
performance_score = 4.8

print(f"Name: {employee_name}")
print(f"Age: {employee_age}")
print(f"Salary: ₹{employee_salary}")
print(f"Department: {employee_department}")
print(f"Active: {is_active}")
print(f"Performance: {performance_score}/5")

# ===== MATHEMATICAL OPERATIONS (Important for data work!) =====
print("\n=== MATH OPERATIONS ===")

# Addition
new_salary = employee_salary + 100000
print(f"Salary after raise: ₹{new_salary}")

# Percentage increase
bonus = employee_salary * 0.10  # 10% bonus
print(f"Annual Bonus: ₹{bonus}")

# Years until you can buy a car
car_price = 1500000
years_needed = car_price / (bonus * 12)
print(f"Months to save for car: {years_needed}")

# ===== STRING OPERATIONS =====
print("\n=== STRING OPERATIONS ===")

full_message = f"Hi, I am {name} and I am {age} years old"
print(full_message)

# Length of string
print(f"Length of name: {len(name)}")

# String indexing
print(f"First letter of name: {name[0]}")
print(f"Last letter of name: {name[-1]}")

# String slicing (substring)
print(f"First 3 letters: {name[0:3]}")

# ===== CHECKING DATA TYPES =====
print("\n=== DATA TYPES ===")
print(f"Type of age: {type(age)}")
print(f"Type of salary: {type(employee_salary)}")
print(f"Type of height: {type(height)}")
print(f"Type of name: {type(name)}")
print(f"Type of is_active: {type(is_active)}")

print("\n" + "="*50)
print("LESSON 1 COMPLETE!")
print("="*50)


