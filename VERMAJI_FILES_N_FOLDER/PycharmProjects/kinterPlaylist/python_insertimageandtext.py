from tkinter import *
from PIL import Image, ImageTk

x=Tk()
x.geometry("600x600")
x.title("THIS GUI IS MADE BY VERMAJI")
(Label(text="hello everyone this is my GUI", bg='yellow', fg='red', font=('algerian', 25, 'bold', 'italic', 'underline'), borderwidth=5, relief=SUNKEN)).pack(side='bottom',anchor='nw', fill=X)
photo=ImageTk.PhotoImage(Image.open('pubg2.jpg'))
Label(image=photo).pack()
x.mainloop()