from tkinter import *
from PIL import Image, ImageTk
root=Tk()
root.geometry("544x544")
root.title("this is a news-type program")
texts=[]
photos=[]
for i in range(0,3):
    with open(f"snake{i+1}.txt")as f:
        text=f.read()
        texts.append(text)
    image=(Image.open(f"snake{i+1}.jpg"))
    # TODO:Resize the images
    image=image.resize((225, 225), Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(image))
frame=Frame(root, width=800, height=70, borderwidth=10, bg='blue')
frame.pack()
Label(frame, text="code with harry news", font=('algerian', 33, 'bold')).pack()
Label(frame, text="jan 19, 2050", font=('Arial Black', 13, 'bold')).pack()

frame1=Frame(root, width=900, height=200)
Label(frame1, text=texts[0], padx=22, pady=22).pack(side=LEFT)
Label(frame1, image=photos[0], anchor='e').pack()
frame1.pack(anchor='w')

frame2=Frame(root, width=900, height=200)
Label(frame2, text=texts[1], padx=22, pady=22).pack(side=RIGHT)
Label(frame2, image=photos[1], anchor='e').pack()
frame2.pack(anchor='w')

frame3=Frame(root, width=900, height=200)
Label(frame3, text=texts[2], padx=22, pady=22).pack(side=LEFT)
Label(frame3, image=photos[2], anchor='e').pack()
frame3.pack(anchor='w')

root.mainloop()

