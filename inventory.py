'''SE T32 - Capstone Project IV -- OOP
Compulsory Task
'''
#=====importing libraries===========


#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        pass
        return f'Product: {self.product}. Code: {self.code}. Country of origin: {self.country}. Cost: {self.cost}. Quantity: {self.quantity}.'


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []

#==========Functions outside the class==============
def read_shoes_data():
	'''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
	inv_file = open('inventory.txt', 'r', encoding = 'utf-8')
	for line in inv_file.read().split("\n")[1:]: # Read inventory.tx and skips first line
		try:
			country, code, product, cost, quantity = line.split(',')
			new_shoe = Shoe(country, code, product, cost, quantity)
			shoe_list.append(new_shoe)
		except Exception as e: # Catch exceptions
			print(e)
		finally:
			pass
	inv_file.close()
	
	return
	#end of read_shoes_data()

def capture_shoes():
	'''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
	try:
		new_country = input("Enter country: ")
		new_code = input("Enter code: ")
		new_product = input("Enter product name: ")
		new_cost = int(input("Enter cost: "))
		new_quantity = int(input("Enter quantity: "))
	except Exception as e: # Catch exceptions
		print(e)
	else:
		new_shoe = Shoe(new_country, new_code, new_product, new_cost, new_quantity)
		shoe_list.append(new_shoe)
	# End of capture_shoes()

def view_all():
	'''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
	for shoe in shoe_list:
		print(shoe.__str__())
	# End of view_all()

def re_stock():
	'''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
	quantity_list = [] # list of shoe quantities
	for shoe in shoe_list: # iterates through shoe list
		quantity_list.append(int(shoe.quantity))
	min_quant = min(quantity_list) # find lowest quantity
	min_quant_pos = quantity_list.index(min_quant) # position of shoe with lowest quantity
	min_quant_shoe = shoe_list[min_quant_pos]
	print('Product with the lowest quantity:')
	print(min_quant_shoe)

	'''Ask user if they want to change quantity of shoe'''
	while True:
		user_choice = input("Would you like to update quantity? (y/n): ")
		if (user_choice == 'y'):
			try:
				'''User can update the quantity'''
				new_quant = int(input("Enter new quantity: "))

			except Exception as e: # Catch exception
				print(e)

			else: # If there is no exception
				existing_shoe = f"{min_quant_shoe.country},{min_quant_shoe.code},{min_quant_shoe.product},{min_quant_shoe.cost},{min_quant_shoe.quantity}"
				updated_shoe = f"{min_quant_shoe.country},{min_quant_shoe.code},{min_quant_shoe.product},{min_quant_shoe.cost},{new_quant}"
				with open('inventory.txt', 'r', encoding = 'utf-8') as inv_file: #reads the file
					mod_inv_file = inv_file.read() #copy the file
					mod_inv_file = mod_inv_file.replace(existing_shoe, updated_shoe) #replace the existing shoe with updated shoe (quantity changed by user)
				with open('inventory.txt', 'w', encoding = 'utf-8') as inv_file2: 
					inv_file2.write(mod_inv_file) #overwrites the file
				return(f"Updated!\n{updated_shoe}")
				#end of update the quantity of shoe

		elif (user_choice == 'n'): # leave the menu
			break
		else: # If neither y or n is entered
			print('Sorry. Input not recognised.')
	# End of re_stock()

def seach_shoe(search_code):
	'''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
	for shoe in shoe_list: # iterates through shoe list
		if (shoe.code == search_code): # finds matching code
			found_shoe = shoe
			return found_shoe # returns the search result
		else:
			pass
	# End of search_shoe()

def value_per_item():
	'''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
	for shoe in shoe_list: # iterates through shoe list
		value = int(shoe.cost) * int(shoe.quantity)
		print(f'''{shoe.product}:		{value}''')
	# end of value_per_item()

def highest_qty():
	'''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
	quantity_list = [] # list of shoe quantities
	for shoe in shoe_list: # iterates through shoe list
		quantity_list.append(int(shoe.quantity))
	max_quant = max(quantity_list) # find highest quantity
	max_quant_pos = quantity_list.index(max_quant) # position of shoe with highest quantity
	max_quant_shoe = shoe_list[max_quant_pos]
	print(f'{max_quant_shoe.product} has {max_quant_shoe.quantity} in stock.')
	print(f'{max_quant_shoe.product} is on sale.')
	# End of highest_qty()

#==========Main Menu=============
'''
Allow the user to choose from the menu.
'''
while True:
	read_shoes_data() # adds shoes from inventory.txt to shoes_list

    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
	menu = input('''
Select one of the following Options below:
	a -     Add shoe
	va -    View all shoes
	re -    Re-stock the lowest quantity shoe
	se -    Search all shoes
	val -   Print the total value for each shoe
	hi -	Highest quantity shoe to go on sale
	e -     Exit
: ''').lower()

	if (menu == 'a'): # Add shoe to shoe_list
		capture_shoes()

	elif (menu == 'va'): # View all shoes in shoe_list
		view_all()

	elif menu == 're': # Re-stock the lowest quantity shoe
		re_stock()

	elif menu == 'se': # Search all shoes
		search_code = input('Enter product code to search for: ') # The code to be searched for
		search_result = seach_shoe(search_code) # Test with code: SKU20394	
		if (search_result is not None):
			print(search_result)
		else:
			print('No results found.')
	
	elif menu == 'val': # Print the total value for each shoe
		print('----------Total value for each item----------')
		print('Product:		Total value')
		value_per_item()

	elif menu == 'hi': # Print highest quantity shoe to go on sale
		highest_qty()
	
	elif menu == 'e': # exit menu
		print('Goodbye!')
		exit()

	else: # if invalid input is entered
		print("You have not made a valid choice. Please try again")