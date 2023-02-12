## finalCapstone Project
-----------------------------------------------------------------------------------------------------------------------------------------

#### About the project:
-----------------------
A Python program that reads and prepares shoe data from 'inventory.txt' for presentation to managers,  used to manage a Nike warehouse's stock taking. Uses the Shoes class with attributes country, code, product, cost, and quantity, and methods such as get_cost, get_quantity, and str. Defines functions outside the class to perform operations on the data.

-----------------------------------------------------------------------------------------------------------------------------------------

#### **Contents:**
#### 1. Project Description
#### 2. Code Syntax, Installation and Use
#### 3. Credits
-----------------------------------------------------------------------------------------------------------------------------------------

#### 1. Project Description
-----------------------
The program is written in Python and is used to manage a Nike warehouse's stock taking. It allows the user to perform various operations on the data stored in a text file named "inventory.txt"

#### 2. Code Syntax, Installation and Use
#### 2.1. Code Syntax
-----------------------
The program consists:
1) Shoes: This class represents a shoe object and has the following attributes: country: The country where the shoe is manufactured code: The code assigned to the shoe product: The name of the product cost: The cost of the shoe quantity: The quantity of the shoes available
This class also contains the following methods:
- get_cost: Returns the cost of the shoe
- get_quantity: Returns the quantity of the shoe
- str: Returns a string representation of the class
- A list named "shoes" to store the shoe objects.
2) There are also several functions outside the class, which are:
- read_shoes_data: This function reads data from the "inventory.txt" file, creates a shoe object with this data and appends it to the "shoes" list.
- capture_shoes: This function allows the user to capture data about a shoe, creates a shoe object, and appends it to the "shoes" list.
- view_all: This function iterates over the "shoes" list and prints the details of each shoe object.
- re_stock: This function finds the shoe object with the lowest quantity, asks the user if they want to add to this quantity, and updates the file for this shoe.
- search_shoe: This function searches for a shoe in the list using its code and returns the object.
- value_per_item: This function calculates the total value of each item by multiplying the cost and quantity and prints this information on the console.
- highest_qty: This function determines the product with the highest quantity and prints it as being for sale.


#### 2.2. Installation
-----------------------
Pre-requisites: This program does not require the installation of any Module libraries.
Usage: To start the program, type the following command into the terminal:

> python inventory.py


#### 2.3. Use
-----------------------
The program will display a menu with eight options:

![image](https://user-images.githubusercontent.com/57161263/218339123-7f8c5f97-bc65-465f-8ebc-26a142a128e1.png)


> #### OPTION 01: Read shoes data from file
This option will read the data from the file named 'inventory.txt' and stores it in memmory prompting the user:

![image](https://user-images.githubusercontent.com/57161263/218339580-bb3135af-3240-495e-bbdc-aff18aa3bde7.png)

No other option will work unless the file 'inventory.txt' is pre-loaded. If the file is not preloaded the following massage will be depicted, upon selection of any remaining option:

![image](https://user-images.githubusercontent.com/57161263/218339545-2eb1f7a0-88b8-4168-b1fb-11a935634594.png)


> #### OPTION 02: Register new shoes data
This option adds new data to the shoe list for the new shoes that are to be added to the inventory.
It will prompt the user to enter, the coutry, the shoes code, the product name, the cost and the quatity to be added to the inventory

![image](https://user-images.githubusercontent.com/57161263/218340158-183672d3-413b-4924-8c7e-476e79cef8e4.png)

Once the above data is introduced a message is displayed to inform the user.

_Note: if -1 is typed at any of the above prompts, the program will return to the Main Menu_


> #### OPTION 03: View all shoes data
This option is used to view all the shoes data stored in the shoe_list inventory.

![image](https://user-images.githubusercontent.com/57161263/218340474-094eb8f6-186f-427f-95a3-71411006ffc8.png)


> #### OPTION 04: Update/Re-stock shoes quantity
This option will update the quantity of shoes selected by the user in the inventory.
The programme will list the three shoe products with the lowest quantity and suggest which shoes should be restocked.
Once the product has been identified, the programme will request that the amount be restocked and will notify the user accordingly.

![image](https://user-images.githubusercontent.com/57161263/218340558-4e92d7e0-13e4-40b7-98ca-1501248e2f30.png)

_Note: if -1 is typed at any of the above prompts, the program will return to the Main Menu_


> #### OPTION 05: Search for shoes by shoes code
This option will allow the user to search for a shoe by entering a code in the form of "SKU00000".

![image](https://user-images.githubusercontent.com/57161263/218340962-991e535f-9927-4de6-b923-1cc6003a3cb5.png)

_Note: if -1 is typed at any of the above prompts, the program will return to the Main Menu_


> #### OPTION 06: View total cost values for each product 
This option will calculate the total value of the shoes in stock by multiplying the cost of each item by its quantity and display it accordingly.

![image](https://user-images.githubusercontent.com/57161263/218341046-331b58da-9579-4634-a4fb-a76296a869e2.png)


> #### OPTION 07: Highest quantity shoes for sale 
This option will output the highest quantity of shoes item for sale.

![image](https://user-images.githubusercontent.com/57161263/218341090-43a54fef-ab4a-40c2-83c0-9a3c549ffe57.png)


> #### OPTION 08: Exit 
This option will terminate the program and advise the user.

![image](https://user-images.githubusercontent.com/57161263/218341164-04038f42-e939-4e2d-b22a-5fdc1f7d0a42.png)


#### 3. Credits
-----------------------
Created by Fernando Vinagre
