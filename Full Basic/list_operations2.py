a = [1,2,3,4,5,6,7,8,9,10]

print(a)

#basic loop
for items in a:
    print(items, end= ', ')


print('\n')
#looping by index number
for items in range(len(a)):
    print(a[items], end= ' ')


print('\n')
#List comprehension offers a shorter syntax when you want to
#create a new list based on the values of an existing list

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#Only accept items that are not "apple"
newlist_2 = [x for x in fruits if x != "apple"]
print(newlist_2)

a.sort()
print(a)
#sort in reverse (by default sort will work as ascending order)
a.sort(reverse= True)
print(a)

#we can reverse a list without order by 'reverse' function
m = ['a', 'l', 'k']
m.reverse()
print(m)