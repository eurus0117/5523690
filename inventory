inventory = {}

# Function to add an item to the inventory
	def add_item(item, quantity: int):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
print(f"{item}: {quantity}")

# Function to view all items in the inventory
def view_inventory():
    # Implementation Instructions:
    # 1. Loop through the inventory dictionary.
    # 2. Print each item's name and its quantity.
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

        # Function to update the quantity of an existing item in the inventory
def update_item(item, quantity):
    if item in inventory:
        inventory[item] = quantity
    else:
        print(f"{item} not found in inventory.")

        # Main function to manage the inventory

def manage_inventory():
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Update Item Quantity")
        print("4. Exit")
        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            add_item(item, quantity)
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            item = input("Enter item name: ")
            quantity = int(input("Enter new quantity: "))
            update_item(item, quantity)
        elif choice == '4':
            print("Exiting Inventory Management System.")
            break
        else:
            print("Invalid choice. Please choose again.")

# Entry point of the program
if __name__ == "__main__":
    manage_inventory()
