# Import tkinter library to show MessageBox
from tkinter import messagebox
# end

# Save order in arrays
def saveOrder(mealName,price,bill,nextMealsPrices,nextMealsNames):

    # Saving info about an order in arrays
    nextMealsPrices.append(price)
    nextMealsNames.append(mealName)

    # To test app in terminal
    print("Aktualnie zamowione mealsNames  : " + str(nextMealsNames))
    print("Aktualnie zamowione mealsPrices : " + str(nextMealsPrices))
    # end

    # Actual bill will be ...
    newBill = bill[0] +float(price)
    bill[0]=newBill

    # To test app in terminal
    print("Aktualny rachunek wynosi : "+str(bill))
    print("\n")
    # end

    messagebox.showinfo("Powiadomienie","Dodano do zamówienia !\nAktualna cena zamówienia: {} zł.".format(newBill))
