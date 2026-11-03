students = [
    {"id": 1, "name": "Ali"},
    {"id": 2, "name": "Sara"}
]

# CREATE
def create_student(student_id, name):
    students.append({"id": student_id, "name": name})
    print("Student added successfully")

# READ
def read_students():
    for student in students:
        print(student)

# UPDATE (Bug in this function)
def update_student(student_id, new_name):
    for student in students:
        if student["id"] == student_id:
            student["name"] == new_name
            print("Student updated")
            return
    print("Student not found")

# DELETE
def delete_student(student_id):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student deleted")
            return
    print("Student not found")

read_students()
update_student(1, "Ahmed")
read_students()
