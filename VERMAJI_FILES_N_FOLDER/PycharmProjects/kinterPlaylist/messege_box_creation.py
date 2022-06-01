from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("544x544")
root.title("PYCHARM")

def help():
    print("i am to be helped")
    print(tmsg.showinfo("help", "harry will help you with his gui"))
    print(tmsg.askokcancel("hello", "are you satisfied with the help"))
    prin=(tmsg.askquestion("dialog box", "was it helpful"))
    print(prin)
    if(prin=='yes'):
        tmsg.showinfo("dialog boz", "tnx for positive feedback")
    else:
        tmsg.showinfo("dialog box", "tnx for suggestion. we will improve")

mainmenu=Menu(root)

submenu=Menu(mainmenu)
submenu.add_command(label="help", command=help)
mainmenu.add_cascade(label="help", menu=submenu)
root.config(menu=mainmenu)

root.mainloop()