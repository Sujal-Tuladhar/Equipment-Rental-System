# def rent_write(data):
def rent_write(data):
    '''
    this function helps in changing the value of
    the text file while rent and return and access dictionary to
    get and change value in the code

    '''
    #2D list created to store value for gear list
    formatted_gear_list = []

    for key, values in data.items():
        formatted_gear = f"{values['name']},{values['brand']},${values['price']:.2f},{values['quantity']}"
        #append to store value in the 2D list
        formatted_gear_list.append(formatted_gear)
    #Join to join two values
    formatted_gear_text = "\n".join(formatted_gear_list)
    #opening file to write in the file
    with open("dataFile.txt", 'w') as file:
        file.write(formatted_gear_text)
 

    

