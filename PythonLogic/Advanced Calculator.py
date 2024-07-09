print("ADVANCED CALCULATOR!!!\n")

print("This is a basic calculator.\n\n"
      "Operator examples:\n"
      "1. + (addition)\n"
      "2. - (subtraction)\n"
      "3. * (multiplication)\n"
      "4. / (division)\n")

operator = input("Enter operator: ")
num_1 = float(input("Enter a number: "))
num_2 = float(input("Enter second number: "))


if operator == "+":
    print(num_1 + num_2)
elif operator == "-":
    print(num_1 - num_2)
elif operator == "*":
    print(num_1 * num_2)
elif operator == "/":
    print(num_1 / num_2)
else:
    print("\nInvalid operator selected!")