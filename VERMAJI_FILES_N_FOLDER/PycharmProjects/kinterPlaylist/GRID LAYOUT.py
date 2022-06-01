from tkinter import *

draw=Tk()
draw.geometry("544x544")
def func1():
    print("CREDENTIALS ARE")
    open('scrollbar_tutorial.py', 'w').write(f"USERNAME IS {usernamevalue.get()}"
                                f"\n"
                                f"PASSWORD IS {passwordvalue.get()}")
draw.title("this is a program to submit details")
Label(draw, text="username").grid(row=0, column=0)
Label(draw, text="password").grid(row=1, column=0)

usernamevalue=StringVar()
passwordvalue=StringVar()
Entry(draw, text=usernamevalue).grid(row=0, column=1)
Entry(draw, text=passwordvalue).grid(row=1, column=1)

Button(draw, text="submit", command=func1).grid(row=3, column=0)

draw.mainloop()
