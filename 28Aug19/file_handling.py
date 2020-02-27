"""r = read = deafault value = open file, but error if file not exist
w = write = open file, but create a new file if file not exist
a = append = open file for appending, but create a new file if file not exist
x = create = create a new file but error if already exists
t = text = defalt mode = text mode 
b = binary file = binary mode = images"""

"""f = open("abc.txt","w")
f.write("This is my first Python file")
f.close()"""

"""f=open("abc.txt","a")
f.write("\nThis is my 2nd line in the file")
f.close()"""

f = open("abc.txt","rb")
#f.read(0)
"""str = f.readline()
print(str)
str=f.readline(13)
print(str)"""
f.seek(3,1)
l1=f.readline()
#f.seek(5,0)
#l2=f.readline()
print(l1)
#print(l2)
f.
