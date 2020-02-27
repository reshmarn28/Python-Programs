from employee import *
basic=float(input("enter the basic salary:"))
gross=ha(basic)+ta(basic)+pf(basic) 
print("gross salary is:",gross)

net=gross-pf(basic)-itax(gross)
print("net salary is:",net)