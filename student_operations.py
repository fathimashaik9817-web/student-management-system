from file_handler import save_students

def add_student(students):
    student_id=input("enter student ID:").strip()
    if not student_id:
        print("Student ID cannot be empty!")
        return
    name=input("enter name:").strip()
    if not name:
        print("name cannot be empty!")
        return
    age=input("enter age:")
    if not age.isdigit():
        print("Invalid age!")
        return
    age=int(age)
    if age<=0 or age>100:
        print("Please enter a valid age between 1 and 100.")
        return
    course=input("enter course:").strip()
    if not course:
        print("course cannot be empty!")
        return
    found=False

    for student in students:
        if student["ID"]==student_id:
            found==True
            break
    if found:
         print("student ID already exists!")
    else:
         student={
            "ID":student_id,
            "Name":name,
            "Age":age,
            "Course":course
         }
    students.append(student)

    save_students(students)
    print("student added successfully!")

def view_students(students):
   if len(students)==0:
      print("No students found.")
   else:
      print("\nstudent records")
      for student in students:
         print("ID:",student["ID"])
         print("Name:",student["Name"])
         print("Age:",student["Age"])
         print("Course:",student["Course"])
         print("_"*30)

def search_students(students):
    search_id=input("enter Student ID  to search:")
    found=False
   
    for student in students:
        if student["ID"]==search_id:
          print("\nstudent found!")
          print("ID:",student["ID"])
          print("Name:",student["Name"])
          print("Age:",student["Age"])
          print("Course:",student["Course"])
          found=True
          break
    if not found:
          print("student not found.")

def update_students(students):
    update_id=input("enter student ID to update:")
    found=False
   
    for student in students:
       if student["ID"]==update_id:
           new_name=input("enter new name:")
           new_age=input("enter new age:")
           new_course=input("enter new course:")
           if not new_age.isdigit():
              print("Invalid age!")
              return
           student["Name"]=new_name
           student["Age"]=new_age
           student["Course"]=new_course
           print("student updated successfully!") 
           found==True
           break
       if found:
            save_students(students)
            print("student updated successfully!")
       else:
            print("student not found.")

def delete_students(students):
     delete_id = input("Enter student ID to delete:")
     found = False

     for student in students:
        if student["ID"] == delete_id:
          students.remove(student)
          found = True
          break

        if found:
            save_students(students)
            print("Student deleted successfully!")

     else:
        print("Student not found.")
