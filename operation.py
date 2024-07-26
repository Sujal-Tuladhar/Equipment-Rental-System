#importing file to get access
import read
import write
import informationFile
#storing table from rady.py in variable
rent_dicti = read.read_file()
#Creating 2D list
equipment_orders_transactions = []
#Creating a function
def rentitem_validation():
    '''
    this function help in function of renting function and does all
    the validation required for the program.this program decreases quantity
    and create bill in terminal.
    '''
    read.for_table()
    #making a loop to re rent item if wanted
    billloop = True
    #try to check datatype validation
    try:

        customer_name = input("Enter customers full name : ")
        while not customer_name.isalpha():
            print("invalid data")
            customer_name = input("Enter customers full name : ")
        customer_phone = int(input("Enter customers Phone number : "))
        
        while billloop == True:
            try:
                
                ask_forId = int(input("Enter the id of the item you want to rent : "))
                #id validation
                if ask_forId in rent_dicti and ask_forId > 0:
                    ask_forQty = int(input("Enter the amount you want rent:"))
                    # quantity validation
                    if ask_forQty<1:
                        print("======quantity cannt be entered=========")
                    else:
                        if rent_dicti[ask_forId]['quantity'] >= ask_forQty:
                            #code for rent
                            rent_dicti[ask_forId]['quantity'] = rent_dicti[ask_forId]['quantity'] - ask_forQty
                            write.rent_write(rent_dicti)
                            print("-------The item has been rented-------.")

                            add_equipment_order(
                                ask_forId, ask_forQty, customer_name, customer_phone)
                            
                            ask_formore = input(
                                "Do you want to rent more item? y/n : ")
                            if (ask_formore == "n"):
                                billloop = False
                                term_rentbill=informationFile.rentitem_billing(equipment_orders_transactions)
                                print(term_rentbill)
                        else:
                            print("x" * 60)
                            print("========The quantity is not available.NOT RENTED=======")
                            print("x" * 60)
                            ask_forId = rentitem_validation()
                else:
                    print("x" * 60)
                    print("========The item of the id doesnt exist.NOT RENTED==========")
                    print("x" * 60)
                    ask_forId = rentitem_validation()

                if (billloop == False):
                        informationFile.rentitem_billing(equipment_orders_transactions)
            except:
                print("=========his datatype cant be taken. Re-enter the value=========")
                print("\n")
    except:
        print("=========his datatype cant be taken. Re-enter the value=========")   
        print("\n")

def add_equipment_order(equipmentId, quantityToRent, customerName, customerPhoneNumber):
    '''
    this function is used to print item in loop
    It is used when user wants to rent or return more item
    '''

    if equipmentId in rent_dicti:
        rentPrice = rent_dicti[equipmentId]['price']
        rentBrand= rent_dicti[equipmentId]['brand']
        transaction = {
            'equipmentId': equipmentId,
            'name': rent_dicti[equipmentId]['name'],
            'price': rentPrice,
            'brand': rentBrand,
            'quantity': quantityToRent,
            'customerName': customerName,
            'phoneno': customerPhoneNumber,
        }
        #to add iterm in 2D list
        equipment_orders_transactions.append(transaction)
        print("========Transaction recorded successfully=========")
    else:
        print("============Invalid equipment ID===========")

# ---------FOR RETURN-----------------
def returnitem():
    '''
        this function help in function of returning function and does all
        the validation required for the program.this program increases quantity
        and create bill in terminal.
        '''
    read.for_table()
    billloop = True
    try:
        customer_name = input("Enter customers full name : ")
        while not customer_name.isalpha():
            print("invalid data")
            customer_name = input("Enter customers full name : ")
        customer_phone = input("Enter customers Phone number : ")
        while (billloop == True):
            try:
                ask_forId = int(
                    input("Enter the id of the item you want to return:"))
                if ask_forId <= 0:
                    print("Wrong Value ☒")
                elif ask_forId not in rent_dicti:
                    print("The product ID doesnt exist.")

                if ask_forId in rent_dicti and ask_forId > 0:
                    ask_forQty = int(input("Enter the amount you want return:"))
                    if ask_forQty<1 :
                        print("======quantity cannot be entered=========")
                    else:
                        rent_dicti[ask_forId]['quantity'] = rent_dicti[ask_forId]['quantity'] + ask_forQty
                        write.rent_write(rent_dicti)
                        print("-------The item has been returned-------.")
                        add_equipment_order(
                                ask_forId, ask_forQty,customer_name, customer_phone)

                        ask_formore = input(
                                "Do you want to rent more item? y/n : ")
                        if (ask_formore == "n"):
                            billloop = False


                else:
                    print("x" * 60)
                    print("========The item id is not available.CANNOT RETURN=======")
                    print("x" * 60)
                    ask_forId = returnitem()

                if (billloop == False):
                        x=informationFile.returnbill(equipment_orders_transactions)
                        print(x)


            except:
                print("=========his datatype cant be taken. Re-enter the value=========")
                
    except:
        print("=========his datatype cant be taken. Re-enter the value=========")    