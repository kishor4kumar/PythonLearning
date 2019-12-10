#if-else
num = -1

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")
    
# Output: Negative number

#python uses indentation instead of {}
if False:
    print("I am inside the body of if.")
    print("I am also inside the body of if.")
print("I am outside the body of if")

#while loop
n = 100
# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter

print("The sum is", sum)

# Output: The sum is 5050

#for Loop
numbers = [6, 5, 3, 8, 4, 2]

sum = 0

# iterate over the list
for val in numbers:
    sum = sum+val

print("The sum is", sum) # Output: The sum is 28

#break statement
for val in "string":
    if val == "r":
        break
    print(val)

print("The end")

#continue statement
for val in "string":
    if val == "r":
        continue
    print(val)

print("The end")

#pass Statement - Suppose, you have a loop or a function that is 
#   not implemented yet, but want to implement it in the future. 
#   They cannot have an empty body. The interpreter would complain. 
#   So, you use the pass statement to construct a body that does nothing.

sequence = {'p', 'a', 's', 's'}
for val in sequence:
    pass