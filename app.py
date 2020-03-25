# Imported library for making GUI
import tkinter as eMenu

# A global constant for our font type 
LARGE_FONT= ("Verdana", 12)

# Main class , everything we have done here is to add new pages in our app

class eMenuApp(eMenu.Tk):

    # Initialization
    def __init__(self, *args, **kwargs):

        eMenu.Tk.__init__(self, *args, **kwargs)
        container = eMenu.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}

        frame = StartPage(container,self)

        self.frames[StartPage] = frame

        frame.grid(row=0,column=0,sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
        
class StartPage(eMenu.Frame):

    def __init__(self, parent, controller):
        eMenu.Frame.__init__(self,parent)
        label = eMenu.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

app = eMenuApp()
app.title('eMenu')
app.geometry('800x480')

app.mainloop()
