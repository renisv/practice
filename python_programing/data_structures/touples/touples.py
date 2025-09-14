def get_student_data():
    return ("Alice", "Smith", 22, "Computer Science")

student_data = get_student_data()

first_name, last_name, age, major = student_data

print(f"{first_name} {last_name} is a {age}-year-old {major} student.")

try:
    student_data[2] = 23
except TypeError as e:
    print(f"\nError when trying to modify the tuple: {e}")
    print("This error occurs because tuples are immutable - they cannot be changed after creation.")

print("\nCreating a new tuple with updated age:")
new_student_data = student_data[:2] + (23,) + student_data[3:]
first_name, last_name, age, major = new_student_data
print(f"Updated: {first_name} {last_name} is now a {age}-year-old {major} student.")