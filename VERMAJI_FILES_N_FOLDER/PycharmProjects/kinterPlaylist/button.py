from tkinter import *
from PIL import Image, ImageTk

root=Tk()
root.geometry("544x544")
def hello():
    print("hello kinter buttons")
def name():
    print("name is harry")
frame1=Frame(root, borderwidth=6, bg='grey', relief=SUNKEN)
frame1.pack(side=LEFT, anchor='nw')
button1=Button(frame1, fg='red', text="intro", command=hello)
button1.pack(side=LEFT)
frame2=Frame(root, borderwidth=6, bg='grey', relief=SUNKEN)
frame2.pack(side=LEFT, anchor='nw')
button2=Button(frame2, fg='red', text="tell me name now", command=name)
button2.pack(side=LEFT)
frame3=Frame(root, borderwidth=6, bg='grey', relief=SUNKEN)
frame3.pack(side=LEFT, anchor='nw')
button3=Button(frame3, fg='red', text="print now")
button3.pack(side=LEFT)
frame4=Frame(root, borderwidth=6, bg='grey', relief=SUNKEN)
frame4.pack(side=LEFT, anchor='nw')
button4=Button(frame4, fg='red', text="print now")
button4.pack(side=LEFT)
frame5=Frame(root, borderwidth=6, bg='grey', relief=SUNKEN)
frame5.pack(side=LEFT, anchor='nw')
button5=Button(frame5, fg='red', text="print now")
button5.pack(side=LEFT)
root.mainloop()


# QUSTNS FOR THIS

# from tkinter import *
# from PIL import ImageTk, Image

# border=Tk()
# border.geometry("544x544")
# def write1():
#     print(open('GUI_basics.py', 'r').read())
# def write2():
#     print(open('GUI_NEWSPAPERQSTN.py', 'r').read())
# border.title("this is a question")
# frame1=Frame(border, bg='red', borderwidth=20, relief=SUNKEN)
# frame1.pack(side=LEFT, anchor='nw', padx=5)
# button1=Button(frame1, text="button1", font=('algerian', 8, 'bold', 'italic'), command=write1)
# button1.pack(side=RIGHT, anchor='ne', padx=6)
# frame2=Frame(border, bg='red', borderwidth=20, relief=SUNKEN)
# frame2.pack(side=LEFT, anchor='nw', padx=5)
# button2=Button(frame2, text="button1", font=('algerian', 8, 'bold', 'italic'), command=write2)
# button2.pack(side=RIGHT, anchor='ne', padx=6)
# border.mainloop()

