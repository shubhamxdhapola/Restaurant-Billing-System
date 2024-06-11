# This dictionary stores menu items and their prices.
menu_and_price = {

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

# Print a welcome message and the menu.
print("\n----Welcome To Our Restaurant----\n")

print("----OUR MENU----\n")

# This loop iterates over the `menu_and_price` dictionary and prints each menu item and its price.
for item in menu_and_price: 
    print(f"- {item} : ₹{menu_and_price[item]}")

# Initialize variables to store the items and their quantities ordered by the customer, total bill, item number and attempts.
items_ordered_by_customer = {} 
total_bill=0 
item_no = 1 
attempts = 1 

try:

    # Define a function to take the customer's order.
    def taking_order():
    
        global item_no
        global total_bill
        global items_ordered_by_customer
        global attempts
    
        # Ask the customer how many items they want to order.
        totalNumberofItems = int(input("\n>> How many items would you like to order? : "))
   
        # Check if the customer wants to order more items than available in the menu.
        if totalNumberofItems > len(menu_and_price):
            pass

        i = 0
        while  totalNumberofItems > i:

            # Ask the customer to enter the item name and quantity.
            item_name = input(f"\n>> Enter item {item_no} : ")
            updated_item_name = item_name.title()
        
            # Check if the item is available in the menu.    
            if updated_item_name in menu_and_price:
                quantity = int(input(">> Enter quantity : "))
            
                # Update the quantity if the item is already ordered.
                if updated_item_name in items_ordered_by_customer:
                    items_ordered_by_customer[updated_item_name] += quantity

                else:
                    items_ordered_by_customer[updated_item_name] = quantity

                total_bill += menu_and_price[updated_item_name] * quantity
    
            else: 
                print(">> Item not available")
                totalNumberofItems+=1
                item_no-=1
                attempts+=1
    
            totalNumberofItems-=1
            item_no+=1
            
            # Check if the customer has exceeded the maximum attempts.
            if attempts > 6: 
                print("\n>> Maximum attempts reached")
                break

        # If the customer has exceeded the maximum attempts, return from the function
        if attempts > 6:
            return
            
        # Display the items ordered by the customer
        you_ordered = "You ordered"
        print("\n---------------------------")
        print(f">> {you_ordered.center(21)} <<")
        print("---------------------------")
    
        order_no=1
        for i in items_ordered_by_customer:
            print(f"{order_no}. {i} x {items_ordered_by_customer[i]}")
            order_no+=1
        
    # Call the 'taking_order' function.
    taking_order()
    
    # Check if the customer wants to order more items.
    if attempts < 6:    
       
       while True:
        
           order_more = input("\n>> Do you want to order more? (Yes/No) : ")
           updated_order_more = order_more.title()

           if updated_order_more == "Yes":
               attempts = 1
               taking_order()

           # Display the invoice and total bill when the customer finishes ordering
           elif updated_order_more == "No":
               print("\n>> You order has been successfully placed!!")
               
               invoice = "Invoice"
               print("\n-----------------------------------")
               print(f">>{invoice.center(30)}<<")  
               print("-----------------------------------")

               order_no = 1      
               for ordered_items in items_ordered_by_customer:
                   print(f"{order_no}. {ordered_items} x {items_ordered_by_customer[ordered_items]} : ",end="")
                   print(f"₹{items_ordered_by_customer[ordered_items] * menu_and_price[ordered_items]} (₹{menu_and_price[ordered_items]}/item)")
                   order_no +=1
                
               print("-----------------------------------")
               print(f">> Your total bill is : ₹{total_bill}")
               print("-----------------------------------")

               print("\n------Thanks for ordering!!------\n")
               break

           else:
           # Inform the user if the input is invalid
               print(">> Invalid input!")
               break
    
    else:
    # Inform the user if they have exceeded the maximum number of attempts
        print(">> Kindly re-run the program to order again!!")

except ValueError:
    # Handle the case when the user inputs a non-integer value
    print(">> Enter input in integer format")
    
