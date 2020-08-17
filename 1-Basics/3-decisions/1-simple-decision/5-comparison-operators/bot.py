#Prompt for user input
print("Please enter the first number")
num1 = int(input())
print("Please enter the second number")
num2 = int(input())

#Determine which message to display
if (num1 < num2) :
    print("\nThe first number is the smallest.")
elif (num1 > num2) :
    print("\nThe second number is the smallest.")
else:
    print("\nThe two numbers equal.")