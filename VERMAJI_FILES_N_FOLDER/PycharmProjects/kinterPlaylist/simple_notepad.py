# from tkinter import *
# from PIL import Image, ImageTk
#
# root=Tk()
# root.geometry("544x544")
# root.title("notepad tutorial")
# scrollbar=Scrollbar(root)
# scrollbar.pack(side=RIGHT, fill=Y)
# text=Text(root, yscrollcommand=scrollbar.set)
# text.pack(fill=BOTH)
# scrollbar.config(command=text.yview)
# root.mainloop()

from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as tmsg

root=Tk()
root.geometry("544x544")
root.title("notepad tutorial")
scrollbar=Scrollbar(root)
scrollbar.pack(side=LEFT, fill=Y)
text=Text(root, yscrollcommand=scrollbar.set)
text.pack()
scrollbar.config(command=text.yview)
root.mainloop()