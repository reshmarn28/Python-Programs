"""r = read = default value = open file, but error if file not exist
w = write = open file, but create a new file if file not exist
a = append = open file for appending, but create a new file if file not exist
x = create = create a new file but error if already exists
t = text = defalt mode = text mode 
b = binary file = binary mode = images"""
f1 = open("image.jpg","rb")
f2 = open("copy.jpg","wb")
for data in f1:
    f2.write(data)
f2 = open("copy.jpg","rb")
print(f2.read())
#f1.write()
# print(f1.readline(2))
# print(f1.readline())
# print(f1.readlines())