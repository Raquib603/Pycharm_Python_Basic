for x in 'banana':
    print(x, end=' ')

print('\n')


# With the break statement,
# we can stop the loop before it has looped through all the items
fruit = ['apple', 'banana', 'cherry', 'chilly', 'oliver']

for i in fruit:
    print(i, end= ' ')
    if i == 'cherry':
        break

print('\n')

# With the continue statement,  [do not print banana]
# we can stop the current iteration of the loop, and continue with the next

for x in fruit:
    if x == 'cherry':
        continue
    print(x, end= ' ')
