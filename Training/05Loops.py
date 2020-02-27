"""#FOR loop
city = "Nagpur"
print(city[2])  #considering string as a list

for letter in city:
    print(letter)

fruits = ['banana','mango','apple',1234]
for f in fruits:
    print(f)
    print("Fruit is "+str(f)) #concatenation

for i in range(1,10):
    print (i)
for i in range(1,10,2):  #print 1-10 but incremented by 2
    print(i)

#for-else loop
for i in range(1,110,10): 
    print(i)
else:
    print("at the end")"""

#While loop
"""count = 0
while(count<9):
    print(count)
    count+=1
else:
    print(count)

while(True):  #infinite loop
    print (0)"""

#Nested loop
city = "Pune"
for i in range(0,4):
    for j in city:
        print(str(i) + ":" +str(j))


    