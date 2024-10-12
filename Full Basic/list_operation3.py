a = ['apple', 'banana', 'orange', 'cucumber', 'chilly']

m = [1, 2, 3, 4, 5, 6]

print(a)

b = a.copy()

print(b)

c = list(b)
print(c)

#adding new list like mathematics {we can also do that by, extend}
x = a + m
print(x)

#count any specific items in list by count method
print(a.count('apple'))

#len will return the value of number of items in a list
print(len(a))