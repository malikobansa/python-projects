#A Python Program to convert Temperature Faranheit of type integer 
#and convert it to degree Celsius

temp = input("Enter a temperature in Fahrenheit: ")

num = int(temp)

# Correct formula to convert Fahrenheit to Celsius
celsius = (num - 32) * 5/9

print(celsius)
