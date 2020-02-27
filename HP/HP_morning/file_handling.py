"""r = read = default value = open file, but error if file not exist
w = write = open file, but create a new file if file not exist
a = append = open file for appending, but create a new file if file not exist
x = create = create a new file but error if already exists
t = text = defalt mode = text mode 
b = binary file = binary mode = images"""

#file = open("name of file", "mode of file")

f1 = open("abc.txt","r")
print(f1.read(2:4))

# f2 = open("xyz.txt","w")
# for data in f1:
#     f2.write(data)
# f2= open("xyz.txt","r")
# print(f2.read())

# f2 = open("xyz.txt","a")
# f2.write("Javascript")
# f2= open("xyz.txt","r")
# print(f2.read())

# print(f1.readline())
# print(f1.readlines())

# f1 = open("image.jpg","rb")
# f2 = open("image1.jpg","wb")
# for data in f1:
#     f2.write(data)

