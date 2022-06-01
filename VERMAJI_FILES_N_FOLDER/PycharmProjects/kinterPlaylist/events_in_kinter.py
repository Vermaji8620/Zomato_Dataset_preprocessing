from tkinter import *
def harry(event):
    print(f"you clciked on the button at {event.x}, {event.y}")
root=Tk()
root.title("event in tkinter")                                                      
root.geometry("544x544")
widgets=Button(root, text="click me", )
widgets.pack()
widgets.bind('<Button-1>', harry)
widgets.bind('<Double-1>', quit)
root.mainloop()