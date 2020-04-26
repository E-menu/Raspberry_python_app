# A constans for our font types
LARGE_FONT= ("Verdana", 12)
EXTRA_LARGE_FONT =("Verdana",20)
# end

# Imported library for making GUI
import tkinter as eMenu
from tkinter import *
# end

# Show order function
def showOrder(self,bill,nextMealsNames,nextMealsPrices,textSummaryOrder):

        for i in range(0,len(nextMealsNames)):
            textSummaryOrder.insert(eMenu.INSERT,i+1)
            textSummaryOrder.insert(eMenu.INSERT," ")
            textSummaryOrder.insert(eMenu.INSERT,nextMealsNames[i])
            textSummaryOrder.insert(eMenu.INSERT," ")
            textSummaryOrder.insert(eMenu.INSERT,nextMealsPrices[i])
            textSummaryOrder.insert(eMenu.INSERT,"\n")

        textSummaryOrder.insert(eMenu.INSERT,"\n")
        textSummaryOrder.insert(eMenu.INSERT,"Cena całkowita zamówienia : {} zł.".format(bill[0]))
