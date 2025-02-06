import random

Cnumber=random.randrange(1, 10)
userInput=int(input("Enter your number:---"))
if userInput>Cnumber:

    print("Computer number", Cnumber)
    print("Your guess number is too high")

elif Cnumber>userInput:

    print("Computer number", Cnumber)
    print("Your guess number is too low")

else:
    print("Computer number", Cnumber)
    print("your guess number is equal")

