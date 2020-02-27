# str = input("Enter a string")
# d=l=0
# for c in str:
#     if c.isalpha():
#         l = l+1
#         print(c)
#     elif c.isdigit():
#         d=d+1
#         print(c)
#     else:
#         pass
# print("no of letters:",l,"\nno of digits:",d)
#squareof nos:
# def sq(n):
#     n=n*n
#     print(n)
# for n in range(31):
#     sq(n)
# def sq():
#     l=list()
#     for i in range(1,31):
#         l.append(i**2)
#     print(l)
# sq()

# def sq(n):
#     return n*n
# for i in range(31):
#     print(sq(i))


#palindrom
# a=input("enter string")
# if(a[::-1]==a):
#     print("its palindrome")
# else:
#     print("not palindrome")

# a=input("enter string")
# def rev(a):
#     return a[::-1]
# s=rev(a)
# if s==a:
#     print("palindrome")
# else:
#     print("not palindrome")

# def mul(s):
#     l=1
#     for p in s:
#         l=l*p
#     return l
# list=[1,2,3]
# print(mul(list))

# l=[]
# n=int(input("elements:"))
# for i in range(n):
#     elements=int(input())
#     l.append(elements)
# print(l)

# l=list(map(float,input("elements:").split()))
# print(l)

#character frequency
# s=input("string: ")
# freq={}
# for i in s:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# print("frequency is:"+str(freq))

#divisible by 7 and multiple of 5
# count=0
# for i in range(1500,2701):
#     if i%7==0 and i%5==0:
#         print(i)
#         count+=1
# print(count)

# 

# a = int(input("enter a number"))
# rev = 0
# while(a>0):
#   rem = a%10
#   rev = rev*10+rem
#   a = a//10 
# print(rev)





    
