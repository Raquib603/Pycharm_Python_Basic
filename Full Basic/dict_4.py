x = {1: 'apple', 2: 'banana', 3: 'orange', 4: 'pinaple', 5: 'cherry', 6: 'avocado'}

# same as list but here we set the index manually as we want

# this only print the keys
for item in x:
    print(item, end=' ')

# loop through both keys and values
for a, b in x.items():
    print(a, b)
print('\n')

# this will print the values
for item in x:
    print(x[item], end=' ')
print('\n')

for item in x.values():
    print(item, end=' ')

print('\n')
