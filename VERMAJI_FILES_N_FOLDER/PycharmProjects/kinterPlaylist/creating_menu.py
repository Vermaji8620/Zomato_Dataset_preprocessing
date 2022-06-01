from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("544x544")
root.title("PYCHARM")
def myfunc():
    print("gbrgbhregbhnrhgbn")
def mypic():
    print("i am fine")

# USE THESE TWO TO CREATE A NON-DROP DOWN MENU

# mymenu=Menu(root)
# mymenu.add_command(label="File", command=myfunc)
# mymenu.add_command(label="Exit", command=quit)
# root.config(menu=mymenu)


# FOR CREATING A DROP DOWN MENU

# mainmenu=Menu(root)
#
# submenu1=Menu(mainmenu, tearoff=0)
# submenu1.add_command(label="cut", command=myfunc)
# submenu1.add_separator()
# submenu1.add_command(label="copy", command=myfunc)
# submenu1.add_separator()
# submenu1.add_command(label="paste", command=myfunc)
# submenu1.add_separator()
# submenu1.add_command(label="print", command=myfunc)
# submenu1.add_separator()
# mainmenu.add_cascade(label="file", menu=submenu1)
#
#
# submenu2=Menu(mainmenu)
# submenu2.add_command(label="save", command=mypic)
# submenu2.add_command(label="save as", command=mypic)
# submenu2.add_command(label="open", command=mypic)
# submenu2.add_command(label="navigate", command=mypic)
# mainmenu.add_cascade(label="edit", menu=submenu2)
# root.config(menu=mainmenu)


root.mainloop()