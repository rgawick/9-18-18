from calculator import addition, subtraction, multipication, division

first = int(input("First Number: "))
operand = input("Would you like to +, -, * or / ? ")
second = int(input("Second Number: "))

if operand == "+":
    addition(first, second)
elif operand == "-":
    subtraction(first, second)
elif operand == "*":
    multipication(first, second)
else:
    division(first, second)
