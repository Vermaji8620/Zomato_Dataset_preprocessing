from tkinter import *

root=Tk()
root.geometry("544x544")
root.title("calculator")
def perform(event):
    global gta
    text=event.widget.cget("text")   #FOR EXTRACTING THE BUTTON THAT IS PRESSED
    if(text=='='):
        if(gta.get().isdigit()):
            value=int(gta.get())
        else:
            try:
                value=eval(gta.get())
            except Exception as g:
                value="ERROR"
        gta.set(value)
        entry.update()
    elif(text=='C'):
        gta.set("")
        entry.update()
    else:
        gta.set(gta.get()+text)
        entry.update()
Label(root, text="CALCULATOR", width=27, height=1, font=('algerian', 25, 'bold', 'underline'), bg='blue', fg='white').pack()
gta=StringVar()
entry=Entry(root, textvariable=gta, font=('Aharoni', 25, 'bold'))
entry.pack()

frame1=Frame(root, bg='blue')
frame1.pack()
b=Button(frame1, text="1", font=('Aharoni', 20, 'bold'), padx=10)
b.pack(side=LEFT)
b.bind("<Button-1>", perform)
b=Button(frame1, text="2", font=('Aharoni', 20, 'bold'), padx=10)
b.pack(side=LEFT)
b.bind("<Button-1>", perform)
b=Button(frame1, text="3", font=('Aharoni', 20, 'bold'), padx=10)
b.pack(side=LEFT)
b.bind("<Button-1>", perform)

frame2=Frame(root, bg='blue')
frame2.pack()
b=Button(frame2, text="4", font=('Aharoni', 20, 'bold'), padx=10)
b.pack(side=LEFT)
b.bind("<Button-1>", perform)
b=Button(frame2, text="5", font=('Aharoni', 20, 'bold'), padx=10)
b.pack(side=LEFT)
b.bind("<Button-1>", perform)
b=Button(frame2, text="6", font=('Aharoni', 20, 'bold'), padx=10)
b.pack(side=LEFT)
b.bind("<Button-1>", perform)

frame3=Frame(root, bg='blue')
frame3.pack()
b=Button(frame3, text="7", font=('Aharoni', 20, 'bold'), padx=10)
b.pack(side=LEFT)
b.bind("<Button-1>", perform)
b=Button(frame3, text="8", font=('Aharoni', 20, 'bold'), padx=10)
b.pack(side=LEFT)
b.bind("<Button-1>", perform)
b=Button(frame3, text="9", font=('Aharoni', 20, 'bold'), padx=10)
b.pack(side=LEFT)
b.bind("<Button-1>", perform)

frame4=Frame(root, bg='blue')
frame4.pack()
b=Button(frame4, text="+", font=('Aharoni', 20, 'bold'), padx=10)
b.pack(side=LEFT)
b.bind("<Button-1>", perform)
b=Button(frame4, text="-", font=('Aharoni', 20, 'bold'), padx=10)
b.pack(side=LEFT)
b.bind("<Button-1>", perform)
b=Button(frame4, text="*", font=('Aharoni', 20, 'bold'), padx=10)
b.pack(side=LEFT)
b.bind("<Button-1>", perform)

frame5=Frame(root, bg='blue')
frame5.pack()
b=Button(frame5, text="/", font=('Aharoni', 20, 'bold'), padx=10)
b.pack(side=LEFT)
b.bind("<Button-1>", perform)
b=Button(frame5, text="%", font=('Aharoni', 20, 'bold'), padx=10)
b.pack(side=LEFT)
b.bind("<Button-1>", perform)
b=Button(frame5, text="!", font=('Aharoni', 20, 'bold'), padx=10)
b.pack(side=LEFT)
b.bind("<Button-1>", perform)

frame6=Frame(root, bg='blue')
frame6.pack()
b=Button(frame6, text="=", font=('Aharoni', 20, 'bold'), padx=10)
b.pack(side=LEFT)
b.bind("<Button-1>", perform)
b=Button(frame6, text="C", font=('Aharoni', 20, 'bold'), padx=10)
b.pack(side=LEFT)
b.bind("<Button-1>", perform)
b=Button(frame6, text=".", font=('Aharoni', 20, 'bold'), padx=10)
b.pack(side=LEFT)
b.bind("<Button-1>", perform)

root.mainloop()


