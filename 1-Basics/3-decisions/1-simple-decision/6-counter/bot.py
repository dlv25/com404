print("Please enter the first whole number.")
num1 = int(input())
print("Please enter the second whole number.")
num2 = int(input())
print("Please enter the third whole number")
num3 = int(input())

even_numbers = 0
odd_numbers = 0 

# Determine which numbers are even and which are odd
if (num1 % 2 == 0):
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1

if (num2 % 2 == 0):
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1

if (num3 % 2 == 0):
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1

# Display result
print("There were", even_numbers, "even and", odd_numbers, "odd numbers.")