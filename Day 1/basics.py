print("burhan")

print("1. My favorite food is ramen")
print("2. I live in birmingham ")
print("3. I was born in bangladesh")

# variables
#must start with letter or underscore
#can contain letters,numbers or underscore(my_var1)
#cannot contain special characters ($,£)
#name should be descriptive of its value (x->user_name,y->age)
#python is case sensitive

name = input("What is your name?")
print(f"Good Morning {name}!")

#integer=whole number
x=25


#string=a word
name ="burhan"

#boolean=true/false
is_sunny=False

# using variables
print(x)
print( name, "is it sunny?", is_sunny)



favourite_food = "ramen" 

birth_year = "1995"

print ("I was born in birth_year and my favourite food is favourite_food")


import sys
#allows us to check memory size

#primitive types
#int->whole numbers
num_1=1
print(num_1)
print(type(num_1))
print(sys.getsizeof(num_1))


#float -> decimials
pi= float(3.14)
print(pi)
print(sys.getsizeof(pi))
#str-> text
city = "Birmingham"
print(city)
print(sys.getsizeof(city))
#bool->logical values(T,F)

is_raining= True
print("is it raining?",is_raining)
print(sys.getsizeof(is_raining))


print ("------------------------------------------------")

# casting (type conversion)

my_num=5
my_float=(my_num)

print(my_float)

my_str = "123"
my_int = int(my_str)

print(my_int)

#boolean as numbers

print(int(False))
print(int(True))

print ("------------------------------------------------")

# user input

age_1 = int(input("Enter your age:"))
print ("You are", age_1, "years old")

decimal = float (input ("enter a decimal:"))
print ("you typed", decimal)

print ("------------------------------------------------")

