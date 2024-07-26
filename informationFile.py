#imprting files to get access of the file
import read
#importing date and time to use in the program
import datetime

#storing the date and time in variable to easy use
time = datetime.datetime.now()
year = str(time.year)
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)
sec = str(time.second)
micr = str(time.microsecond)
#storing dictionary in variable by calling
rentbill_dictionary = read.read_file()

def rentitem_billing(data):
    '''
    this program is used to print invoice of bill in new file and
    manage how data is kept in the invoice
    '''
    #accessing data from 2D list
    customername=data[0]['customerName']

# Calculate total for each transaction
    for item in data:
        #calculating the total amount
        item['total'] = item['price'] * item['quantity']

    # Calculate grand total
    grand_total = sum(item['total'] for item in data)

    # Create a formatted bill
    formatted_date = day+"-"+month+"-"+year
    formatted_time = hour+"~"+month+"~"+sec
    bill_text = "==========Kurukuru Rented item BILL===========\n\n"
    bill_text += "="*92 +"\n"
    bill_text += f"\t\t\t\t\t\t\t Date Of Item rented = {formatted_date}\n"
    bill_text += f"\t\t\t\t\t\t\t\t   Rented Time = {formatted_time}\n"
    bill_text += "=" * 92+"\n"
    bill_text += "\t\t\t\t KuruKuru Rental Shoppers"+"\n"
    bill_text += "\t\t\t\t 9863033719,Bhotahity,Ason"+"\n"
    bill_text += "\t\t\t\t\t Rent Bill"+"\n"
    bill_text += "="*92+"\n"
    bill_text += f"\t\t\t\t\t\t\tCustomer Name : "+customername + "\n"
    bill_text += "="*92+"\n"
    bill_text += f"|\tItem Name   \t|   Brand Name\t\t| Quantity | price per item | Total amount |\n"
    bill_text += "="*92+"\n"
    for item in data: 
        
        item_line = "{:<20}\t{:<15}\t{:>8}\t{:>13}\t{:>11}".format(item['name'], item['brand'], item['quantity'], f"${item['price']:.2f}", f"${item['total']:.2f}\n")
        bill_text +=item_line
    bill_text += "="*92+"\n"
    bill_text += f"\t\t\t\t\t\t\t\t Grand Total: ${grand_total}\n"
    bill_text += "="*92+"\n"
    
    # Write the bill to a new file
    file_name = "Rent"+customername+"_"+month+day+hour+minute+".txt"
    with open(file_name, "w") as file:
        file.write(bill_text)

    print("Bill generated and written to", file_name)
    print("\n")
    return bill_text

def returnbill(data):
    '''
    this program ask for the days late while returning
    item and print invoice of bill in new file and
    manage how data is kept in the invoice

    '''
    try:
        dayslateing=int(input("Enter how many late did you renturn the item?"))
        customername=data[0]['customerName']
        print(customername)
        fine=0
        total_returnamount=0
        formatted_date = day+"-"+month+"-"+year
        formatted_time = hour+"~"+month+"~"+sec
    # Calculate total for each transaction
        for item in data:
            fine=dayslateing*(item['price']/5)+fine
            item['total'] = item['price'] * item['quantity']
            total_returnamount=fine+item['total']
            
        # Create a formatted bill
        bill_text = " ==========Kurukuru Returned item BILL===========\n\n"
        bill_text += "="*92 +"\n"
        bill_text += f"\t\t\t\t\t\t\t Date Of Item Returned = {formatted_date}\n"
        bill_text += f"\t\t\t\t\t\t\t\t   Returned Time = {formatted_time}\n"
        bill_text += "=" * 92+"\n"
        bill_text += "\t\t\t\t KuruKuru Rental Shoppers"+"\n"
        bill_text += "\t\t\t\t 9863033719,Bhotahity,Ason"+"\n"
        bill_text += "\t\t\t\t\t Return Bill"+"\n"
        bill_text += "="*92+"\n"
        bill_text += f"\t\t\t\t\t\t\tCustomer Name : "+customername + "\n"
        bill_text += "="*92+"\n"
        bill_text += f"|\tItem Name   \t|   Brand Name\t\t| Quantity | price per item | Total amount |\n"
        bill_text += "="*92+"\n"
        for item in data:
            item_line = "{:<20}\t{:<17}\t{:>5}\t{:>10}\t{:>11}".format(item['name'], item['brand'], item['quantity'], f"${item['price']:.2f}", f"${item['total']:.2f}\n")
            bill_text +=item_line
        bill_text += "="*92+"\n"
        bill_text += "\n"
        bill_text += f"\t\t\t\t\t\t\t\t\t\t Fine: ${fine}\n"
        bill_text += f"\t\t\t\t\t\t\t\t\t Grand Total: ${total_returnamount}\n"
        bill_text += "="*92+"\n"

        # Write the bill to a new file
        file_name = "Return"+customername+"_"+month+day+hour+minute+".txt"
        with open(file_name, "w") as file:
            file.write(bill_text)

        print("Bill generated and written to", file_name)
        print("\n")
        return bill_text
    except:
        print("=========his datatype cant be taken. Re-enter the value=========")