# store data values in pairs lieke -  {key : value}
# doesnt store duplicate keys

x = {
    'brand': 'ford',
    'model': 'mustang',
    'year': '1964'
}

print(x)

# we can use the key to access the dictionary values
print(x['brand'])

print(len(x))
print(type(x))

# we can use dict() constructor to make a dictionary
thisdict = dict(name="John", age=36, country="Norway")
print(thisdict)
