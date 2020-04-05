# Save order in .txt file function

def saveOrder(str):

    file = open('/home/pi/Desktop/project/Raspberry_python_app/app_orders/currentOrder.txt','w')
    file.write(str) 
    file.close() 
        
