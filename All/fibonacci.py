def fib(limit):
    a,b=0,1
    print(a,b)
    while a<limit:
        yield a
        a,b=b,a+b
x = fib(5)
for i in x:
    print(i)
