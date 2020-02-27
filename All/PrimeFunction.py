"""def prime(n):
    x=1
    for i in range(2,n):
        if n%i==0:
            x=0
            break
        else:
            x=1
    return x
num=int(input("Enter the number:"))
result=prime(num)
if result==1:
    print(num,"is a prime no")
else:
    print(num,"is not a prime no")"""

a=int(input("Enter a no"))
def prime(a):
    for i in range(2,a//2):
        if (a%i==0):
            print(a,"is not a prime no")
            break
    else:
        print(a,"is a prime no")
prime(a)