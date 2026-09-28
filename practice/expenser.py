def expenses_add(expense,category,amount):
    expense[category]=[amount]

expense={}
expenses_add(expense,"food",500)
print(expense)