"""myself={
    "name":"sai",
    "age":32,
    "city":"chennai"
}
print(f"My name is {myself['name']} and I am {myself['age']}")

product = {"name": "Pen", "price": 10}
product["price"]=90
print(product)
person = {"name": "Sam", "age": 25, "city": "Delhi"}
person.pop("city")
print(person)"""
"""marks = {"Math": 80, "Science": 90, "English": 70}
for key,value in marks.items():
    print(f"{key}: {value}")
 if value>75:
     print(f"{key} is above 75")"""
prices = {"apple": 50, "banana": 20, "mango": 80}
total=0
for fruit,price in prices.items():
    total+=price
    print(total)