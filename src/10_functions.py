# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def evenOdd(i):
   return True if i % 2 == 0 else False
    

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
if evenOdd(num):
    print("Even!")
else:
    print("Odd")

