# Import tkinter library to show MessageBox
from tkinter import messagebox
# end

# Save order in .txt file function
def saveOrder(str,bill,var):

    # Saving info about an order in .txt file
    file = open('app_orders/currentOrder.txt','w')
    file.write(str)
    file.close()

    # Actual bill will be ...
    newPrice=0.00
    newPrice = bill[0] +float(var)
    bill[0]=newPrice

    messagebox.showinfo("Powiadomienie","Dodano do zamówienia !\nAktualna cena zamówienia: {} zł.".format(newPrice))
