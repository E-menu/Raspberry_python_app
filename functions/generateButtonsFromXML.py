# A constans for our font types
LARGE_FONT= ("Verdana", 12)
EXTRA_LARGE_FONT =("Verdana",20)
# end

# Imported library for making GUI
import tkinter as eMenu
from tkinter import *
# end

# Imported library for reading XML files
import os
from xml.etree import ElementTree
# end

# Importing files from directory /functions
import sys
sys.path.append(os.path.abspath("/"))
from saveOrder import *
# end

def makeButtonsFromXML(self,findInXML,xmlFileName,columnNumber,bill,prices,nextMealsPrices,nextMealsNames):

    # reading XML file
    xmlName = '{}'.format(xmlFileName)
    fullFile = os.path.abspath(os.path.join('menu_items',
                xmlName))
    dom = ElementTree.parse(fullFile)

    labelsName = []
    # To save generated buttons
    btn = []

    findAll = dom.findall('./dish/{}'.format(findInXML))

    for f in findAll:
        labelsName.append(f.text)

    i=0
    # Generating buttons with assigned functions
    for name in labelsName:
        btn.append(Button(self, text="Zamów",
        command=lambda c=i:saveOrder(labelsName[c],prices[c],bill,nextMealsPrices,nextMealsNames)))

        btn[i].grid(row=i+1, column=4,padx=5,pady=5)
        i += 1

    return i
