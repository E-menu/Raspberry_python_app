# Imported library for making GUI
import tkinter as eMenu

# Importet library for reading XML files
import os
from xml.etree import ElementTree

# Import time and date library
import time as tm
import datetime as dt

# Import module for GUI weather
import requests, json 

# Import module for images
from tkinter  import *

# A global constant for our font type 
LARGE_FONT= ("Verdana", 12)
EXTRA_LARGE_FONT =("Verdana",20)

# Variables for weather API
api_key = "8b7c4545e3874014261a301b43f9d144"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name="Wrocław"
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

# Response from server and getting weather info  
response = requests.get(complete_url)
x = response.json()
y = x["main"] 
current_temperature = y["temp"]
temp_celsius = round(current_temperature-273,2)
current_pressure = y["pressure"]
current_humidity = y["humidity"]
z = x["weather"] 
weather_description = z[0]["description"] 

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

def saveOrder(str):

    file = open('testfile.txt','w')
    file.write(str) 
    file.close() 
        
# Exit Function

def exitFunction():
    exit()

    
# Start Page
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

        date_label = eMenu.Label(self,text=f"{dt.datetime.now():%a, %b %d %Y}",font='ariel 30',bg='black',fg='red',width=15)
        date_label.grid(row=1,column=2,padx=40,pady=20)
                            
        weather_label = eMenu.Label(self, text="Miasto: {} \n Temperatura: {} °C \n Ciśnienie: {} hPa \n Wilgotność: {} % \n Opis: {}".format(city_name,temp_celsius,current_pressure,current_humidity,weather_description),font='ariel 20',bg='black',fg='red',width=20)
        weather_label.grid(row=2,column=2,padx=0,pady=0)      

        
# First Page
class PageOne (eMenu.Frame):

    def __init__(self,parent,controller):
        eMenu.Frame.__init__(self,parent)

        # reading XML file
        file_name = 'reed.xml'
        full_file = os.path.abspath(os.path.join('data',file_name))
        
        dom = ElementTree.parse(full_file)\

        courses = dom.findall('/course/title')

        
        names= []
        btn = []
        
        for c in courses:
            names.append(c.text)

        i=0
        for name in names: 
            lb = Label(self, text=name,font='Helvetica 18 bold')
            lb.grid(row=i, column=0,padx=5,pady=5)
            i += 1

        i=0
        for name in names:
            btn.append(Button(self, text="Zamów", command=lambda c=i:saveOrder(names[c])))
            btn[i].grid(row=i, column=1,padx=5,pady=5) #this packs the buttons
            i += 1    
            
        
        button1 = eMenu.Button( self,text="Wróć",font=LARGE_FONT,width=15,height=3,
                                command=lambda: controller.show_frame(StartPage))
        button1.grid(row=i+1,column=0,padx=20,pady=20)  

app = eMenuApp()

app.title('eMenu')
app.geometry('800x480')
app.mainloop()
