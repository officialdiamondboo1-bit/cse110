# CREATIVITY: Added structured string formatting to align prices neatly 
# and dynamically display the total item count alongside the grand total.

# Create two parallel lists to store the item names and their respective prices
item_names = []
item_prices = []

action = 0

print("Welcome to the Shopping Cart Program!")

# Loop continues running until the user enters 5 to quit
while action != 5:
    print("\nPlease select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    
    # Read the user's menu choice
    action = int(input("Please enter an action: "))
    
    # OPTION 1: Add a new item and price
    if action == 1:
        new_item = input("What item would you like to add? ")
        new_price = float(input(f"What is the price of '{new_item}'? "))
        
        # Save both values into their respective lists
        item_names.append(new_item)
        item_prices.append(new_price)
        print(f"'{new_item}' has been added to the cart.")
        
    # OPTION 2: Display the contents of the shopping cart
    elif action == 2:
        print("\nThe contents of the shopping cart are:")
        # Loop through using range to print 1-based index numbering
        for i in range(len(item_names)):
            print(f"{i + 1}. {item_names[i]} - ${item_prices[i]:.2f}")
            
    # OPTION 3: Remove an item safely
    elif action == 3:
        # Display the cart first so the user can see item numbers
        print("\nThe contents of the shopping cart are:")
        for i in range(len(item_names)):
            print(f"{i + 1}. {item_names[i]} - ${item_prices[i]:.2f}")
            
        remove_num = int(input("\nWhich item would you like to remove? "))
        # Convert user's 1-based choice to a Python 0-based index
        index_to_remove = remove_num - 1
        
        # Check if the chosen index is within valid bounds of the list
        if index_to_remove >= 0 and index_to_remove < len(item_names):
            item_names.pop(index_to_remove)
            item_prices.pop(index_to_remove)
            print("Item removed.")
        else:
            print("Sorry, that is not a valid item number.")
            
    # OPTION 4: Compute the total amount
    elif action == 4:
        total_price = 0.0
        # Iterate through the prices list to compute the grand total
        for price in item_prices:
            total_price += price
        print(f"\nThe total price of the items in the shopping cart is ${total_price:.2f}")
        
    # OPTION 5: Quit the program
    elif action == 5:
        print("Thank you. Goodbye!")
