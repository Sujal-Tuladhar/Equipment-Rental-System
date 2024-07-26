#import file to access them
import read
import operation
#creating function
def mainFunc():
    '''
    mainFunc is a function that helps in running of the system.
    It is the front part that encapsulate the program and shows 
    function being called from diiferent files to run the program.
    '''

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("-------Welcome to the KuruKuru Rental Shop---------")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    #declaring loop
    program_loop = True
    #Set loop to true because this program run in a loop
    while program_loop:
        print("RENT OR 1 : If you want to rent an item. ")
        print("RETURN OR 2 : If you want to put back an item. ")
        print("INVENTORY OR 3 : To go to the inventory of rental system  ")
        print("END OR 4 : If you want to exit the rental system   ")
        print("\n")
        customer_entry = input("Enter a number to select a option: ").upper()
        
        if customer_entry == "1" or customer_entry == "RENT":
            print("\n")
            print("\t\t\t\t===========RENT TAB HAS OPENED===========")
            #calling function from operation.py
            operation.rentitem_validation()
            
        elif customer_entry == "2" or customer_entry == "RETURN":
            print("\n")
            print("\t\t\t===========RETURN TAB HAS OPENED===========")
            #calling function from operation.py
            operation.returnitem()
        elif customer_entry == "3" or customer_entry == "INVENTORY":
            print("\n")
            print("\t\t\t===========INVENTORY HAS OPENED===========")
            #calling function from read.py
            read.for_table()
            print("\n")
        elif customer_entry == "4" or customer_entry == "END":
            program_loop = False#setting loop false to get out of the program
            print("\t\t|======================|")
            print("\t\t|Thank You for visiting|")
            print("\t\t| KuruKuru Rental Shop |")
            print("\t\t|THE SYSTEM HAS CLOSED |")

            print("\t\t|======================|")
        else:
            print("x" * 57)
            print("===========INVALID DATA HAS BEEN ENTERED===========")
            print("x" * 57)
            print("\n")
mainFunc()#calling the function
