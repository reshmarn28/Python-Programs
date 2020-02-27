from employee import *
basic=float(input("enter the basic salary:"))
gross=da(basic)+hra(basic)+pf(basic)
print("gross salary is:",gross)

net=gross-pf(basic)-itax(gross)
print("net salary is:",net)