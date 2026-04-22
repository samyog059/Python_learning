# Creating a dictionary inside a dictionary
students = {
    "student1": {
        "name": "Ram",
        "age": 18,
        "grade": "A"
    },
    "student2": {
        "name": "Sita",
        "age": 17,
        "grade": "B"
    },
    "student3": {
        "name": "Hari",
        "age": 19,
        "grade": "A+"
    }
}

# Accessing data
print(students["student1"]["name"])   # Output: Ram
print(students["student2"]["grade"])  # Output: B
