
"""from tkinter import *
root = Tk()
root.mainloop()"""


"""from tkinter import *
root = Tk()
root.title("My window")
root.geometry("400 * 300")
root.wm_iconbitmap('image.bmp')
root.mainloop()"""

"""from tkinter import *
from tkinter import font
root = Tk()
list_fonts = list(font.families())
print(list_fonts)"""

from tkinter import *
root = Tk()
c = Canvas(root, bg="blue", height=700, width=1200, cursor='pencil')
id = c.create_line(50, 50, 200, 50,200, 150,width = 4, fill="white")
