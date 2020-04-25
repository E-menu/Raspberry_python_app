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
from generateLabelsFromXML import *
from generateButtonsFromXML import *
# end

def makeFirstPage (self,bill,nextMealsPrices,nextMealsNames):

    # reading XML file
    mainMeals = 'mainMeals.xml'
    fullFile = os.path.abspath(os.path.join('menu_items',mainMeals))
    dom = ElementTree.parse(fullFile)

    xmlFileName = 'mainMeals.xml'
    tmpInt = 0
    tmpPrices = []

    labelInfoMainMeals = eMenu.Label(self, text="Dania główne",
                                foreground="green",font='Verdana 15 bold')
    labelInfoMainMeals.grid(row=0,column=0,padx=5,pady=5)

    labelInfoPrice = eMenu.Label(self, text="  Cena  ",
                                foreground="red",font='Verdana 15 bold')
    labelInfoPrice.grid(row=0,column=3,padx=5,pady=5)

    labelInfoDescription = eMenu.Label(self, text="Opis",
                                foreground="black",font='Verdana 15 bold')
    labelInfoDescription.grid(row=0,column=1,padx=5,pady=5)

    labelInfoWeight = eMenu.Label(self, text="Waga",
                                foreground="black",font='Verdana 15 bold')
    labelInfoWeight.grid(row=0,column=2,padx=5,pady=5)

    labelInfoAction = eMenu.Label(self, text="Akcja",
                                foreground="blue",font='Verdana 15 bold')
    labelInfoAction.grid(row=0,column=4,padx=5,pady=5)

    findInXML = 'title'
    makeLabelsFromXML(self,findInXML,xmlFileName,0)

    findInXML = 'price'
    tmpPrices=makeLabelsFromXML(self,findInXML,xmlFileName,3)

    findInXML = 'weight'
    makeLabelsFromXML(self,findInXML,xmlFileName,2)

    findInXML = 'description'
    makeLabelsFromXML(self,findInXML,xmlFileName,1)

    findInXML = 'title'
    tmpInt=makeButtonsFromXML(self,findInXML,xmlFileName,4,bill,tmpPrices,nextMealsPrices,nextMealsNames)


    labelInfoPageNumber = eMenu.Label(self, text="Strona : 1/3", foreground="blue",font='Helvetica 18 bold')
    labelInfoPageNumber.grid(row=tmpInt+1,column=4,padx=10,pady=5)

    return tmpInt
