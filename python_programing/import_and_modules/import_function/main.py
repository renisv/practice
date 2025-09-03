import string_utils as su
import sys

if len(sys.argv) < 3:
    print("Usage: python main.py <number1> <number2> [--add|--multiply|--subtract|--divide]")
    exit(1)

first_num = int(sys.argv[1])
second_num = int(sys.argv[2])

if "--add" in sys.argv:
    result = su.sum(first_num, second_num)
    print(f"{first_num} + {second_num} = {result}")
elif "--multiply" in sys.argv:
    result = su.multiply(first_num, second_num)
    print(f"{first_num} × {second_num} = {result}")
elif "--subtract" in sys.argv:
    result = su.subtract(first_num, second_num)
    print(f"{first_num} - {second_num} = {result}")
elif "--divide" in sys.argv:
    result = su.divide(first_num, second_num)
    print(f"{first_num} ÷ {second_num} = {result}")
else:

    result = su.sum(first_num, second_num)
    print(f"{first_num} + {second_num} = {result} (default: add)")