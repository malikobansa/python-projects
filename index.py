#A Python Program that reads an integer 
#and determines and prints whether a number is odd or even

# Reading an integer from the user
num = int(input("Enter an integer: "))

# Determining whether the number is odd or even
if num % 2 == 0:
    print(f"The number {num} is even.")
else:
    print(f"The number {num} is odd.")


