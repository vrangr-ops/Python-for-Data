# Initialise an empty list to store customer dictionaries
customers = []

print("Enter customer details. Type 'exit' as first name to quit.")

while True:
    first_name = input("Enter first name: ")
    if first_name.lower() == "exit":
        break
    last_name = input("Enter last name: ")

    # Create a dictionary for the current customer
    customer = {
        "first_name": first_name,
        "last_name": last_name
    }

    # Add the dictionary to the list
    customers.append(customer)

# Print the final list of customer dictionaries
print("\nCustomer list:")
for customer in customers:
    print(customer)

    