from studentmanager import StudentManager

def main():
    manager = StudentManager()
    
    
    manager.load_from_csv("students.csv")
    
    while True:
        print("\n" + "="*50)
        print("STUDENT GRADES MANAGEMENT SYSTEM")
        print("="*50)
        print("1. Display all students")
        print("2. Display student details")
        print("3. Add new student")
        print("4. Add grade to student")
        print("5. Remove student")
        print("6. Display class statistics")
        print("7. Sort students by name")
        print("8. Sort students by average")
        print("9. Save to file")
        print("0. Exit")
        print("-"*50)
        
        choice = input("Enter your choice (0-9): ").strip()
        
        if choice == "1":
            
            manager.display_all_students()
            
        elif choice == "2":
        
            try:
                student_id = int(input("Enter student ID: "))
                manager.display_student_details(student_id)
            except ValueError:
                print("Error: Please enter a valid student ID (numbers only)")
            except Exception as e:
                print(f"Error: {e}")
                
        elif choice == "3":
            
            try:
                student_id = int(input("Enter student ID: "))
                student_name = input("Enter student name: ").strip()
                
                
                from student import Student
                new_student = Student(student_id, student_name)
                manager.add_student(new_student)
                print(f"Student {student_name} added successfully!")
                
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Error: {e}")
                
        elif choice == "4":
            
            try:
                student_id = int(input("Enter student ID: "))
                grade = int(input("Enter grade (4-10): "))
                manager.add_grade(student_id, grade)
                print(f"Grade {grade} added to student ID {student_id}")
                
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Error: {e}")
                
        elif choice == "5":
            
            try:
                student_id = int(input("Enter student ID to remove: "))
                manager.remove_student_by_id(student_id)
                print(f"Student ID {student_id} removed successfully!")
                
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Error: {e}")
                
        elif choice == "6":
            
            manager.display_class_statistics()
            
        elif choice == "7":
            
            sorted_students = manager.sort_by_name()
            print("\n=== STUDENTS SORTED BY NAME ===")
            for student in sorted_students:
                print(student)
                
        elif choice == "8":
            
            sorted_students = manager.sort_by_average()
            print("\n=== STUDENTS SORTED BY AVERAGE ===")
            for student in sorted_students:
                avg = student.calculate_average()
                print(f"{student.name}: {avg:.2f}")
                
        elif choice == "9":
            
            manager.save_to_csv("students.csv")
            
        elif choice == "0":
            
            save = input("Save changes before exiting? (y/n): ").lower()
            if save == 'y':
                manager.save_to_csv("students.csv")
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice! Please enter a number between 0-9.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()