import re

def is_binary_multiple_of_3(string):
    binary_numbers = re.findall(r'[01]+', string)
    for binary_number in binary_numbers:
        decimal_value = int(binary_number, 2)
        if decimal_value % 3 != 0:
            return False
    return True

num_lines = int(input("Введите количество строк: "))
valid_strings = []

for i in range(num_lines):
    user_input = input(f"{i + 1}-ая строка: ")
    if is_binary_multiple_of_3(user_input):
        valid_strings.append(user_input)

print("Подходящие строки:")
for valid_string in valid_strings:
    print(valid_string)
