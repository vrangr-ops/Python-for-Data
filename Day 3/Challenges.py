
def is_even(number):
    if number % 2 == 0: #modulus of 2-function tells you if the number can be divided by 2 fully with no remainder
        return "Even"
    else:
        return "Odd"
    

print(is_even(54))

def repeat_word(word,times):
    return word * times




def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

