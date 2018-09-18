# integer 
print("#### numbers #####")
my_integer = 4.
print(type(my_integer), my_integer)

my_integer_as_string = "4.5"
my_integer_new = int(float(my_integer_as_string))
print(type(my_integer_new), my_integer_new)
print(dir(my_integer_new))

# strings
print("#### strings #####")
my_next_string = "my string"
print(type(my_next_string), my_next_string)

my_next_string = my_next_string + my_next_string.upper()

print(type(my_next_string), my_next_string)
print(dir(my_next_string))

mystring = "A very long string that I will slice"


print(mystring[8:13])

print(mystring[:-5])
print(mystring[-5:])

# mystring2 = str(list(mystring).reverse()) # not working
# print(mystring2)


# lists
mylist = range(1, 50)
print(mylist)
print(dir(mylist))


# tuples
def myfunc(a, b, c):
    print("{} {} {}".format(a, b, c))


mytuple = (0, 1, 2)
myfunc("arg1", "arg2", "arg3")
myfunc(*mytuple)

myfunc(*mylist[:3])

# dictionary
mydict = {'key': 'value', 'key2': 'blah'}
for k, v in mydict.iteritems():  # .items() in python 3
    print("{}=>{}".format(k, v))
