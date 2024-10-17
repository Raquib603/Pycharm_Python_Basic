fruit = ['apple', 'banana', 'cherry', 'chilly', 'oliver']

# if run by index then i should be initialize with another integer
# range() function works with integers
for i in range(len(fruit)):
    print(i, end= ' ') #to see the indexes
    print(fruit[i], end= ' ')

print('\n')

for item in fruit:
    print(item, end= ' ')