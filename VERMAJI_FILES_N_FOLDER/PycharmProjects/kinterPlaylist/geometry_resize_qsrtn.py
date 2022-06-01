from tkinter import *

root=Tk()
def execute():
    root.geometry(f"{width.get()}x{height.get()}")
root.geometry("544x544")
root.title("esehi")
Label(root, text="width", font=('algerian', 20, 'bold')).grid(row=0, column=0)
Label(root, text="height", font=('algerian', 20, 'bold')).grid(row=1, column=0)
width=StringVar()
height=StringVar()
Entry(root, text=width).grid(row=0, column=1)
Entry(root, text=height).grid(row=1, column=1)
Button(root, text="RESIZE", bg='blue', fg='white', font=('Bauhaus 93', 15, 'underline'), command=execute).grid(row=2, column=0)

root.mainloop()