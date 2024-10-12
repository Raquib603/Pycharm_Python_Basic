# -------There are several ways to join two or more sets in Python.

# The union() and update() methods joins all items from both sets.
# The intersection() method keeps ONLY the duplicates.
# The difference() method keeps the items from the first set that are not in the other set(s).
# The symmetric_difference() method keeps all items EXCEPT the duplicates.

set1= {1, 2, 3, 4}
set2 = {3, 5, 8, 9}

set3 = set1.union(set2)
set4 = set1.update(set2) #update stores the values into the first variable
print(set3)
print(set1)


#here we could also use or '|' for union. Ex: myset = set1 | set2 | set3 |set4
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

#----------union = |--------intersection = &---------------

#intersection for only common items from sets
set1 = {'apple', 'banana', 'cherry'}
set2 = {'google', 'microsoft', 'apple'}
set3 = set1.intersection(set2)
print(set3)