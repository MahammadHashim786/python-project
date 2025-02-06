def calculator(num1,num2,opr):
    if opr == "add":
        return num1 + num2
    elif opr == "sub":
        return num1 - num2
    elif opr == "mul":
        return num1 * num2
    elif opr == "div":
        return num1 / num2
    else:
        return "invalid opreter"
print(calculator(4,4,"add"))
print(calculator(4,4,"sub"))
print(calculator(4,4,"mul"))
print(calculator(4,4,"div"))