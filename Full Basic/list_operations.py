
#Remember that the first item has index 0
x = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]


#  [included : excluded]
print(x)

print(x[3:6])


#search in list
if 'cherry' in x:
    print('Yes, cherry is present in this list')


#change list item
x[2:4] = 'watermelon', 'cucumber'
print(x)

# --insert-- insert items for specific location
x.insert(2, 'chilly')
print(x)

# --append-- add items to the last
x.append('onion')
print(x)


#add multiple list into one. this will autometically store the list into the first one
a = [1, 2, 3]
b = [4, 5, 6]
c = a.extend(b)
print(a)

#remove from list(this will remove the first occurance)
a.remove(1)
print(a)

#pop will remove the specific index, attribute is index number. but by default it will remove the last item
a.pop()
print(a)
a.pop(2)
print(a)

#del also do the same job. and clear will use for delete all elements from the list
a.clear()
print(a)
