"""r = read = deafault value = open file, but error if file not exist
w = write = open file, but create a new file if file not exist
a = append = open file for appending, but create a new file if file not exist
x = create = create a new file but error if already exists
t = text = defalt mode = text mode 
b = binary file = binary mode = images"""

#File write
"""f = open("xyz.txt", "w")
f.write("This is my file")
f.close()"""

"""#append
f = open("xyz.txt","a")
f.write("\nThis is my 2nd line")
f.close()"""

"""#read
f = open("xyz.txt","r")
f.read(16)
str = f.read()
print(str)"""

#readline
f = open("xyz.txt","r")
"""str = f.read(0)
print(str)
str = f.readline()
print(str)
str = f.readline()
print(str)
str = f.readline()
print(str)
str = f.readlines()
print(str)"""

#seek
f = open("xyz.txt","rb")
f.seek(3,0)
l1 = f.readlines()
print(l1)
f.seek(3,1)
l2 = f.readlines()
print(l2)