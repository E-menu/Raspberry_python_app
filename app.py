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

# For image library
from PIL import Image, ImageTk

# A variable for customer's bill
bill = []
bill.append(0.00)

# A variable to remember specific item price
price = []
price.append(0.00)

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
        
        label = eMenu.Label(self, text="Strona startowa", font='Helvetica 24 bold')
        label.grid(row=0,column=2,padx=20,pady=20)

        button1 = eMenu.Button( self,text="Złóż zamówienie",font=EXTRA_LARGE_FONT,width=15,height=3,
                                command=lambda: controller.show_frame(PageOne))
        button1.grid(row=1,column=1,padx=20,pady=20)

        button2 = eMenu.Button( self,text="Zamknij aplikację",foreground="white",font=EXTRA_LARGE_FONT,bg="red",width=15,height=3,command=exitFunction)
        button2.grid(row=2,column=1,padx=20,pady=20)

        current_date = " "
        current_date = returnDate(current_date)
        
        date_label = eMenu.Label(self,text=current_date,font='ariel 30',bg='black',fg='green2',width=15)
        date_label.grid(row=1,column=2,padx=40,pady=20)

        temperature = 0 ; pressure = 0 ; humidity = 0 ;description = "none"
        temperature,pressure,humidity,description = weather(temperature,pressure,humidity,description)
        
        
        weather_label = eMenu.Label(self, text="Miasto: {} \n Temperatura: {} °C \n Ciśnienie: {} hPa \n Wilgotność: {} % \n Opis: {}".format(CITY_NAME,temperature,pressure,humidity,description),font='ariel 20',bg='black',fg='green2',width=20)
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
    

        # To save meal names that will be used to save order in .txt file
        names= []
        # To save generated buttons
        btn = []
        # To save item's prices
        prices = []
        # To save items weight
        weights = []

        meals = dom.findall('./dish/title')
        
        for m in meals:
            names.append(m.text)

        product_prices = dom.findall('dish/price')    

        for p in product_prices:
            prices.append(p.text)

        product_weights = dom.findall('dish/weight')
            
        for w in product_weights:
            weights.append(w.text)
            

        labelInfo0 = eMenu.Label(self, text="Dania główne", foreground="green",font='Verdana 15 bold')
        labelInfo0.grid(row=0,column=0,padx=5,pady=5)

        labelInfo1 = eMenu.Label(self, text="  Cena  ", foreground="red",font='Verdana 15 bold')
        labelInfo1.grid(row=0,column=3,padx=5,pady=5)

        labelInfo2 = eMenu.Label(self, text="Opis", foreground="black",font='Verdana 15 bold')
        labelInfo2.grid(row=0,column=1,padx=5,pady=5)

        labelInfo3 = eMenu.Label(self, text="Waga", foreground="black",font='Verdana 15 bold')
        labelInfo3.grid(row=0,column=2,padx=5,pady=5)
        
        labelInfo4 = eMenu.Label(self, text="Akcja", foreground="blue",font='Verdana 15 bold')
        labelInfo4.grid(row=0,column=4,padx=5,pady=5)
        
        i=0
        # Generating labels
        for name in names: 
            lb = Label(self, text=name,font='Helvetica 16 bold')
            lb.grid(row=i+1, column=0,padx=5,pady=5)
            i += 1

        i=0    
        for p in prices:
            lb = Label(self, text=p,font='Helvetica 16  bold')
            lb.grid(row=i+1, column=3,padx=5,pady=5)
            i += 1    

        i=0    
        for w in weights:
            lb = Label(self, text=w, font='Helvetica 16  bold')
            lb.grid(row=i+1, column=2,padx=5,pady=5)
            i += 1     
            
        i=0
        # Generating buttons with assigned functions
        for name in names:
            btn.append(Button(self, text="Zamów", command=lambda c=i:saveOrder(names[c],bill,prices[c])))
            btn[i].grid(row=i+1, column=4,padx=5,pady=5) 
            i += 1    
            
        
        button1 = eMenu.Button( self,text="Wróć",font=LARGE_FONT,width=8,height=2,
                                command=lambda: controller.show_frame(StartPage))
        button1.grid(row=i+1,column=0,padx=10,pady=5)  

        labelInfo = eMenu.Label(self, text="Strona : 1/3", foreground="blue",font='Helvetica 18 bold')
        labelInfo.grid(row=i+1,column=4,padx=10,pady=5)

        button2 = eMenu.Button( self,text="Następna strona",font=LARGE_FONT,width=15,height=2,
                                command=lambda: controller.show_frame(StartPage))
        button2.grid(row=i+1,column=1,padx=10,pady=5) 
        

class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom
        
# Launch this app , add title, set geometry and make a mainloop
app = eMenuApp()
app.title('eMenu')
app.geometry('800x480')
#appFull=FullScreenApp(app)
app.mainloop()

