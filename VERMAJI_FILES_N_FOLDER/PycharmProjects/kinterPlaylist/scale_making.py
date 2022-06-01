from  tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("544x544")
def getdollar():
    print(f"we have credited {myslider2.get()} dollars to your bank account")
    tmsg.showinfo("amount credited", f"we have credited {myslider2.get()} dollars to your bank account")
root.title("slider tutorial")
myslider1=Scale(root, from_=0, to=455)
myslider1.pack()
Label(root, text="how many dollars do you want?").pack()
myslider2=Scale(root, from_=10, to=100, orient=HORIZONTAL)
myslider2.pack()
# FOR HAVING THE SLIDER SET AT  A PARTICULAR VALUE
myslider2.set(43)
Button(root, text="get dollars", command=getdollar).pack()
# FOR DENOTING THE PARTICULAR PLACE FOR A PARTICULAR VALUE
myslider3=Scale(root, from_=0, to=100, orient='horizontal', tickinterval=20)
myslider3.pack()
root.mainloop()