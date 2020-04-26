# A constans for our font types
LARGE_FONT= ("Verdana", 12)
EXTRA_LARGE_FONT =("Verdana",20)
# end

# Import tkinter library to show MessageBox
from tkinter import messagebox
# end

# Imported library for making GUI
import tkinter as eMenu
from tkinter import *
# end

def sendOrder(self,textSummaryOrder):

    textSummaryOrder.delete(1.0,END)
    messagebox.showinfo("Powiadomienie","Udało się wysłać zamówienie !")
