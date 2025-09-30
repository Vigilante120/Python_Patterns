import json
from datetime import datetime, date
from decimal import Decimal

# BASIC JSON OPERATIONS 
#  1. Python to JSON (Serialization)

python_dict = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "is_student": False,
    "courses": ["Python", "JavaScript", "SQL"]
}

# converting py dict to json string 
json_string = json.dumps(python_dict)
print("Python to JSON:")
print(json_string)
print(type(json_string))

# note in the output python dict is in False and 
# after conversion to json its false 

# 2. Json to Python (Desirialization)
json_data = '{"name": "Jane Smith", "age": 25, "skills": ["React", "Node.js"]}'
python_obj = json.loads(json_data)
print("\nJSON to Python:")
print(python_obj)
print(type(python_obj))

# 3. Pretty printing JSON
print("\nPretty Json:")
pretty_json = json.dumps(python_dict, indent=4)
print(pretty_json)


# PART 2: FILE OPERATIONS

# Sample data
students = [
    {"id": 1, "name": "Alice", "grades": [85, 92, 78]},
    {"id": 2, "name": "Bob", "grades": [91, 87, 93]},
    {"id": 3, "name": "Charlie", "grades": [76, 81, 85]}
]

# 1. Writing JSON to file 
with open("students.json", 'w') as file:
    json.dump(students, file, indent=4)
print("Data Written Inside the file")

# 2. Reading JSON to file
with open("students.json", 'r') as file:
    loaded_studs = json.load(file)
print("\nFile Loaded")
for student in loaded_studs:
    avg_grade = sum(student['grades']) / len(student['grades'])
    print(f"{student['name']}: {avg_grade:.1f}")

# 3. Append to existing JSON file (read, modify, write)

try:
    with open("students.json", "r") as file:
        data = json.load(file)
    
    # adding new student now 
    new_student = {
        "id": 4,
        "name": "Nishant",
        "grades": [75, 85, 95]
    }
    data.append(new_student)

    with open('students.json', 'w') as file:
        json.dump(data, file, indent=4)
    print("new student added.")

except FileNotFoundError:
    print("File Not Found")

# adding one more student 

try: 
    with open("students.json", 'r') as file:
        data = json.load(file)
    
    # adding new student
    new_student = {
        "id": 5,
        "name": "Mehul",
        "grades": [75,89,99]
    }
    # why data is first because we have to add data
    # in the data variable ++ , so 
    data.append(new_student)
    with open("students.json", 'w') as file:
        json.dump(data, file,indent=4)

    print("New Student Added")

except FileNotFoundError:
    print("File Not Found")


# Advanced JSON Handling

# Custom Json Encoder for special tyes
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, date):
            return obj.isoformat()
        elif isinstance(obj, Decimal):
            return float(obj)
        elif isinstance(obj, set):
            return list(obj)
        return super().default(obj)


# Testing custom encoders
data_with_special_types = {
    "timestamp": datetime.now(),
    "birth_date": date(1990, 5, 15),
    "price": Decimal('19.99'),
    "tags": {"python", "json", "tutorial"}
}

custom_json = json.dumps(data_with_special_types,
                         cls=CustomJSONEncoder, indent=2)
print("Custom JSON with special types")
print(custom_json)

# 2. JSON Schema Validation (manual)

def validate_user_schema(data):
    required_fields = ["name", "email", "age"]

    if not isinstance(data, dict):
        return False, "Data Must be Dictionary"
    
    for field in required_fields:
        if field not in data:
            return False, f"Missing Required Field: {field}"
        
    if not isinstance(data["age"], int) or data["age"] < 0:
        return False, "Age must be a positive integer"
    
    if "@" not in data["email"]:
        return False, "This is Not a Valid Email Format"
    
    return True, "Valid"

# test validation 
user_data = {
    "name": "Nishant",
    "email": "test@mail.com",
    "age": 25}
is_valid, message = validate_user_schema(user_data)
print(f"\n validation result: {is_valid}, {message}")

# 3 Nested JSON manipulation 
nested_data = {
    "company": "AI_INFOSA",
    "departments": {
        "engineering": {
            "employees": [
                {
                    "name": "nishant", "role": "junior dev", "salary": 999999
                },
                {
                    "name": "praful", "role": "senior dev", "salary": 999999
                }
                
            ],
            "budget": 1000000
        },
        "marketing": {
            "employees": [
                {
                    "name": "Ram",
                    "role": "Manager",
                    "salary": 85000
                }
            ],
            "budget": 200000
        }
    }
}
 
# Deep Access and modification 
def get_nested_value(data, keys):
    for key in keys.split('.'):
        if isinstance(data, dict) and key in data:
            data = data[key]
        else:
            return None
    return data

# get all engineering employees
# Get all engineering employees
eng_employees = get_nested_value(nested_data, "departments.engineering.employees")
print(f"\nEngineering employees: {len(eng_employees)}")

# Calculate total company salary
total_salary = 0
for dept_name, dept_data in nested_data["departments"].items():
    for employee in dept_data["employees"]:
        total_salary += employee["salary"]
print(f"Total Company Salary: ${total_salary:,}")