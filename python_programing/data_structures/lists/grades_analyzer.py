def calculate_average(grade_list):
    sum = 0
    count = 0
    for grade in grades:
        sum += grade
        count += 1
    return sum / count

grades = [85, 90, 78, 92, 88, 76, 95, 89]

avg = calculate_average(grades)

print(f"Average grade is {avg:.1f}")

print(f"Max grade is {max(grades)}")

print(f"Min grade is {min(grades)}")

grades.insert(4, 123)

above_88_counter = 0

for grade in grades:
    if grade > 88:
        above_88_counter += 1

print(f"Theres {above_88_counter} students with a grade above 88")
