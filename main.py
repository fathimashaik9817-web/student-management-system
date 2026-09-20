from file_handler import load_students 
from student_operations import (add_student, view_students, search_students, update_students, delete_students)
def main():
    students=load_students()

    while True:
      print("\n"+"="*40)
      print("  STUDENT MANAGEMENT SYSTEM")
      print("="*40)
      print("1. Add Student")
      print("2. View Students")
      print("3. Search Student")
      print("4. Update Student")
      print("5. Delete Student")
      print("6. Exit")

      choice=input("Enter your choice:")

      if choice== "1":
        add_student(students)

      elif choice=="2":
        view_students(students)

      elif choice=="3":
        search_students(students)

      elif choice=="4":
        update_students(students)

      elif choice == "5":
        delete_students(students)

      elif choice=="6":
        print("thank you!")
      break
    else:
      print("Invalid choice!")
if __name__=="__main__":
       main()