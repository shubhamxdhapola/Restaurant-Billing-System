This Python script simulates a restaurant ordering system, allowing customers to place their orders interactively. It showcases a menu, takes customer orders,
handles quantity updates, and generates an invoice. Here’s a detailed breakdown of the project:

### Key Features:

1. *Menu Display*:
   - The script starts by printing a welcome message and displaying the restaurant menu with items and their prices stored in a dictionary.

2. *Taking Orders*:
   - The taking_order function prompts the customer to specify the number of items they wish to order.
   - For each item, the customer inputs the item name and quantity. The script checks if the item is available on the menu.
   - If an item is ordered multiple times, the quantities are aggregated.
   - The total bill is updated based on the item prices and quantities ordered.

3. *Order Validation*:
   - The script ensures that the customer does not exceed the number of items available on the menu.
   - It allows a maximum of six invalid attempts to input an item not on the menu. Exceeding this limit terminates the ordering process.

4. *Ordering More Items*:
   - After the initial order, the customer is asked if they want to order more items.
   - If the customer chooses to order more, the taking_order function is called again.
   - If the customer finishes ordering, an invoice is generated and displayed, showing the items ordered, quantities, individual item costs, and the total bill.

5. *Error Handling*:
   - The script includes error handling to manage non-integer inputs gracefully, ensuring the program does not crash due to invalid data entry.

### Workflow:

1. *Menu and Price Dictionary*:
   - A dictionary (menu_and_price) stores the menu items and their respective prices.

2. *User Interaction*:
   - The script interacts with the user through the console, asking for the number of items, item names, and quantities.

3. *Order Processing*:
   - Orders are processed, validated, and stored in a dictionary (items_ordered_by_customer) that tracks the items and quantities ordered.

4. *Billing*:
   - The total bill is calculated in real-time as items are added.
   - An invoice is generated at the end of the order, summarizing the entire order and total cost.

5. *User Feedback*:
   - The script provides feedback on invalid inputs and informs the customer when the order is successfully placed.

### Summary:

This project provides a straightforward, interactive experience for users to place orders at a virtual restaurant, handling multiple scenarios
such as ordering additional items and managing invalid inputs. It effectively demonstrates basic concepts of Python programming including dictionaries,
loops, conditionals, functions, and exception handling.
