##Python file: inventory.py
# For a better output visualisation, please open this file in PyCharm, Thank you.

#=====General variables for constant use===========
# General variables declared - for text formatting - to be used throughout the program.
WHITE = "\033[0m"
ORANGE = "\033[33m"
PURPLE = "\033[35m"
GREY = "\033[37m"
DARKGREY = "\033[90m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
DARKCYAN = "\033[36m"
ITALIC_S = "\x1B[3m"
ITALIC_E = "\x1B[0m"


#========The beginning of the class==========
# Definition of class Shoes.
class Shoes:
    # The class has five instance variables: "country", "code", "product", "cost", and "quantity". These instance
    # variables are set in the constructor method "init".
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # The class has the method "get_cost" which return the values of the "cost" instance variable.
    def get_cost(self):
        return self.cost

    # The class has the methods "get_quantity" which return the values of the "quantity" instance variable.
    def get_quantity(self):
        return self.quantity

    # the class has a special method "str", which returns a formatted string that represents the instance of the class.
    # When this object is passed to the "print" function, the "str" method is called and its returned string is printed
    def __str__(self):
        return f'Country: {self.country}\n' \
               f'Code: {self.code}\n' \
               f'Product: {self.product}\n' \
               f'Cost: {self.cost}\n' \
               f'Quantity: {self.quantity}'


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
#  Global shoe_list list to store the data read from the file.
shoe_list = []


#==========Functions outside the class==============
# function read_shoes_data() that reads data from the file named 'inventory.txt' and stores it in a list shoe_list.
def read_shoes_data():
    # try-except block to handle any exceptions that may occur during the process of reading the file.
    try:
        # with statement to open the file in read mode.
        with open('inventory.txt', 'r', encoding='utf-8-sig') as f:
            # The file is read using the readlines method, which returns a list of strings, where each string is a line
            # from the file.
            lines = f.readlines()
            # for loop to iterate over the lines, and if the line number is 0, it continues to the next iteration.
            for i, line in enumerate(lines):
                if i == 0:
                    continue
                # For each line, the code splits the line using the split method with a comma separator, and assigns
                # the resulting values to the variables country, code, product, cost, and quantity.
                country, code, product, cost, quantity = line.strip().split(',')
                # The values of cost and quantity are converted to a float and int respectively using the float
                # and int functions.
                cost = float(cost)
                quantity = int(quantity)
                # The values are appended to the shoe_list as a Shoes object.
                shoe_list.append(Shoes(country, code, product, cost, quantity))
            print(f"{GREEN}Inventory \'inventory.txt\' has been read Successfully.{WHITE}")
    # If an exception occurs, the code will print an error message with the exception message.
    except Exception as e:
        print(f"{RED}Error: {e}.{WHITE}")


# The not_shoe_list() function checks if the shoe_list is empty and prints an error message if it is.
def not_shoe_list():
    if not shoe_list:
        print(f"{RED}Please read the file \'inventory.txt\' first by choosing choice 1 from the main menu.{WHITE}")


# The capture_shoes() function captures data for new shoes to be added to the inventory and appends it to the shoe_list.
def capture_shoes():
    # The function calls the not_shoe_list() function to check if the shoe_list is empty and display an error
    # message accordingly.
    not_shoe_list()
    if shoe_list:
        print(f"─────────────────────────────────────────────────────────────────────────────────────\n"
              f"│{CYAN}{'REGISTER NEW SHOES DATA':^{83}}{WHITE}│\n"
              f"─────────────────────────────────────────────────────────────────────────────────────\n"
              f"{ITALIC_S}{DARKGREY}"
              f"{'==> Note: To return to the Main Menu, enter -1 at any of the options below. <==':^{83}}"
              f"{WHITE}{ITALIC_E}")
        # Request the user for the country, code, product, cost, and quantity to register new shoes data.
        # for each field, if the user enters -1, the function returns.
        country = input(f"Please enter the country:\t\t")
        if country == "-1":
            return
        code = input(f"Please enter the shoes code\n"
                     f"(In the format of SKU00000):\t")
        if code == "-1":
            return
        product = input(f"Please enter the product name:\t")
        if product == "-1":
            return
        cost = float(input(f"Please enter the cost:\t\t\t"))
        if cost == -1:
            return
        quantity = int(input(f"Please enter the quantity of \'{product}\' shoes:\t"))
        if quantity == -1:
            return
        # The new shoes data is appended to the shoe_list as a Shoes object.
        shoe_list.append(Shoes(country, code, product, cost, quantity))
        # Open the file inventory.txt in append mode and writes the new shoes data to the file using the append method.
        with open('inventory.txt', 'a', encoding='utf-8-sig') as f:
            f.write(f"\n{country},{code},{product},{cost},{quantity}")
        print(f"{GREEN}{quantity} units of '{product}\' shoes have been added to the \'inventory.txt\' Successfully.{WHITE}")

# The view_all function is used to view all the shoes data stored in the shoe_list.
def view_all():
    # The function calls the not_shoe_list() function to check if the shoe_list is empty and display an error
    # message accordingly.
    not_shoe_list()
    # If the shoe_list is not empty, it prints a table that provides information about the data.
    if shoe_list:
        print(f"─────────────────────────────────────────────────────────────────────────────────────\n"
              f"│{YELLOW}{'VIEW ALL SHOES DATA':^{83}}{WHITE}│\n"
              f"─────────────────────────────────────────────────────────────────────────────────────")
        # It prints the table header.
        print(f"│{'Country:':^{18}}"
              f"│ {'Code:':^{12}}"
              f"│ {'Product:':^{24}}"
              f"│ {'Cost (R ):':^{14}}"
              f"│ {'Stock:':^{7}}│")
        print("─" * 85)
        # for loop to iterate over the shoe_list and print the data for each shoe.
        for shoes in shoe_list:
            # The data is printed in the format specified in the f-string inside the print statement. The f-string uses
            # placeholders to insert values into the string. The values are obtained from the attributes of the
            # shoes object.
            print(f"│{shoes.country:^{17}} "
                  f"│{shoes.code:^{12}} "
                  f"│{shoes.product:^{25}}"
                  f"│{shoes.cost:^{15},.2f}"
                  f"│{shoes.quantity:^{8}}│")


# The function re_stock() updates the quantity of shoes in the inventory.
def re_stock():
    # The function calls the not_shoe_list() function to check if the shoe_list is empty and display an error
    # message accordingly.
    not_shoe_list()
    # If the shoe list exists.
    if shoe_list:
        print(f"─────────────────────────────────────────────────────────────────────────────────────\n"
              f"│{MAGENTA}{'UPDATE/ RE-STOCK SHOES QUANTITY':^{83}}{WHITE}│\n"
              f"─────────────────────────────────────────────────────────────────────────────────────\n"
              f"{ITALIC_S}{DARKGREY}"
              f"{'==> Note: To return to the Main Menu, enter -1 at any of the options below. <==':^{83}}"
              f"{WHITE}{ITALIC_E}")
        # Finds the three shoes with the lowest quantity in the inventory by looping through all the shoes in the list
        # and updating the minimum quantity and corresponding shoe if it finds a shoe with a lower quantity.
        shoes_to_restock = []
        for i in range(3):
            min_quantity = float('inf')
            restock_shoe = None
            for shoes in shoe_list:
                if shoes.get_quantity() < min_quantity and shoes not in shoes_to_restock:
                    min_quantity = shoes.get_quantity()
                    restock_shoe = shoes
            if restock_shoe:
                shoes_to_restock.append(restock_shoe)

        # If shoes with the lowest quantity are found, it prompts the user to choose which shoe they want to re-stock.
        if shoes_to_restock:
            print(f"Current the below shoes have the lowest quantity:")
            print("─" * 85)
            print(f"│ {'Ref.:':^{12}}│ "
                  f"{'Code:':^{12}}│ "
                  f"{'Product:':^{40}}│ "
                  f"{'Stock:':^{12}}│")
            print("─" * 85)
            for i, shoes in enumerate(shoes_to_restock):
                print(f"│ {i + 1:^{12}}│ "
                      f"{shoes.code:^{12}}│ "
                      f"{shoes.product:^{40}}│ "
                      f"{shoes.quantity:^{12}}│")
            print("─" * 85)
            # Asks the user which shoe they want to restock by printing a list of shoes with the lowest quantity and a
            # prompt for the user to choose one of the shoes. The reference number input by the user is then verified
            # to ensure it is a digit and within the range of the shoes in the list.
            reference = input("Which shoes would you like to restock?\n"
                              "Please choose one of the Ref. numbers listed above.\n"
                              ":")
            # If the user enters -1, the function returns.
            if reference == "-1":
                return
            # The reference number of the chosen shoe is checked, and if it's invalid, an error message is printed, and
            # the function returns.
            if not reference.isdigit() or int(reference) > len(shoes_to_restock) or int(reference) <= 0:
                print(f"{RED}Invalid reference number, please try again.{WHITE}")
                return
            chosen_shoe = shoes_to_restock[int(reference) - 1]
            # If the reference number is valid, the user is asked to enter the quantity of shoes to add.
            quantity = input(f"Please enter the quantity of \'{chosen_shoe.product}\' shoes to add: ")
            # If the user enters -1, the function returns.
            if quantity == "-1":
                return
            chosen_shoe.quantity += int(quantity)
            # The chosen shoe's quantity is updated, and the shoe inventory is updated in the file inventory.txt.
            with open('inventory.txt', 'w', encoding='utf-8-sig') as f:
                f.write("country,code,product,cost,quantity\n")
                for shoes in shoe_list:
                    f.write(f"{shoes.country},{shoes.code},{shoes.product},{shoes.cost},{shoes.quantity}\n")
            # Informs the user using a success message to confirm the update was successful
            print(f"{GREEN}Stock quantities of {chosen_shoe.product} have been Successfully updated.\n"
                  f"Current stock of {chosen_shoe.product} is {chosen_shoe.quantity}.{WHITE}")
        # If no shoes to re-stock are found, an error message is printed.
        else:
            print(f"{RED}No shoes to re-stock.{WHITE}")


# The function search_shoe allows the user to search for a shoe by entering a code in the form of "SKU00000".
def search_shoe():
    # The function calls the not_shoe_list() function to check if the shoe_list is empty and display an error
    # message accordingly.
    not_shoe_list()
    # If the "shoe_list" exists
    if shoe_list:
        print(f"─────────────────────────────────────────────────────────────────────────────────────\n"
              f"│{ORANGE}{'SEARCH FOR SHOES (BY SHOES CODE)':^{83}}{WHITE}│\n"
              f"─────────────────────────────────────────────────────────────────────────────────────\n"
              f"{ITALIC_S}{DARKGREY}"
              f"{'==> Note: To return to the Main Menu, enter -1 at any of the options below. <==':^{83}}"
              f"{WHITE}{ITALIC_E}")
        # it prompts the user to enter the shoes code.
        code = input(f"Please enter the shoes code to search (in the form of: SKU00000): ")
        # If the user enters -1, the function returns immediately.
        if code == "-1":
            return
        print(f"{GREEN}The below shoes have been found with the code \'{code}\':{WHITE}")
        print("─" * 85)
        shoes_found = False
        # It loops through the "shoe_list" to find a shoe that matches the entered code.
        for shoes in shoe_list:
            # If a match is found, the function prints the details of the shoe such as its country, code, product,
            # cost, and stock.
            if shoes.code == code:
                shoes_found = True
                print(f"│ {'Attribute:':^{40}}│ {'Value:':^{40}}│")
                print("─" * 85)
                print(f"│ {'Country:':^{40}}│ {shoes.country:^{40}}│")
                print(f"│ {'Code:':^{40}}│ {shoes.code:^{40}}│")
                print(f"│ {'Product:':^{40}}│ {shoes.product:^{40}}│")
                print(f"│ {'Cost (R ):':^{40}}│ {shoes.cost:^{40},.2f}│")
                print(f"│ {'Stock (units):':^{40}}│ {shoes.quantity:^{40}}│")
                break
        # If no match is found, the function prints a message accordingly.
        if not shoes_found:
            print(f"{RED}Shoes with code '{code}' not found.{WHITE}")

# The function value_per_item calculates the total value of the shoes in stock by multiplying the cost of each item by
# its quantity.
def value_per_item():
    # The function calls the not_shoe_list() function to check if the shoe_list is empty and display an error
    # message accordingly.
    not_shoe_list()
    # If the "shoe_list" exists
    if shoe_list:
        print(f"─────────────────────────────────────────────────────────────────────────────────────\n"
              f"│{DARKCYAN}{'CURRENT STOCK (TOTAL VALUES FOR EACH PRODUCT)':^{83}}{WHITE}│\n"
              f"─────────────────────────────────────────────────────────────────────────────────────")
        # It initializes the "total_value" variable to 0
        total_value = 0
        print(f"Values for the Shoes items in stock:")
        # It outputs a table header
        print("─" * 85)
        print(f"│ {'Code:':^{10}}"
              f"│ {'Product:':^{20}}"
              f"│ {'Stock:':^{11}}     {'Cost (R):':^{12}}     {'Total Cost (R):':^{15}}│")
        print("─" * 85)
        # it loops through the "shoe_list" and calculates the value of each shoe by calling the "get_cost" and
        # "get_quantity" methods of each shoe object and multiplying them.
        for shoes in shoe_list:
            value = shoes.get_cost() * shoes.get_quantity()
            # It outputs the information oin the form of a table.
            print(f"│ {shoes.code:^{10}}"
                  f"│ {shoes.product:^{20}}"
                  f"│ {shoes.quantity:^{11}}"
                  f"  x  {shoes.cost:^{12},.2f}"
                  f"  =  {value:^{15},.2f}│")
            # The function then adds the value of each shoe to the "total_value" and prints it to the table.
            total_value += value
        print("─" * 85)
        print(f"│ {' ':^{32}}"
              f"│ {'Total stock value (R):':^{33}}"
              f"{total_value:^{15},.2f}│")


# The function highest_qty outputs the highest quantity of shoes item for sale.
def highest_qty():
    # The function calls the not_shoe_list() function to check if the shoe_list is empty and display an error
    # message accordingly.
    not_shoe_list()
    # If the "shoe_list" exists
    if shoe_list:
        print(f"─────────────────────────────────────────────────────────────────────────────────────\n"
              f"│{PURPLE}{'HIGHEST QUANTITY OF SHOES ITEM FOR SALE':^{83}}{WHITE}│\n"
              f"─────────────────────────────────────────────────────────────────────────────────────")
        # Initial code, however it was identifying one product with higher value and not various with the same quantity
        # max_qty = 0
        # max_shoe = None
        # for shoes in shoe_list:
        #     if shoes.get_quantity() > max_qty:
        #         max_qty = shoes.get_quantity()
        #         max_shoe = shoes
        # if max_shoe:
        #     print(f"The below shoes product has the highest quantity:")
        #     print("─" * 85)
        #     print(f"│ {'Product:':^{40}}│ {'Stock:':^{40}}│")
        #     print("─" * 85)
        #     print(f"│ {max_shoe.product:^{40}}│ {max_shoe.get_quantity():^{40}}│")
        # else:
        #     print(f"{RED}No shoes found.{WHITE}")

        # It calculates the maximum quantity of shoes by using a list comprehension to get the quantity of each shoe in
        # shoe_list, and getting the maximum value using the max function.
        max_qty = max([shoe.get_quantity() for shoe in shoe_list])
        # It creates a list of shoes that have the maximum quantity.
        max_shoes = [shoe for shoe in shoe_list if shoe.get_quantity() == max_qty]
        # It checks if the list is not empty.
        if max_shoes:
            # If it's not empty and contains a single higher cost, it prints the code, product, and quantity of
            # those shoes.
            if len(max_shoes) == 1:
                max_shoe = max_shoes[0]
                print(f"The below shoes product has the highest quantity:")
                print("─" * 85)
                print(f"│ {'Code:':^{18}}│ {'Product:':^{40}}│ {'Stock:':^{20}}│")
                print("─" * 85)
                print(f"│ {max_shoe.code:^{18}}│ {max_shoe.product:^{40}}│ {max_shoe.get_quantity():^{20}}│")
            # If it contains several shoes with the same higher cost, it loops through the list and prints the code,
            # product, and quantity of each shoe.
            else:
                print(f"The below shoes products have the highest quantity:")
                print("─" * 85)
                print(f"│ {'Code:':^{18}}│ {'Product:':^{40}}│ {'Stock:':^{20}}│")
                print("─" * 85)
                for max_shoe in max_shoes:
                    print(f"│ {max_shoe.code:^{18}}│ {max_shoe.product:^{40}}│ {max_shoe.get_quantity():^{20}}│")
        # If the list is empty, it prints a message accordingly.
        else:
            print(f"{RED}No shoes found.{WHITE}")


#==========Main Menu=============
# Through a while loop, it continuously displays a main menu to the user and waits for the user's choice.
while True:
    # The options are displayed using the print statement with format strings.
    # The f at the beginning of each print statement indicates that the string is a formatted string.
    # The curly braces {} are used to insert values into the string.
    # The :^{83}} part is used to center the text within a 83 character wide field.
    # This table representation is similarly used throughout the above code.
    print(f"─────────────────────────────────────────────────────────────────────────────────────\n"
          f"│{BLUE}{'MAIN MENU':^{83}}{WHITE}│\n"
          f"─────────────────────────────────────────────────────────────────────────────────────\n"
          f"│{'[ 1. ] - Read shoes data from file              ':^{83}}│\n"
          f"│{'[ 2. ] - Register new shoes data                ':^{83}}│\n"
          f"│{'[ 3. ] - View all shoes data                    ':^{83}}│\n"
          f"│{'[ 4. ] - Update/Re-stock shoes quantity         ':^{83}}│\n"
          f"│{'[ 5. ] - Search for shoes by shoes code         ':^{83}}│\n"
          f"│{'[ 6. ] - View total cost values for each product':^{83}}│\n"
          f"│{'[ 7. ] - Highest quantity shoes for sale        ':^{83}}│\n"
          f"│{'[ 8. ] - Exit                                   ':^{83}}│")
    print("─" * 85)
    # The selected choice is stored in the choice variable which is obtained through an input function.
    choice = int(input('Enter your choice: '))
    # if-elif statements to call different functions depending on the user's choice.
    if choice == 1:
        read_shoes_data()
    elif choice == 2:
        capture_shoes()
    elif choice == 3:
        view_all()
    elif choice == 4:
        re_stock()
    elif choice == 5:
        search_shoe()
    elif choice == 6:
        value_per_item()
    elif choice == 7:
        highest_qty()
    elif choice == 8:
        print(f"{ITALIC_S}{GREEN}Thank you. Good Bye!{WHITE}{ITALIC_E}")
        break
    # If the user enters an invalid choice, a message is printed accordingly.
    else:
        print(f"{RED}Invalid Menu choice. Please try again.{WHITE}")
