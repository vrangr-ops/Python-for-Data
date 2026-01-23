# Control Flow
# is how a program decides what to do next, in Python this includes
    # conditional statements
    # comparison operators
    # logical operators
    # loops
    # control statements



# conditional statements

age = 20
if age >= 18:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
else:
    print("You are a child")

age = 24
if age >=24:
    print('You can drink in the USA')
elif age >= 18:
    print("You are an adult")
else:
    print("You are a child")


print('----------------------------------------')

# comparison and logical operators

# AND
age = 25
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")

age = 16
has_drivingid =True
if age >= 18 and has_drivingid:
    print('Can drive car')
else:
     print('Have a walk')

# OR
day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
else:
    print("It's a weekday!")


print('----------------------------------------')

# loops
# use these to iterate over a sequence (list, string, range etc)

# loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("I like", fruit)

# loop in range
for i in range(5):
    print(i)

# while loops
num = 1
while num <= 8:
    print(num)
    num += 1




# control statements in loops
    # break - exit loop immediately
    # continue - skip current iteration and continue with the next
    # pass - does nothing (placeholder for code)

# break example
for i in range(1, 10):
    if i == 7:
        break
    print(i)

# continue example
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# pass example
for i in range(3):
    pass # placeholder



print("--------------------------------------------------------")


# DICTIONARIES
# organise data based on key-value pairs
# syntax is key:value
# they are mutable and dynamic

Student ={'name':'bob','age':'45','course':['Chemistry','Physics']}
print(Student['course'])
print(Student.get('phone'))

print(len(Student))

print(Student.items)

# declare a dictionary
my_dictionary = {
    "first_name": "Barack",
    "last_name": "Obama",
}

print(my_dictionary)

# get a value with the key
print("My name is", my_dictionary["first_name"])

# add a new key value
my_dictionary["job"] = "President"
print(my_dictionary)

# check if a key exists
print("Do they have a job?", "job" in my_dictionary)


# get list of
# keys
print(my_dictionary.keys())
# values
print(my_dictionary.values())
# both
for keys, values in my_dictionary.items():
    print(keys, values)


# delete a key
del my_dictionary["job"]
print(my_dictionary)

# loop through keys
for key in my_dictionary:
    print("Key", key)

# delete all entries
my_dictionary.clear()
print(my_dictionary)



# Built in Dictionary methods

d = {'a': 10, 'b': 20, 'c': 30}

# returns the value for a key if it exists in the dict
print(d.get('a'))
print(d.get('z'))

# returns a list of key-value pairs in the dict
print(d.items())
print(list(d.items())[0][1])

# returns a list of keys
print(d.keys())

# returns a list of values
print(d.values())


# merging a dict with another

d2 = {'b': 200, 'd': 400}

d.update(d2)
print(d)




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

#Extension
#Search or Filter Customers by First or Last Name.


