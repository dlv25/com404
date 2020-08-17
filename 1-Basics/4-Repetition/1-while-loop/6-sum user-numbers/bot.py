#Asks for user input
print("How many numbers should I sum up?")
num_sums = int(input())

#Sets variable
summed = 0

#Display blank line
print()

#Sum numbers
total = 1

while (summed < num_sums):
    print("Please enter number", summed, "of", num_sums, ":")
    number = int(input())
    total = total + number
    summed = summed + 1

#Displays result
print("The answer is: ", total)