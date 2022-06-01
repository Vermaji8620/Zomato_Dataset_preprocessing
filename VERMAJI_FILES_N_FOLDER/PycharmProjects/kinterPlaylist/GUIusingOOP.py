from tkinter import *

# JO MERA PEHLE ROOT HUA KRTA THA WO CLASS K ANDAR AB
# SELF HAI AUR WAHI ROOT AB MERA CLASS K BAHAR WINDOW HAI

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("544x544")

    def status(self):
        self.var=StringVar()
        self.var.set("ready")
        self.statusbar=Label(self, textv=self.var, relief=SUNKEN, anchor='w')
        self.statusbar.pack(side=BOTTOM, fill=X)

    def click(self):
        print("button clicked")

    def create_button(self, inptext):
        Button(text=inptext, command=self.click).pack()

if __name__ == '__main__':
    window=GUI()
    window.status()
    window.create_button("click me")
    window.mainloop()