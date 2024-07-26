# module to read the file's information
def read_file():
    '''
    This file read the item in the DataFIle.txt and adds it to a
    dictionary and addes key value to identify each product differently
    '''
    gear_file = open("dataFile.txt", "r")
    gear_dictionary = {}
    gear_ID = 1
    
    for i in gear_file:
        #strip removes all the white space and line break
        #split to seperate data and mange data
        i = i.strip().split(',')
        name = i[0]
        brand = i[1]
        price = float(i[2].replace('$',' '))
        quantity = int(i[3])
        gear_dictionary[gear_ID]={'name':name,'brand':brand,'price':price,'quantity':quantity}
        gear_ID = gear_ID+1
    gear_file.close()
    #returns gear dictionary when call
    return gear_dictionary

'''
    for_table function takes the manage data to a proper table
    so user can understand the data properly

'''
def for_table():

        table_dicti = read_file()
        print("\n")
        print("|"+ "x" * 10 + "|" +
            "x" * 21 + "|"+
            "x" * 18 + "|"+
            "x" * 10 + "|"+
            "x" * 10 + "|")
        # for header of the table
        print("| {:<8} | {:<19} | {:<16} | {:<8} | {:<8} |".format("Item Id", "Item", "Company", "Rate", "Quantity"))
        print("|" + "x" * 10 + "|" + "x" * 21 + "|" + "x" * 18 + "|" + "x" * 10 + "|" + "x" * 10 + "|")
        for key, values in table_dicti.items():
            val = ("| {:<8} | {:<19} | {:<16} |{:<8}$ | {:<8} | "
                   .format(str(key), str(values['name']), str(values['brand']), str(values['price']),
                           str(values['quantity'])))
            print(val)
        print("|" + "x" * 73 + "|")

