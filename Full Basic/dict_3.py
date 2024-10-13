thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#it only can access the key
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

#change items

thisdict['year'] = 1999
print(thisdict)

#we also can use update | for update we have to use key and value together
thisdict.update({'year': 2000})
print(thisdict)

#add new key and value
thisdict['color'] = 'yellow'
print(thisdict)

#remove item
thisdict.pop('model')
print(thisdict)

#clear() method can make the dict empty