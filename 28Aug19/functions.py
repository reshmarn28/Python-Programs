"""def display():
    print("This is my first function")
display()

def functon_with_parameters(param1,param2,param3):
    print("Value for param1 is {}".format(param1))
    print("Value for param1 is {}".format(param2))
    print("Value for param1 is {}".format(param3))

a = int(input("enter the value for a:"))
functon_with_parameters(a,"python",30.4)
#functon_with_parameters(my_int)

def function_with_defalt_parameters(param1,param2,param3=20):
    print("Value for param1 is {}".format(param1))
    print("Value for param2 is {}".format(param2))
    print("Value for param3 is {}".format(param3))

function_with_defalt_parameters(100,200,)"""

def function_with_returning_value():
    return "Python"
str = function_with_returning_value()
print(str)

def add(a,b):
    c = a + b
    return c
result = add(10,20)
print(result)
