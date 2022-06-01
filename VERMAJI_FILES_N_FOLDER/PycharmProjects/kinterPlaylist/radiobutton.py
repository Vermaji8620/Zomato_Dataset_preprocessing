# JAISE KI CHECKBUTTON WALA PROGRAM THA USME EK OPTION KO CHECK YA FIR UNCHECK
# KR SKTE HAI. MATLAB KI AGAR SATH ME BHOT SARA OPTION HAI, TO SB KO EK BAAR ME
# HI CHECK KR SKTE HAI.    LEKIN HMKO AISA PROGRAM CHHAIYE KI BHOT SARA OPTION
# ME SE KOI EK OPTION SELECT HO. TO WAISE PANE K LIYE YE RADIOBUTTON WALA PROGAM
# KAAM ME ATAA HAI



from tkinter import *
import tkinter.messagebox as tsmg

root=Tk()
root.geometry("544x544")
root.title("radiobuttons")
def order():
    tsmg.showinfo(f"order received ", f"we have received your order for {var.get()}. Thanks for ordering")
var=IntVar()
var.set(1)
Label(root, text="what would you like to have sir", fg='blue', font=('algerian', 15, 'bold')).pack()
radio1=Radiobutton(root, text="dosa", value=1)
radio1.pack()
radio2=Radiobutton(root, text="idly", value=2)
radio2.pack()
radio3=Radiobutton(root, text="paratha", value=3)
radio3.pack()
radio4=Radiobutton(root, text="samosa", value=4)
radio4.pack()
Button(root, text="order now", command=order).pack()
root.mainloop()