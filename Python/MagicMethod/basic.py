# everything defined in python is an Object
def func():
    pass

print(type(func)) # type <class 'function'>

str1 = 'hello'
str2 = 'world'

# we can add 2 strings because this object are of same type
# python has implemented it as double underscore method
# there is some kind of class behind it defining all of its behaviour
new_str = str1 + str2   
new_str_2 = str1.__add__(str2) # it uses __add__ method
print(new_str)
print(new_str_2)

new_str = str1.__len__()
print(new_str)
