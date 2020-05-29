# A constans for our font types
LARGE_FONT= ("Verdana", 12)
EXTRA_LARGE_FONT =("Verdana",20)
# end

# Import tkinter library to show MessageBox
from tkinter import messagebox
# end

# Imported library for making GUI
import tkinter as eMenu
from tkinter import *
# end

# Importing library to connect to serwer to send orders
import socket
import time
# end 

def sendOrder(self,textSummaryOrder,bill,nextMealsNames,nextMealsPrices,s):

    billInt = int (bill[0])

    if billInt == 0:

        textSummaryOrder.delete(1.0,END)
        messagebox.showinfo("Powiadomienie","Nie wysłano pustego zamówienia !")

        print("\n Nie wysłano zamównienia, bowiem jest puste \n")
        
    else:
        textSummaryOrder.delete(1.0,END)

        message = ""
        
        for i in range(0,len(nextMealsNames)):
            message += ";"
            message += nextMealsNames[i-1]
            message += ","
            message += nextMealsPrices[i-1]
        
        mainMessage = "\u0044\u0001PCAPPK1"
        mainMessage += message

        print(mainMessage)
        
        lengthOfMessage = len(mainMessage.encode('utf-8'))
        lengthOfMessageInt = int(lengthOfMessage)


        print("Dlugosc wiadomosci : ",lengthOfMessageInt)

        bytes1 = bytes( [lengthOfMessageInt] )
        bytes2 = mainMessage.encode('utf-8')
        allbytes = bytes1 + bytes2

        time.sleep(2)

        s.send(allbytes)
        from_server = s.recv(2)
        print("\nOdpowiedz serwera :",from_server,"\n")

        print("Wysłano zamówienie \n")
        
        messagebox.showinfo("Powiadomienie","Udało się wysłać zamówienie !")

        bill[0]=0.00
        nextMealsNames.clear()
        nextMealsPrices.clear()
