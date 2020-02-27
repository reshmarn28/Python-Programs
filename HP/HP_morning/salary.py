from employee import *
basic=float(input("enter basic salary:"))
gross = basic+hra(basic)+ta(basic)+pf(basic)
print("Your gross salary is:",gross)
net = gross-itax(gross)
print("Your net salary is:",net)