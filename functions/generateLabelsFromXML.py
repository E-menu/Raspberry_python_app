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

def makeLabelsFromXML(self,findInXML,xmlFileName,columnNumber):

    # reading XML file
    xmlName = '{}'.format(xmlFileName)
    fullFile = os.path.abspath(os.path.join('menu_items',
                xmlName))
    dom = ElementTree.parse(fullFile)

    labelsName = []

    findAll = dom.findall('./dish/{}'.format(findInXML))

    for f in findAll:
        labelsName.append(f.text)

    i=0
    # Generating labels
    for name in labelsName:
        lb = Label(self, text=name,font='Helvetica 16 bold')
        lb.grid(row=i+1, column=columnNumber,padx=5,pady=5)
        i += 1

    return labelsName
