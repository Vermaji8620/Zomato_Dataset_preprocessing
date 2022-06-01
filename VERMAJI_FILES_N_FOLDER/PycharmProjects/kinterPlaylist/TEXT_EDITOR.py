from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newfile():
    global file
    root.title("UNTITLED--NOTEPAD")
    file=None
    Textarea.delete(1.0, END)      #PEHLA LINE KA ZERO-ETH CHARACTER SE END TAK   

def openfile():
    global file
    file=askopenfilename(defaultextension=".txt", filetypes=[("All files", "*.*"),
                                                             ("Text Documents", "*.txt")])
    if(file==""):
        file=None
    else:
        root.title(os.path.basename(file)+"- Notepad")
        Textarea.delete(1.0, END)
        f=open(file, 'r')
        Textarea.insert(1.0, f.read())
        f.close()

def savefile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                               filetypes=[("All files", "*.*"),("Text Documents", "*.txt")])
        if file=="":
            file=None
        else:
            f=open(file, 'w')
            f.write(Textarea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file)+ "- Notepad")


    else:
        f = open(file, 'w')
        f.write(Textarea.get(1.0, END))
        f.close()

def quitapp():
    root.quit()
def cut():
    Textarea.event_generate()
def copy():
    Textarea.event_generate("<<Copy>>")
def paste():
    Textarea.event_generate("<<Paste>>")
def about():
    tmsg.showinfo("NOTEPAD", "Notepad by VERMAJI")

if __name__ == '__main__':
    # BASIC KINTER SETUP
    root=Tk()
    root.geometry("544x544")
    root.title("UNTITLED__NOTEPAD")
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)
    Textarea=Text(root, font=('algerian', 13), yscrollcommand=scrollbar.set)
    Textarea.pack(expand=True, fill=BOTH)
    scrollbar.config(command=Textarea.yview)
    file=None
    # LETS CREATE A MENUBAR
    Menubar=Menu(root)

    Filemenu=Menu(Menubar, tearoff=0)
    Filemenu.add_command(label="New", command=newfile)
    Filemenu.add_command(label="Open", command=openfile)
    Filemenu.add_command(label="Save", command=savefile)
    Filemenu.add_separator()
    Filemenu.add_command(label="Exit", command=quitapp)
    Menubar.add_cascade(label="File", menu=Filemenu)
    root.config(menu=Menubar)

    Editmenu=Menu(Menubar, tearoff=0)
    Editmenu.add_command(label="cut", command=cut)
    Editmenu.add_command(label="copy", command=copy)
    Editmenu.add_command(label="paste", command=paste)
    Menubar.add_cascade(label="Edit", menu=Editmenu)
    root.config(menu=Menubar)

    Helpmenu=Menu(Menubar, tearoff=0)
    Helpmenu.add_command(label="about notepad", command=about)
    Menubar.add_cascade(label="help", menu=Helpmenu)
    root.config(menu=Menubar)

    root.mainloop()

