def myfunc():
    global x
    x = 'fantastic'

myfunc()

print('python is '+ x)


y = memoryview(bytes(5))
print(y)

a = range(6)
print(a)

#Variables that are created outside of a function (as in all of the examples in the previous pages)
# are known as global variables.
#Global variables can be used by everyone, both inside of functions and outside.