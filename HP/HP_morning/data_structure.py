#set
#s1=set(range(5))
#s.add(10)
# I=[1,2,4]
# s.update(range(5))
#s1=s.copy()
# print(s.pop())
# print(s.pop())
#s={10,20,30,40,50,30,20,50}
# s.remove(20)
# s.remove(100)
# s.discard(30)
# s.discard(100)
# s.clear()
# print(s)
# x={10,20,30}
# y={30,40,50}
#print(x.union(y))
# print(x.intersection(y))
#print(x.difference(y))
# print(x.symmetric_difference(y))
# s=set("python")
# print(s)
# s={x*x for x in range(5)}
# print(s)

# w = input("Enter the word")
# s = set(w)
# v = {'a','e','i','o','u'}
# print(s.intersection(v))


#List
# l1=[10,20,[30,40]]
# print(l1[2][1])
# l2=[40,50,60]
# l=l1+l2
# print(l)
# l=[90,50,10,20,30,20,40,40,60]
# print(l.sort())
# print(l.reverse())
# print(l.pop())
# l.remove(40)
# l1=[70,80]
# l.extend(l1)
# l.insert(5,70)
# l.append(70)
# print(l)
# print(l.index(40))
# print(l.count(40))
# print(len(l))
# l[2]=50
# l1=list(range(2,20,2))
# print(l1)
# l="Learning python is very easy task"
# l1=l.split()
# print(list(l1))


#tuple
# s1={10,20,30}
# s2={10,20,30}
# print(s1 is s2)
# l1=[10,20,30]
# l2=[10,20,30]
# print(l1 is l2)
# t1=(10,20,30)
# t2=(10,20,30)
# print(t1 is t2)

#t1=tuple(range(10,101,10))
# print(t1[2:5])
# print(t1[2:])
# print(t1[::2])
#print(len(t1))
# print(t1.count(990))
#print(t1.index(990))
# t=(39,17,20,48,50,38,40)
# print(min(t))
# print(max(t))
# t1=sorted(t)
# print(t1)
# a=10
# b=20
# c=30
# d=40
# t=a,b,c,d
# print(t)
# a,b,c,d=t
# print(a)

#Dictionary
d=dict()
d[100]='a','d'
d[200]='b'
d[300]='c'
print(d)
# print(d[100])
# d[400]='f'
# print(d)
# d[200]='e'
# print(d)
# del(d[200])
# print(d)
# print(d.keys())
# print(d.items())
# print(d.values())
# d.pop(100)
# print(d)
d.setdefault(300)
print(d[300])
d[300]='f'
print(d)
d.setdefault()