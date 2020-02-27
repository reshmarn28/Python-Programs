"""#Logical
p = True
q = False

print(p & q)
print( p or not q)


#Relational
a=10
b=50
print(a>b)
print(a==b)
print(a<b)"""

#membership
x = "Python"
print('y'in x)
print('g' not in x)

#identity
a = 3
b = 3
print(a is b)
l1 =(1,2,3)
l2 = (1,2,3,4)
print(l1 is not l2)
print(id(l1))
print(id(l2))