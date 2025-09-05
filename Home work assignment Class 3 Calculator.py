# Python session 3 Home Work
# Calculator_Script

# Create functions for all the calculation signs

adder = lambda a, b: a + b
subtractor = lambda a, b: a - b
multiplier = lambda a, b: a * b
divisor = lambda a, b: a / b
expo = lambda a, b: a ** b

a = int(input("Enter first number: "))
b = int(input("Enter 2nd number: "))
c = input("calculation sign: ")

if c == "/":
  print("The result after dividing", a, "from ", b, "is", divisor(a, b))
elif c == "*":
  print("The multiplication between ", a, "and ", b, "is", multiplier(a, b))
elif c == "-":
  print("The subtraction of", b, "from", a, "is", subtractor(a, b))
elif c == "+":
  print("The addition of", a, "and", b, "is", adder(a, b))
elif c == "**":
  print("The result of base", a, "and exponent", b, "is", expo(a, b))