original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
only_even = []
squared = []
even_or_odd = []

for number in original:
    if number % 2 == 0:
        only_even.append(number)

print(only_even)

for number in only_even:
    number = number * number
    squared.append(number)

print(squared)

for number in original:
    if number % 2 == 0:
        even_or_odd.append("even")
    else :
        even_or_odd.append("odd")

print(even_or_odd)