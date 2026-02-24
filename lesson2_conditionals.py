"""
=====================================
PYTHON LESSON 2: CONDITIONALS & DECISION MAKING
=====================================
Purpose: Learn how to make decisions in code
Real-world use: Filter data, validate inputs, make business decisions
"""

print("="*60)
print("LESSON 2: CONDITIONALS & DECISION MAKING")
print("="*60)

# ===== CONCEPT 1: COMPARISON OPERATORS =====
print("\n### COMPARISON OPERATORS ###")
print("Used to compare two values and get True/False\n")

age = 21
voting_age = 18

# Greater than (>)
print(f"age > voting_age: {age > voting_age}")  # True - you can vote!

# Less than (<)
salary = 500000
min_salary = 300000
print(f"salary < min_salary: {salary < min_salary}")  # False - you earn enough!

# Equal to (==)
my_name = "Omkar"
print(f"my_name == 'Omkar': {my_name == 'Omkar'}")  # True

# Not equal to (!=)
department = "Data Analytics"
print(f"department != 'HR': {department != 'HR'}")  # True

# Greater than or equal (>=)
experience_years = 3
print(f"experience_years >= 2: {experience_years >= 2}")  # True

# Less than or equal (<=)
print(f"age <= 25: {age <= 25}")  # True

# ===== CONCEPT 2: IF STATEMENT =====
print("\n\n### IF STATEMENT (One-way decision) ###\n")

age = 21
if age >= 18:
    print(f"✓ You are {age} years old - YOU CAN VOTE!")

# Another example
salary = 500000
if salary > 400000:
    print(f"✓ Your salary ₹{salary} is EXCELLENT!")

# ===== CONCEPT 3: IF/ELSE STATEMENT =====
print("\n\n### IF/ELSE STATEMENT (Two-way decision) ###\n")

has_car = False

if has_car:
    print("✓ You own a car!")
else:
    print("✗ You don't have a car yet. But soon you will!")

# Data validation example
user_age = 16

if user_age >= 18:
    print(f"Age {user_age}: Eligible to apply for job")
else:
    print(f"Age {user_age}: Not eligible yet. Wait {18 - user_age} more years!")

# ===== CONCEPT 4: IF/ELIF/ELSE STATEMENT =====
print("\n\n### IF/ELIF/ELSE STATEMENT (Multiple decisions) ###\n")

# Grade assignment based on marks
marks = 85

if marks >= 90:
    grade = "A"
    print("Marks: {marks} → Grade: {grade} ⭐⭐⭐⭐⭐ (Outstanding!)")
elif marks >= 75:
    grade = "B"
    print("Marks: {marks} → Grade: {grade} ⭐⭐⭐⭐ (Good!)")
elif marks >= 60:
    grade = "C"
    print("Marks: {marks} → Grade: {grade} ⭐⭐⭐ (Pass!)")
elif marks >= 50:
    grade = "D"
    print("Marks: {marks} → Grade: {grade} ⭐⭐ (Barely Pass!)")
else:
    grade = "F"
    print("Marks: {marks} → Grade: {grade} ✗ (Fail - Need to study more!)")

# ===== REAL WORLD: SALARY BRACKET DECISION =====
print("\n\n### REAL WORLD: Salary Bracket & Tax Calculation ###\n")

employee_salary = 500000

if employee_salary >= 1000000:
    tax_rate = 0.30  # 30% tax
    category = "High Earner"
elif employee_salary >= 500000:
    tax_rate = 0.20  # 20% tax
    category = "Mid-High Earner"
elif employee_salary >= 250000:
    tax_rate = 0.10  # 10% tax
    category = "Mid Earner"
else:
    tax_rate = 0.05  # 5% tax
    category = "Entry Level"

tax_amount = employee_salary * tax_rate
net_salary = employee_salary - tax_amount

print(f"Gross Salary: ₹{employee_salary}")
print(f"Category: {category}")
print(f"Tax Rate: {tax_rate*100}%")
print(f"Tax Amount: ₹{tax_amount}")
print(f"Net Salary: ₹{net_salary}")

# ===== CONCEPT 5: LOGICAL OPERATORS =====
print("\n\n### LOGICAL OPERATORS (AND, OR, NOT) ###\n")

# AND operator - Both conditions must be True
age = 21
has_license = True

if age >= 18 and has_license:
    print("✓ You can drive!")
else:
    print("✗ You cannot drive")

# OR operator - At least one condition must be True
has_cash = False
has_credit_card = True

if has_cash or has_credit_card:
    print("✓ You can buy stuff!")
else:
    print("✗ You can't buy anything")

# NOT operator - Reverses the condition
is_student = False

if not is_student:
    print("✓ You are working! Earning money!")
else:
    print("✗ You are still studying")

# ===== COMPLEX REAL WORLD EXAMPLE: Loan Approval =====
print("\n\n### COMPLEX EXAMPLE: Bank Loan Approval ###\n")

# Applicant details
name = "Omkar"
salary = 500000
credit_score = 750
experience_years = 3
loan_amount = 1000000

# Approval criteria
can_approve = False

if salary >= 300000 and credit_score >= 700 and experience_years >= 2:
    if loan_amount <= salary * 2:
        can_approve = True

if can_approve:
    print(f"✓ LOAN APPROVED for {name}!")
    print(f"  Salary: ₹{salary}")
    print(f"  Credit Score: {credit_score}")
    print(f"  Experience: {experience_years} years")
    print(f"  Approved Loan: ₹{loan_amount}")
else:
    print(f"✗ LOAN REJECTED for {name}")
    if salary < 300000:
        print(f"  Reason: Salary too low (need ₹300,000+)")
    if credit_score < 700:
        print(f"  Reason: Credit score too low (need 700+)")
    if experience_years < 2:
        print(f"  Reason: Not enough experience (need 2+ years)")

# ===== DATA VALIDATION EXAMPLE =====
print("\n\n### DATA VALIDATION: Employee Check ###\n")

def validate_employee(name, age, salary):
    """Check if employee data is valid"""
    
    if not name or len(name) < 2:
        print("✗ Invalid name!")
        return False
    
    if age < 18 or age > 65:
        print(f"✗ Invalid age {age}! (Must be 18-65)")
        return False
    
    if salary < 0 or salary > 10000000:
        print(f"✗ Invalid salary {salary}!")
        return False
    
    print(f"✓ Valid employee: {name}, Age: {age}, Salary: ₹{salary}")
    return True

print("Test 1:")
validate_employee("Omkar", 21, 500000)

print("\nTest 2:")
validate_employee("O", 16, 500000)

print("\nTest 3:")
validate_employee("Rajesh", 30, -50000)

# ===== PRACTICE: YOUR FIRST DECISION =====
print("\n\n### YOUR TURN: Car Purchase Decision ###\n")

monthly_salary = 500000 / 12  # Monthly salary
car_price = 1500000
down_payment_available = 300000
monthly_emi = 25000

print(f"Monthly Salary: ₹{monthly_salary:.0f}")
print(f"Car Price: ₹{car_price}")
print(f"Down Payment Available: ₹{down_payment_available}")
print(f"Monthly EMI: ₹{monthly_emi}")

if down_payment_available >= car_price * 0.2 and monthly_emi <= monthly_salary * 0.3:
    print("\n✓ YOU CAN BUY THE CAR!")
    print("  - Down payment is sufficient (20% of price)")
    print("  - EMI won't exceed 30% of monthly salary")
else:
    print("\n✗ Not ready yet. Keep saving!")

print("\n" + "="*60)
print("LESSON 2 COMPLETE! You can now make decisions in code!")
print("="*60)