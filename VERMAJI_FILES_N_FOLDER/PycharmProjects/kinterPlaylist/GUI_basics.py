from tkinter import *
from PIL import ImageTk, Image

x=Tk()
x.geometry("700x600")
x.title("VERMAJI KA GUI")
# x.minsize(100, 100)
# x.maxsize(400, 400)
# photo=ImageTk.PhotoImage(Image.open('pubg1.jpg'))
# Label(image=photo).pack()

# IMPORTANT LABEL OPTIONS
# text=adds the text
# bd=background
# fg=foreground
# font=sets the font
# padx=x padding
# pady=y padding
# relief=(border styling)=SUNKEN, RAISED, GROOVE, RIDGE
# pics=ImageTk.PhotoImage(Image.open('pubg1.jpg'))
# Label(image=pics).pack()

(Label(text="hello i am here", bg='red', fg='yellow', padx=13, pady=54, font=("Panoptica", 25, 'bold', 'italic', 'underline'),
       borderwidth=100, relief=SUNKEN)).pack(side=BOTTOM, anchor='sw', fill=Y)

#FOR CHANGING THE ICON
x.wm_iconbitmap('snake1.jpg')
#FOR CHANGING THE WINDOW COLOUR
x.config(bg='red')
# FOR GETTING THE PC SREEN WIDTH AND HEIGHT
width=x.winfo_screenwidth()
height=x.winfo_screenheight()
print(f"{width}x{height}")

x.mainloop()