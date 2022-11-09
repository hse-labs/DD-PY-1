number = 2342354235235

list_digits = [int(digit) for digit in str(number)]

print(sum(list_digits))
print(sum([even_digit for even_digit in list_digits if even_digit % 2 == 0]))
print(len(list_digits))
print(min(list_digits))
print(list_digits[0] - list_digits[-1])
