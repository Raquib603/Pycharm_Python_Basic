fruit = ['apple', 'banana', 'cherry', 'chilly', 'oliver']

for i in range(len(fruit)):
    print(fruit[i], end=', ')

print('\n')
# range() function works with integer
# range() function defaults to 0 as a starting value

for x in range(6):
    print(x, end= ' ')

print('\n')
# specify the starting value by adding a parameter:
# range(2, 6), which means values from 2 to 6 (but not including 6)
for x in range(2, 10):
    print(x, end= ' ')

print('\n')
# there is default increment for range function 1
# but we can specify the increment

for x in range(2, 100, 3):
    print(x, end= ' ') #starting with 2, within 100 and increment by 3