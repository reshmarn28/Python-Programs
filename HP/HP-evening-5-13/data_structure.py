#set
#s={1,2,1,4,5.5,6.2,'a','b',1,2,5.5}
# print(s[0])
# s={40,50,60}
# I=[10,20,30]
# # s.add(6)
# s.update(I,range(5))

# s={10,20,30}
# s1=s.copy()
# print(s1)
#print(s.pop())
# s.remove(100)
# s.discard(100)
# s.clear()
# print(s)

# s={10,20,30}
# s1={40,50,30}
# print(s.union(s1))
# print(s.intersection(s1))
# print(s.difference(s1))
# print(s.symmetric_difference())
# s=set("python")
# print(s)
# s={x*x for x in range(5)}
# print(s)



#List
# l=[10,20,30,5.7,2.9]
# l.sort()
# l.reverse()
# print(l)
# print(l.pop())
# print(l.pop())
# print(l.insert(2,777))
# l1=['c','d','e']
# print(l.append(l1))
#print(l.extend(l1))
# l.remove(10)
# print(l)
#print(l.count(60))
#print(l.index(10))
# print(len(l))
# l[2]=700
# print(l)
# print(l[0:])
# print(l[1:5])
# print(l[:])
# print(l[1:7:2])
# print(l[-1])

# print(l)
# print(l[0])
# l1=list(range(1,9,2))
# print(l1)
# s="It is very easy to learn python"
# l2=s.split()
# print(l2)
# l=[10,20,[30,40]]
# print(l[0])
# print(l[1])
# print(l[2][1])


#tuple
# t=[10,20,30,40,50,20,40]
# l= tuple(t)
# print(l)
# t1=10,20,30
# t2=30,40,50
# t=t1+t2
# # print(len(t1))
# # print(t.count(30))
# print(t.index(30))
# t=58,29,40,38,10
# # t1=sorted(t)
# print(min(t),max(t))
# t=(10,20)
# a=30
# b=40
# c=50
# d=60
# t=a,b,c,d
# print(t)

#Dictionary
d=dict()
d[100]='a','d'
d[200]='b'
print(len(d))
print(d.keys())
print(d.values())
# print(d)
# d[100]='c'
# print(d)
# print(d.get(300))
print(d.popitem())
# del d[200]
# print(d[100][0])
# d.clear()
print(d.items())
d1=d.copy()
print(d1)
# print(len(d))
# print(d.get(100))
#print(d.popitem())
d.setdefault(300,'abc')
print(d)