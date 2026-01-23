

# Create the 5X table (1 to 10) using list multiplication
# We start with a list of 1-10 and multiply each element conceptually 
#  Define the initial table.
table = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
# 1. Print the full list
print("Full List:", table)
# 2. Remove one value from the list (e.g., removing 15)
table.remove(15)
print("After removing 15:", table)
# 3. Insert a number back in the correct place
# Index 2 is the 3rd position (where 15 was)
table.insert(2, 15)
print("After inserting 15 back:", table)
# 4. Remove the last value
table.pop()
print("After removing the last value:", table)
# 5. Print the 5th element
# Remember: Python starts counting at 0, so index 4 is the 5th element
print("The 5th element is:", table[4])
# 6. Find the position (index) of 40 in the list
position = table.index(40)
print("The position of 40 is index:", position)
# 7. Count how many times 5 appears in the list
count_five = table.count(5)
print("Number of times 5 appears:", count_five)

#sam solution
# Step 1: Start with an empty list
times_five = []

# Step 2: Use append to build the list step by step
times_five.append(5 * 0)
times_five.append(5 * 1)
times_five.append(5 * 2)
times_five.append(5 * 3)
times_five.append(5 * 4)
times_five.append(5 * 5)
times_five.append(5 * 6)
times_five.append(5 * 7)
times_five.append(5 * 8)
times_five.append(5 * 9)

# Step 3: Print the full list
print("5 times table:", times_five)

# Step 4: Remove one value (for example 35) using list method remove()
times_five.remove(35)
print("After removing 35:", times_five)

# Step 5: Insert a number back in the correct place
times_five.insert(7, 35)  # put 35 back at index 7
print("After inserting 35 back:", times_five)

# Step 6: Use pop() to remove the last value
last_value = times_five.pop()
print("After popping last value:", times_five)
print("The popped value was:", last_value)

# Step 7: Use indexing to print the 5th element in the list
print("The 5th element (index 4) is:", times_five[4])
# Step 8: Find the position (index) of a value in the list
index_of_25 = times_five.index(25)
print("The number 25 is at position:", index_of_25)

# Step 9: Count how many times a number appears in the list
count_5 = times_five.count(5)
print("The number 5 appears", count_5, "time(s) in the list.")

#dictionary

customers = [
{"first": "Charlie", "last": 'Bucket'},
{"first": 'Bobby',"last": "Smith"},
{"first": "Alice", "last": "Johnson"},
{"first": "Lisa",'last':'Simpson'},
{"first": "David", "last": "Tennant"}
]

def search_exact(customers, query):
    query = query.lower()
    return [
        c for c in customers
        if c.get("first", "").lower() == query or c.get("last", "").lower() == query
    ]

print(search_exact(customers, "alice"))

print(search_exact(customers, 'bobby'))


search_name = input("Search by first or last name: ").lower()

print("Search results:")
results = []

for customer in customers:
    if customer["first"].lower() == search_name or customer["last"].lower() == search_name:
        print(customer)
        results.append(customer)

if len(results) == 0:
    print("Customer not found.")

print("\nSearch results as a list:\n", results)


#Question 1
   #Ask the user for their exam score (0–100) and print:
    #A grade" for 90–100
    #B grade" for 80–89
   #"C grade" for 70–79
   #"Fail" for below 70

score = int(input('What was your exam score (0–100): '))


if 90 <= score <= 100:
    print("A grade")
elif 80 <= score <= 89:
    print("B grade")
elif 70 <= score <= 79:
    print("C grade")
elif 0 <= score < 70:
    print("Fail")
else:
    print("Invalid score")



#Question 2
   #Ask the user for a number and print:
#Between 10 and 20" if the number is in the range 10–20 inclusive.
   #"Outside range" otherwise.

num = int(input("Enter a number: "))

if 10 <= num <= 20:
    print("Between 10 and 20")
else:
    print("Outside range")


#Question 3
   #Print all even numbers from 2 to 20 using a for loop.
   #Use a while loop to count down from 10 to 1.

#Even numbers from 2 to 20 (for loop)

for num in range(2, 21, 2):
    print(num)

#Countdown from 10 to 1 (while loop)
count = 10

while count >= 1:
    print(count)
    count -= 1

#Question 4
for num in range(1, 11):
    if num % 3 == 0:
        continue   # skip multiples of 3
    
    if num == 8:
        break      # stops  the loop completely
    
    print(num)


#Mini Project: Number Guessing Game
   #Combine everything learned:
   #Create a random in between 1-10 (Dynamically not hardcoded!!)
   #Allow users to guess the number
   #Keep game going until they get it right
   #You can give clues if they get it wrong eg "too high" or "too low"

import random

# generate a random number between 1 and 10
secret_number = random.randint(1, 10)

while True:
    guess = int(input("Guess the number (1–10): "))

    if guess == secret_number:
        print("Correct! You guessed it!")
        break
    elif guess > secret_number:
        print("Too high, try again.")
    else:
        print("Too low, try again.")

