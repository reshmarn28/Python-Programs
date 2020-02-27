"""n = int(input("enter the number"))
i = 1
while (i<=10):
    t = n*i
    print(n,"*",i,"=",t)
    i=i+1"""

"""n = int(input("enter the number"))
prod = 1
sum = 0
while(n>=1):
    prod = prod * n
    print(prod)
    n=n-1
    sum = sum + prod
    print(sum)
else:
    print ("otherwise")"""

"""x= 1
sum =0
while(True):
    sum = sum + x
    print(sum)
    x = x+1"""


"""n=(10,25,57,28,59,57,23,89,12,25)
odd = 0 
even = 0
for i in n:
    if(i%2==0):
        even = even + 1
    else:
        odd = odd + 1
print("even count is:",even,"\n odd count is:",odd)

print(list(range(1,11)))"""

"""#n=(10,25,57,28,59,57,23,89,12,25)
for i in range(10):
    if(i==3):
        break
    print(i)"""

"""for i in n:
    if(i==28):
        break
    print(i)"""


"""sum = 0
for i in range(10):
    sum = sum + i
    if i==5:
        continue
print(sum)"""


even = 0
odd = 0
i=1
while(i<11):
    if(i%2==0):
        even=even+1
    else:
        odd=odd+1
    i=i+1
print("even count is:",even,"\n odd count is:",odd)


str = input("Enter a string")
d=l=0
for c in str:
    if c.isalpha():
        l = l+1
        print(c)
    elif c.isdigit():
        d=d+1
        print(c)
    else:
        pass
print("no of letters:",l,"\nno of digits:",d)
