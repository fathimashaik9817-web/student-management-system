def load_students():
    students=[]
    try:
      with open("students.txt","r")as file:
        lines=file.readlines()
    except FileNotFoundError:
       return[]
    for line in lines:
        student_id,name,age,course=line.strip().split(",")
        student={
            "ID":student_id,
            "Name":name,
            "Age":age,
            "Course":course
        }
        students.append(student)
    return students
def save_students(students):
    with open("students.txt","w") as file:
        for student in students:
            file.write(f"{student['ID']},{student['Name']},{student['Age']},{student['Course']}\n")