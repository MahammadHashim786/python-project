# Marks sheet

percentage = int(input("Enter percentage: "))
 
if percentage >= 80:
    print("You got A1 Grade")
elif percentage >= 70 and percentage < 80:
    print("You got A Grade")
elif percentage >= 60 and percentage < 70:
    print("You  got B Grade")
elif percentage >= 50 and percentage < 60:
    print("You got C Grade")
elif percentage >= 40 and percentage < 50:
    print("You got D Grade")
elif percentage >= 33 and percentage < 40:
    print("You got D Grade")
else:
    print("You are Fail")