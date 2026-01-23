#functions
#use def key word to define a function
#name of function comes after def
#parenthesis can hold arguments/parameters
#code block within every function starts with a (:) and is indented
"""
#syntax
def testfunction(arguments):
    #code block
    return #optional

print('Hello World')
#defining the function
def helloworld():
    print('Hello World')


helloworld() #calling the function

#function with arguments
#function is going to take 2 numbers and then print their sum

def twonumbers(num1,num2):
    return num1+num2

twonumbers(15,6)

result= twonumbers(15,6)
print(result)

#scope
#variables outside function
num3 =100   
num4 =200

def mutiplenumbers():
    num5=20 #locally scoped variables
            #can be used in the function only
    num6=50
    print(num3+num4+num5+num6)

mutiplenumbers()
print(num5)


#Challenges


MVP
Write a function called my_first_function.
Your function should take in a string as an argument.
It should print in the format: "I love {argument}!".

"""

def my_first_function():
    print('I Like cake')




"""
MVP
Write a function tripler().
It should take in a number and return the number × 3.
Print the results with three different arguments.

"""
def tripler(number):
    return number * 3

# Print results with three different arguments
print(tripler(2))
print(tripler(10))
print(tripler(-4))


"""

MVP
Write a function greet() that takes a name as a parameter.
It should return "Hello, {name}!".

"""
def greet(name):
    return f"Hello, {name}!"




"""

MVP
Write a function is_even() that takes a number as input.
Return "Even" if the number is even, "Odd" if it’s odd.
"""

def is_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


"""
MVP
Write a function repeat_word(word, times)
It should return the word repeated times number of times.
"""

def repeat_word(word, times):
    return word * times


""""

MVP
Write a function factorial(n) that calculates the factorial of n.
Example: factorial(5) → 5 * 4 * 3 * 2 * 1 = 120.
"""
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result



""""

MVP
Write a function power(base, exponent=2)
By default, it should square the base.
If an exponent is provided, use it instead.

"""
def power(base, exponent=2):
    return base ** exponent



