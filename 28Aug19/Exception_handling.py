a=10
b=0
try:
    print(a/b)
except Exception:
    print("you can not divide by",b,"\n try another number")
finally:
    print("Resource closed")