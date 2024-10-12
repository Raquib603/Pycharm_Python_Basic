x = {'cherry', 'banana', 'orange', 'apple', 'garlic', 'onion'}


#access set

for item in x:
    print(item, end= ", ")

print('\n')
#we can use 'in' or 'not in' to check item is in there or not
if 'cucumber' in x:
    print("It is present")
else: print("Its not present")


#adding items
x.add('ommo')
print(x)


#adding another set to a existing set
b = {1, 3, 5}
x.update(b)
print(x)

#we use remove or pop for removing items from set 