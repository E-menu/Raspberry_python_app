# Added a Python package for GUI apps  
from tkinter import *

# Inicialazing new window
window = Tk()

# Window title and resolution 
window.title("Customer app")
window.geometry('800x480')

lbl = Label(window,text="Correct resolution")
lbl.grid(column=0,row=0)

# Main loop 
window.mainloop()
