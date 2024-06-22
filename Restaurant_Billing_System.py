# This dictionary stores menu items and their prices.
menu = {
    
	"Pasta" : 69,
    "Pizza" : 79,
    "Burger" : 69,
    "Noodles" : 59,
    "Coffee" : 59,
    "Tea" : 19,
    "Cold Drink" : 49,
    "Ice Cream" : 49,
    "Fries" : 29,
    "Sandwich" : 49,
    "Salad" : 49,
    "Soup" : 49,
    "Dessert" : 49, 
    "Fried Rice" : 79
}

# Global variables
current_item_number = 1
total_bill = 0
customer_order = {}
attempts = 1
line = '='

# Display the restaurant menu
def display_menu():
	
  print(f"\n{line * 4} Welcome To Our Restaurant {line * 4}")
  print(f"\n{line * 7} OUR MENU {line * 7}\n")

  # This loop iterates over the `menu` dictionary and prints each menu item and its price.
  for item, price in menu.items(): 
    print(f"- {item.ljust(15)} : ₹{price}")

	
# Function to take customer's order
def take_order():

	global current_item_number, total_bill, customer_order, attempts
	
	try:
		# Ask how many items the customer wants to order
		total_items_to_order = int(input("\n>> How many items would you like to order? : "))

		# Check if the customer wants to order more items than available in the menu. 
		if total_items_to_order > len(menu):
			print(">> You are trying to order more items than available in the menu please order considering menu.")
			increment_attempts()
			return
		
		# Process each item in the order
		while  total_items_to_order > 0:
      
			# Ask the customer to enter the item name and quantity
			item_name = input(f"\n>> Enter item {current_item_number} : ").title().strip()

			# Check if the item is available in the menu
			if item_name in menu:
				quantity = int(input(">> Enter quantity : "))

				# Update the quantity if the item is already ordered
				if item_name in customer_order:
					customer_order[item_name] += quantity

				else:
					customer_order[item_name] = quantity

				# Update the total bill
				total_bill += menu[item_name] * quantity

				total_items_to_order -= 1
				current_item_number += 1  

			else: 
				print(">> This item is not available in our menu please order considering menu")
				attempts += 1

			# Check if the customer has exceeded the maximum attempts.
			if attempts > 6: 
				print("\n>> You are out of attempts because of multiple invalid inputs")
				return False

		return True
						
	except ValueError: 
		print(">> Invalid Input! Please enter a numeric value")
		increment_attempts()
		
# Function to handle attempts count
def increment_attempts():
	
	global attempts
	attempts += 1
	if attempts <= 6:
		take_order()
	else:
		print("\n>> You are out of attempts because of multiple invalid inputs")
	
# Display items ordered by the customer            
def display_ordered_items():
	
	items_ordered = "Items Ordered"
	print(f"\n{line*30}")
	print(f'>> {items_ordered.center(23)} <<')
	print(f"{line*30}")

	for orderNo, (item_name, quantity) in enumerate (customer_order.items(), 1):
		print(f"{orderNo}. {item_name} x {quantity}")


# Ask if customer wants to order more items or finalize the order        
def order_more_items():
	
	global attempts
	
	while True:
		
		order_more = input("\n>> Do you want to order more? (Yes/No) : ").title().strip()

		if  order_more == "Yes":
			take_order()
			display_ordered_items()
		
		elif order_more == "No":
			print(">> Your order has been successfully placed!")
			print_invoice()
			break
		
		else:
			print(">> Invalid input! Please enter 'Yes' or 'No'. ")
			
			attempts += 1
			if attempts > 6:
				print("\n>> You are out of attempts because of multiple invalid inputs")
				break
			
			
# Print the invoice with the total bill and details of items ordered
def print_invoice():

	invoice = "Invoice"
	print(f"\n{line*35}")
	print(f">>{invoice.center(30)}<<")  
	print(f"{line*35}")

	for order_no, (item_name, quantity) in enumerate (customer_order.items(), 1):
		
		item_total = quantity * menu[item_name]
		print(f"{order_no}. {item_name} x {quantity} : ₹{item_total} (₹{menu[item_name]}/item) ")
		
	print(f"{line*35}")
	print(f">> Your total bill is : ₹{total_bill}")
	print(f"{line*35}")

	print(f"\n{line * 5} Thanks for ordering {line * 5} \n")


def main():
	
	display_menu()
	isTrue = take_order()
	if isTrue == True:
		display_ordered_items()
		order_more_items()
	
if __name__ == "__main__":
	main()
