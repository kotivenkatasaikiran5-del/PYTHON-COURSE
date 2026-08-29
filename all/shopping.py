foods=[]
prices=[]

while True:
    food=input("enter food item (x to exit):")
    if food=="x":
        break
    price=float(input("enter price of food item:"))
    foods.append(food)
    prices.append(price)
for food,price in (foods,prices):
    print(food)
    print(price)

for price in prices:
    total=sum(prices)
    print(total)   