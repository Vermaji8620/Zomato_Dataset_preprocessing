from tkinter import *

root=Tk()
root.geometry("544x544")
def add():
    global i
    lbx.insert(ACTIVE, f"{i}") #ACTIVE KA MATLAB HOTA HAI KI
    # JO V MENU HM SELECT KRKE RAKHE HAI USKE BAAD ADD HO JAYEGA
    i+=1
i=0
root.title("listbox tutorial")
lbx=Listbox(root)
lbx.pack()
lbx.insert(END, "first item of our listbox")
Button(root, text="add item", command=add).pack()
root.mainloop()


