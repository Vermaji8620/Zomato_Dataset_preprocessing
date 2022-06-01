from tkinter import *
from PIL import Image, ImageTk

root=Tk()
root.geometry("655x333")
f1=Frame(root, bg='grey', borderwidth=10, relief=SUNKEN)
f1.pack(side=LEFT, fill=Y, pady=122)
l1=Label(f1, text="project tkinter--pycharm")
l1.pack(pady=142)

f2=Frame(root, borderwidth=9, bg='yellow', relief=SUNKEN)
f2.pack(side=TOP)
l2=Label(f2, text="welcome to sublime", fg='red', font='algerian 25 bold')
l2.pack()

root.mainloop()

# ANOTHER PROGRAM


# from tkinter import *
# from PIL import ImageTk, Image
#
# border=Tk()
# border.geometry("455x455")
# border.title("hello this is my program")
# fr1=Frame(border,  bg='red', borderwidth=115, relief=SUNKEN)
# fr1.pack(side=RIGHT, anchor='se', fill=X)
# l1=Label(fr1, text="hello my world", bg='blue', fg='white', font=('algerian', 25, 'bold', 'italic'), borderwidth=90, relief=SUNKEN)
# l1.pack()
# fr2=Frame(border, bg='pink', borderwidth=20, relief=SUNKEN)
# fr2.pack(side=BOTTOM, anchor='sw')
# picsart=ImageTk.PhotoImage(Image.open('snake2.jpg'))
# l2=Label(fr2, image=picsart)
# l2.pack(side=BOTTOM, anchor='sw')
# border.mainloop()