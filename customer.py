# Customer Loyalty Management System

# Database to store customer information and loyalty points
customer_database = {}

# Customer Loyalty Management System

# Database to store customer information and loyalty points
customer_database = {}

# Function to check if email already exists in the database
def email_exists(email):
    for customer_name, customer_info in customer_database.items():
        if customer_info['contact_details']['email'] == email:
            return True, customer_name, customer_info['loyalty_points']
    return False, None, None

# Function to add a new customer to the database
def add_customer(name, email):
    email_exists_flag, existing_customer_name, existing_loyalty_points = email_exists(email)

    if email_exists_flag:
        print(f"This email has already been used by the customer:")
        print(f"Name: {existing_customer_name}")
        print(f"Email: {email}")
        print(f"Total Loyalty Points: {existing_loyalty_points}")
    else:
        customer_database[name] = {'contact_details': {'email': email}, 'loyalty_points': 0}
        print(f"Customer '{name}' added successfully with email '{email}' and total loyalty points '0'.")
        
# Test the add_customer function
add_customer("cl", "123456@example.com")
add_customer("pecy", "pecy@example.com")
add_customer("aa", "12345678@example.com")
add_customer("cls", "123456@example.com") # shows the customer email already exits


# Function to record transaction and update loyalty points
def record_transaction(customer_name, transaction_amount):
    points_earned = transaction_amount * 100 #Ensure that points have no decimal points and that most purchases contain two decimals
    record_loyalty_points(customer_name, points_earned)
    

# Function to record loyalty points earned per transaction
def record_loyalty_points(customer_name, points_earned):
    if customer_name in customer_database:
        customer_database[customer_name]['loyalty_points'] += points_earned
        print(f"Loyalty points recorded: {points_earned} for {customer_name}")
        print(f"Total loyalty points for {customer_name}: {customer_database[customer_name]['loyalty_points']}")
    else:
        print(f"Customer '{customer_name}' not found in the database. Please add the customer first.")

# Function to display transaction history
def display_transaction_history(customer_name):
    if customer_name in customer_database:
        print(f"\nTransaction History for {customer_name}:")
        print(f"Total loyalty points for {customer_name}: {customer_database[customer_name]['loyalty_points']}")
        
        # Check if 'loyalty_level' key exists, if not, assume Basic level
        loyalty_level = customer_database[customer_name].get('loyalty_level', 'Basic')
        print(f"Loyalty Level for {customer_name}: {loyalty_level}")
    else:
        print(f"Customer '{customer_name}' not found in the database. Please add the customer first.")

    
# Function to check and reward loyalty levels
def check_and_reward_level(customer_name):
    loyalty_points = customer_database[customer_name]['loyalty_points']
    # Check for Silver level (3000 points)
    if loyalty_points >= 3000 and loyalty_points < 5000:
        customer_database[customer_name]['loyalty_level'] = 'Silver'
        print(f"Congratulations, {customer_name}! You have reached Silver level.")
        customer_database[customer_name]['loyalty_points'] += 50  # Reward additional 50 points

    # Check for Gold level (5000 points)
    elif loyalty_points >= 5000:
        customer_database[customer_name]['loyalty_level'] = 'Gold'
        print(f"Congratulations, {customer_name}! You have reached Gold level.")
        customer_database[customer_name]['loyalty_points'] += 100  # Reward additional 100 points

# Function to use loyalty points for purchase
def use_loyalty_points(customer_name, purchase_amount):
    if customer_name in customer_database:
        loyalty_points = customer_database[customer_name]['loyalty_points']

        # Check if accumulated loyalty points are enough for deduction
        if loyalty_points < purchase_amount * 100:
            print(f"Insufficient points. Cannot use points for this purchase.")
        else:
            deduction_points = purchase_amount * 100
            customer_database[customer_name]['loyalty_points'] -= deduction_points
            print(f"Loyalty points used for the purchase: {deduction_points}")
            print(f"Remaining total loyalty points for {customer_name}: {customer_database[customer_name]['loyalty_points']}")
    else:
        print(f"Customer '{customer_name}' not found in the database. Please add the customer first.")


# Test the functions
add_customer("cl", "1234567.com")
add_customer("pecy", "pecy.com")
add_customer("aa", "12345678@example.com")

# Simulate a transaction for everyone
record_transaction("cl", 5.99)
record_transaction("pecy", 32.99)
record_transaction("aa", 59.99)

# Simulate transactions for John Doe
record_loyalty_points("cl", 599)  # No level achieved
record_loyalty_points("pecy", 3299)  # Silver level achieved, rewarded 50 points
record_loyalty_points("aa", 5999)  # Gold level achieved, rewarded additional 100 points

# Display the current customer database
print("\nCurrent Customer Database:")
for customer_name, customer_info in customer_database.items():
    print(f"Name: {customer_name}, Email: {customer_info['contact_details']['email']}, Loyalty Points: {customer_info['loyalty_points']}, Loyalty Level: {customer_info.get('loyalty_level', 'Basic')}")
