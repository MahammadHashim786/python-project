a = int(input("Enter your First Number "))
b = int(input("Enter your second Number "))
opr = input("+" "-" "/" "* Enter your character ")

if opr == "+":
    print(a + b)
elif opr == "-":
    print(a - b)
elif opr == "/":
    print(a / b)
elif opr == "*":
    print(a * b)
else:
    print("invalid correcter")
