menu = {
    "Pizza" : 300,
    "Pasta" : 180,
    "Burger" : 150,
    "Salad" : 100,
    "coffee" : 80
}

# Greet

print("welcome to Hashim Restaurant")
print("Pizza: Rs300\nPasta: Rs180\nBurger: Rs150\nSalad: Rs100\nCoffee: Rs80")

oder_total = 0

# 80 + 70 = 150

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    oder_total += menu[item_1] 
    print(f"Your item {item_1} has been added to Your order")

else:
    print(f"Ordered item {item_1} is not available yet!")

another_order = input("Do You want to add another item? (Yes/No) ")
if another_order == "Yes":
    item_2 = input("Enter the name of second ")
    if item_2 in menu:
        oder_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not available!")

print(f"The Total amount of items to pay is {oder_total}")