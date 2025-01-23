num1 = int(input("Enter The No 1: "))
num2 = int(input("Enter The No 2: "))
operator = input("Enter The operator: ")

if operator == '+':
    print(num1 + num2)

elif operator == '-':
    print(num1 - num2)

elif operator == '*':
    print(num1 * num2)

elif operator == '/':
    print(num1 / num2)

else:
    print('Invalid Operator!')   