menu={
    "pizza":3.00,
    "nachos":5.00,
    "sods":2.00,
    "chips":4.00,
    "fries":5.00
}
cart=[]
total=0
print("--------MENU--------")
for x,y in menu.items():
    print(x,y)
while True:
    item=input("Enter the food item and q to exit")
    if item=="q":
        break
    elif menu.get(item) is not None:
        cart.append(item)
print(cart)
for food in cart:
    total=total+menu[food]

print(total)
