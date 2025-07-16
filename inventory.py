# Craig Selbrede 07/10/2025


#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        """Create a Shoe object.
        country = The country of origin of the shoe.
        code = The SKU code of the shoe.
        product = The specific type of shoe.
        cost = the cost to manufacture the shoe.
        quantity = The current stock of the shoe.
        """
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''


    def get_cost(self):
        """Return the cost of the shoe."""
        return self.cost
        '''
        Add the code to return the cost of the shoe in this method.
        '''


    def get_quantity(self):
        """Return the quantity of the shoe."""
        return int(self.quantity)
        '''
        Add the code to return the quantity of the shoes.
        '''


    def __str__(self):
        """Return a String version of the object Shoe."""
        return ("Country: "+self.country+", Code: "+self.code+", Product: "+self.product
                +", Cost: "+self.cost+", Quantity: "+self.quantity+"!")
        '''
        Add a code to returns a string representation of a class.
        '''


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []

#==========Functions outside the class==============
def read_shoes_data():
    """Read in shoe data from a file into a list."""
    file = open('inventory.txt', "r+")
    i = 0
    try:
        for line in file:
                if i > 0:

                    this_line=line.split(",")
                    shoe_list.append(Shoe(this_line[0], this_line[1], this_line[2],
                              this_line[3], this_line[4]))
                i+=1

        file.close()
    except FileNotFoundError as error:
        print("The file does not exist.") 
        print(error)
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''


def capture_shoes():
    """Create a new shoe object and add it to the list and the file."""
    country = input("Enter a country: ")
    code = input("Enter a code: ")
    product = input("Enter a product: ")
    while True:
        try:
            cost = input("Enter a cost: ")
            test_cost = int(cost)
            break
        except Exception:
            print("Oops! Not a valid entry, please try again.")

    while True:
        try:
            quantity = input("Enter a quantity: ")
            test_quant = int(quantity)
            break
        except Exception:
            print("Oops! Not a valid entry, please try again.")
            
    shoe_list.append(Shoe(country, code, product, cost, quantity))
    file = open('inventory.txt', "a+")
    file.write("\n"+country+","+code+","+product+","+cost+","+quantity)
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    file.close()



def view_all():
    """Print all the Shoe objects in shoe_list."""
    for i in range(0, len(shoe_list)):
        print(str(shoe_list[i]))
        i+=1
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''

def re_stock():
    """Print the lowest quantity Shoe and subsequently update its stock."""
    min = shoe_list[0].get_quantity()
    min_index = 0
    for i in range(1, len(shoe_list)):
        if shoe_list[i].get_quantity() < min:
            min = shoe_list[i].get_quantity()
            min_index = i
        i+=1
    print(str(shoe_list[min_index])+" are the details for the shoe with the lowest quantity.")
    updated_stock = input("How much stock would you like to add? ")
    shoe_list[min_index].quantity = str(int(shoe_list[min_index].quantity)+
                                        int(updated_stock))+"\n"
    file = open('inventory.txt', "w+")
    i = 0
    try:
        file.write("Country,Code,Product,Cost,Quantity\n")
        for i in range (0, len(shoe_list)):
            file.write(shoe_list[i].country+","+shoe_list[i].code+","+shoe_list[i].product
                       +","+shoe_list[i].cost+","+shoe_list[i].quantity)
            i+=1
        file.close()
    except FileNotFoundError as error:
        print("The file does not exist.") 
        print(error)
    
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''


def search_shoe(code):
    """Search for a shoe with a specific code.
    code = the code you are searching for."""
    for i in range(0, len(shoe_list)):
        if(shoe_list[i].code==code):
            return(str(shoe_list[i]))
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''

def value_per_item():
    """Iterate over the list, calculating the value per item and printing it."""
    for i in range(0, len(shoe_list)):
        value = int(shoe_list[i].quantity) * int(shoe_list[i].cost)
        print(str(shoe_list[i].product)+" has a value of $"+str(value))
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''


def highest_qty():
    """Iterate over the list, finding the highest quantity shoe and printing its details."""
    max = shoe_list[0].get_quantity()
    max_index = 0
    for i in range(1, len(shoe_list)):
        if shoe_list[i].get_quantity() > max:
            max = shoe_list[i].get_quantity()
            max_index = i
        i+=1
    print(str(shoe_list[max_index])+
          " are the details for the shoe with the highest"
          " quantity! They're for sale.")
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
Finished = False
while Finished == False:
    print("Would you like to...")
    print("A. ...read the shoe data?")
    print("B. ...add a shoe?")
    print("C. ...view all shoes?")
    print("D. ...restock a low quantity shoe?")
    print("E. ...find a shoe by code?")
    print("F. ...see the values per item?")
    print("G. ...view the item with the highest quantity?")
    result = input("X. ... exit the menu?:  ")
    if result == 'A':
        read_shoes_data()
        print()
    if result == 'B':
        capture_shoes()
        print()
    if result == 'C':
        view_all()
        print()
    if result == 'D':
        re_stock()
        print()
    if result == 'E':
        code = input("Enter a code: ")
        print(search_shoe(code))
        print()
    if result == 'F':
        value_per_item()
        print()
    if result == 'G':
        highest_qty()
        print()
    if result == 'X':
        Finished = True
