def reverse_string(string):
	string = string[::-1]
	return string

def all_upper(string):
	string = string.upper()
	return string

def count_vowel(string):
    vowels = "aeiouyAEIOUY"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

def circle_area(ray):
	area = 3.14 * ray * ray
	return area

def factorial(number):           
	result = 1
	for i in range(1,number + 1):
		result = result * i
	return result

def is_prime(number):
    if number < 2:
        return f"{number} is not prime"
    for i in range(2, number):
        if number % i == 0:
            return f"{number} is not prime"  
    return f"{number} is prime"

def sum(first_number, second_number):
	return first_number + second_number

def multiply(first_number, second_number):
    return first_number * second_number

def subtract(first_number, second_number):
    return first_number - second_number

def divide(first_number, second_number):
    if second_number == 0:
        return "Error: Cannot divide by zero!"
    return first_number / second_number