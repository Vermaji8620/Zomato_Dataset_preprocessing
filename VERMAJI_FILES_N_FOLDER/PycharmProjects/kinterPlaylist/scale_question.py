from tkinter import *
import tkinter.messagebox as tmsg

root=Tk()
root.geometry("544x544")
root.title("just esehi")
def func():
    tmsg.showinfo("customer service", "THANKS FOR THE RATING GIVEN")
    open('usedinsliderquestion.py', 'a').write(f"{slider.get()}")
    print("customer slider rating updated")
tmsg.showinfo("customer service", "kindly rate us please")
# MAKING A SLIDER
slider=Scale(root, from_=0, to=10, orient='horizontal', tickinterval=2)
slider.pack()
# SUBMISSION BUTTON MAKING
Button(root, text="SUBMIT RATING", command=func).pack()

root.mainloop()
