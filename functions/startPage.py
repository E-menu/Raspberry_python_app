# A constans for our font types
LARGE_FONT= ("Verdana", 12)
EXTRA_LARGE_FONT =("Verdana",20)
# end

# Imported library for making GUI
import tkinter as eMenu
from tkinter import *
# end

# Importing files from directory /functions
import sys
import os
sys.path.append(os.path.abspath("/"))
from weatherApi import *
from returnDate import *
# end

def makeStartPage (self):

    labelStartPage = eMenu.Label(self, text="Strona startowa", font='Helvetica 24 bold')
    labelStartPage.grid(row=0,column=2,padx=20,pady=20)

    currentDate = " "
    currentDate = returnDate(currentDate)

    dateLabel = eMenu.Label(self,text=currentDate,font='ariel 30',bg='black',fg='green2',width=15)
    dateLabel.grid(row=1,column=2,padx=40,pady=20)

    temperature = 0
    pressure = 0
    humidity = 0
    description = "none"

    temperature,pressure,humidity,description = weather(temperature,pressure,humidity,description)


    weatherLabel = eMenu.Label(self, text="Miasto: {} \n Temperatura: {} °C \n Ciśnienie: {} hPa \n Wilgotność: {} % \n Opis: {}"
                                    .format(CITY_NAME,temperature,pressure,humidity,description),
                                    font='ariel 20',bg='black',fg='green2',width=20)
    weatherLabel.grid(row=2,column=2,padx=0,pady=0)
