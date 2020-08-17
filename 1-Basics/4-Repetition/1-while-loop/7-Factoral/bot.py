#Asks for user input
print("Please enter a number:")
num = int(input())

#calculate the factoral
count = 0 
total = 1

while (count < num):
    count = count + 1
    total = total * count

print("The factoral is", total)