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
sys.path.append(os.path.abspath("functions"))
from weatherApi import *
from saveOrder import *
from returnDate import *
from mealsPages import *
from setFullScreen import *
from startPage import *
# end


# A variable for customer's bill
bill = []
bill.append(0.00)

# A variable to remember next item in order price
nextMealsPrices = []

# A variable to remember next item in order name
nextMealsNames = []

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

        for F in (StartPage,PageOne,PageTwo,PageThree):

            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

    def show_first_frame(self, cont,nextMealsNames,nextMealsPrices):

        # If we go to first page we ALWAYS will be ordering from beginning
        bill[0]=0.00
        nextMealsNames.clear()
        nextMealsPrices.clear()

        frame = self.frames[cont]
        frame.tkraise()

##############
# Start Page #
##############

class StartPage(eMenu.Frame):

    def __init__(self, parent, controller):
        eMenu.Frame.__init__(self,parent)

        makeStartPage(self)

        buttonMakeOrder = eMenu.Button( self,text="Nowe zamówienie",font=EXTRA_LARGE_FONT,width=15,height=3,
                                        command=lambda: controller.show_first_frame(PageOne,nextMealsNames,nextMealsPrices))
        buttonMakeOrder.grid(row=1,column=1,padx=20,pady=20)

        buttonCloseApp = eMenu.Button( self,text="Zamknij aplikację",foreground="white",font=EXTRA_LARGE_FONT,
                                bg="red",width=15,height=3,command=exitFunction)
        buttonCloseApp.grid(row=2,column=1,padx=20,pady=20)


##############
# First Page #
##############

class PageOne (eMenu.Frame):

    def __init__(self,parent,controller):
        eMenu.Frame.__init__(self,parent)

        tmpInt = 0
        tmpInt=makeMealPage(self,bill,nextMealsPrices,nextMealsNames,'mainMeals.xml','Dania główne',1)

        buttonNextPage = eMenu.Button( self,text="Następna strona",font=LARGE_FONT,width=15,height=2,
                                        command=lambda: controller.show_frame(PageTwo))
        buttonNextPage.grid(row=tmpInt+1,column=0,padx=10,pady=5)

###############
# Second Page #
###############

class PageTwo (eMenu.Frame):

    def __init__(self,parent,controller):
        eMenu.Frame.__init__(self,parent)

        tmpInt = 0
        tmpInt=makeMealPage(self,bill,nextMealsPrices,nextMealsNames,'additives.xml','Dodatki',2)

        buttonNextPage = eMenu.Button( self,text="Następna strona",font=LARGE_FONT,width=15,height=2,
                                        command=lambda: controller.show_frame(PageThree))
        buttonNextPage.grid(row=tmpInt+1,column=0,padx=10,pady=5)

###############
# Third Page  #
###############

class PageThree (eMenu.Frame):

    def __init__(self,parent,controller):
        eMenu.Frame.__init__(self,parent)

        tmpInt = 0
        tmpInt=makeMealPage(self,bill,nextMealsPrices,nextMealsNames,'drinks.xml','Napoje',3)

        buttonNextPage = eMenu.Button( self,text="Następna strona",font=LARGE_FONT,width=15,height=2,
                                        command=lambda: controller.show_frame(StartPage))
        buttonNextPage.grid(row=tmpInt+1,column=0,padx=10,pady=5)

# Launch this app , add title, set geometry and make a mainloop
app = eMenuApp()
app.title('eMenu')
app.geometry('800x480')
#appFull=FullScreenApp(app)
app.mainloop()
