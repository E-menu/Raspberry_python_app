# A constans for our font types 
LARGE_FONT= ("Verdana", 12)
EXTRA_LARGE_FONT =("Verdana",20)

# Imported library for making GUI
import tkinter as eMenu
from tkinter import *

# Imported library for reading XML files
import os
from xml.etree import ElementTree

# Importing files from dictionary /functions
import sys
sys.path.append(os.path.abspath("/home/pi/Desktop/project/Raspberry_python_app/functions"))
from weatherApi import *
from saveOrder import *
from returnDate import *

# Exit Function
def exitFunction():
    exit()
    
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

        for F in (StartPage,PageOne):
            
            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

##############    
# Start Page # 
##############

class StartPage(eMenu.Frame):

    def __init__(self, parent, controller):
        eMenu.Frame.__init__(self,parent)
        
        label = eMenu.Label(self, text="Strona startowa", font='Helvetica 18 bold')
        label.grid(row=0,column=1,padx=20,pady=20)

        button1 = eMenu.Button( self,text="Złóż zamówienie",font=EXTRA_LARGE_FONT,width=15,height=3,
                                command=lambda: controller.show_frame(PageOne))
        button1.grid(row=1,column=1,padx=20,pady=20)

        button2 = eMenu.Button( self,text="Zamknij aplikację",foreground="white",font=EXTRA_LARGE_FONT,bg="red",width=15,height=3,command=exitFunction)
        button2.grid(row=2,column=1,padx=20,pady=20)

        current_date = " "
        current_date = returnDate(current_date)
        
        date_label = eMenu.Label(self,text=current_date,font='ariel 30',bg='black',fg='red',width=15)
        date_label.grid(row=1,column=2,padx=40,pady=20)

        temperature = 0 ; pressure = 0 ; humidity = 0 ;description = "none"
        temperature,pressure,humidity,description = weather(temperature,pressure,humidity,description)
        
        
        weather_label = eMenu.Label(self, text="Miasto: {} \n Temperatura: {} °C \n Ciśnienie: {} hPa \n Wilgotność: {} % \n Opis: {}".format(CITY_NAME,temperature,pressure,humidity,description),font='ariel 20',bg='black',fg='red',width=20)
        weather_label.grid(row=2,column=2,padx=0,pady=0)      

##############
# First Page #
##############

class PageOne (eMenu.Frame):

    def __init__(self,parent,controller):
        eMenu.Frame.__init__(self,parent)

        # reading XML file
        main_meals = 'mainMeals.xml'
        full_file = os.path.abspath(os.path.join('menu_items',main_meals))
        dom = ElementTree.parse(full_file)
        meals = dom.findall('/dish/title')

        # To save meal names that will be used to save order in .txt file
        names= []
        # To save generated buttons
        btn = []

        for m in meals:
            names.append(m.text)

        i=0
        # Generating labels
        for name in names: 
            lb = Label(self, text=name,font='Helvetica 18 bold')
            lb.grid(row=i, column=0,padx=5,pady=5)
            i += 1

        i=0
        # Generating buttons with assigned functions
        for name in names:
            btn.append(Button(self, text="Zamów", command=lambda c=i:saveOrder(names[c])))
            btn[i].grid(row=i, column=1,padx=5,pady=5) 
            i += 1    
            
        
        button1 = eMenu.Button( self,text="Wróć",font=LARGE_FONT,width=15,height=3,
                                command=lambda: controller.show_frame(StartPage))
        button1.grid(row=i+1,column=0,padx=20,pady=20)  



# Launch this app , add title, set geometry and make a mainloop
app = eMenuApp()
app.title('eMenu')
app.geometry('800x480')
app.mainloop()
