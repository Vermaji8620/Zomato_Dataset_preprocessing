from tkinter import *

root=Tk()

def getvals():
    print(f"username is {username.get()}"
          f"\n"     
          f"password is {password.get()}")

    a=open('used in checkbox.py', 'a').write(f"username is {username.get()}"
                                f"\n"
                                f"password is {password.get()}"
                                f"\n"
                                f"\n")

root.geometry("544x545")
root.title("this is a program")
Label(root, text="Username").grid(row=0, column=0)
Label(root, text="password").grid(row=1, column=0)
username=StringVar()
password=StringVar()
Entry(root, text=username).grid(row=0, column=1)
Entry(root, text=password).grid(row=1, column=1)
Button(root, text="submit", command=getvals).grid(row=4, column=0)
Checkbutton(root, text="do you want to submit finally").grid(row=3, column=0)
root.mainloop()