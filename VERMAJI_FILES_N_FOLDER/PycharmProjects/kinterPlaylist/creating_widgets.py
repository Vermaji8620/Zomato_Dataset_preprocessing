from tkinter import *

root=Tk()
canvas_width =500
canvas_height=500
root.geometry(f"{canvas_width}x{canvas_height}")
can_widget=Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()
# THE LINE GOES FROM THE POINT x1,y1 TO x2,y2
can_widget.create_line(0, 0, 500, 500, fill='red')
can_widget.create_line(0, 500, 500, 0, fill='blue')
can_widget.create_line(250, 0, 250, 500)
can_widget.create_line(0, 250, 500, 250)
# TO CREATE A RECTANGLE SPECIFY THE PARAMETERS IN THIS ORDER--coordiantes
# of top left and coordiantes of bottom right
can_widget.create_rectangle(100, 100, 400, 400, fill='blue')
can_widget.create_oval(100, 100, 400, 400, fill='black')
can_widget.create_text(250, 240, text="python",
                       font=('algerian', 25, 'bold'),
                       fill='white')

root.mainloop()
