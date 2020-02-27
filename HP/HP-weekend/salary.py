from employee import *
a=float(input("enter basic salary"))
gross=da(a)+hra(a)+pf(a)
print("Gross salary is:",gross)
net=gross-itax(gross)
print("net salary is:",net)