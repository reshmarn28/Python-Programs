total = 100
percentage = 12.3
name = 'ashish'

#int float
a=b=10
print (a+b)
print (9/4)

#multiline input
address = '''ashish
hadapsar
Pune'''
print(address)

#list
arr = [1,2,3,4,5]
print(arr[0]) #print particular value
print(arr[0:3]) #print the 0-3rd position
calender = ['Jan','Feb','March']
print(calender[2:]) #print from 2nd element to last
print(calender * 2) #print 2 times
mix = [1,2,3,'pune']
print(arr)
print(mix)

#concatenation of 2 lists
print(calender+arr)

#modify the elements
calender[0] = 'December'
print(calender)
calender[1:2]='April','May'
print(calender)

#tuple
lis = [1,2,3,4,5]
tup = (1,2,3,4,5)
print(lis, tup)
print(tup[3])
del lis #delete the entire list
del tup #delete the entire tuple
#print(lis, tup)


#Dictionary
d = {'name':'ashish','city':'pune'}
print(d)
print(d['name'])
d['name'] = 'amit'
print (d['name'])

tinydict = {2:'two'} #mixed dictionary
print(tinydict)
print(d.keys())  #print only keys
print(d.values())  #print only values

del d['city']  #DELETE THE VALUE
print(d)

l1=[1,2,3,4,5,6]
l2=[7,8,9,0,10]
l3=[4,5,6,7,7]
print(l1,tuple(l2),tuple(l3))
