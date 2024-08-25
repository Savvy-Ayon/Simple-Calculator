def calculator():
    num1 = float(input("First number: "))
    num2 = float(input("second number: "))
    operator = input("operation (+, -, *, /,): ")

    if operator == '+':
        result = num1 + num2
        print("addition: ", result)
    elif operator == '-':
        result = num1 - num2
        print("substraction: ", result)
    elif operator == '*':
        result = num1 * num2
        print("maltiplication: ", result)
    elif operator == '/':
        result = num1 / num2
        print("division: ", result)
    else:
        print("unknown oparetion!")

calculator()