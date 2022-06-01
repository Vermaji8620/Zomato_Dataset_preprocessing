from tkinter import *


root=Tk()
root.geometry("544x544")
root.title("status bar")
def upload():
    statusvar.set("busy...")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("ready now")
statusvar=StringVar()
statusvar.set("ready")
sbar=Label(root, textvariable=statusvar,  anchor='w', relief=SUNKEN)
sbar.pack(side=BOTTOM, fill=X)
Button(root, text="UPLOAD", command=upload).pack()
root.mainloop()
