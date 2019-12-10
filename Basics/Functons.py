#function
def print_lines():
    print("I am line1.")
    print("I am line2.")

# function call
print_lines()

def add_numbers(a, b):
    sum = a + b
    print(sum)

add_numbers(4, 5)

def add_numbers(a, b):
    sum = a + b
    return sum

result = add_numbers(4, 5)
print(result)

# Recursive function to find the factorial of a number
def calc_factorial(x):

    if x == 1:
        return 1
    else:
        return (x * calc_factorial(x-1))

num = 6
print("The factorial of", num, "is", calc_factorial(num)) 
# Output: The factorial of 6 is 720

#LAMDA
square = lambda x: x ** 2
print(square(5))
# Output: 25