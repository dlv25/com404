#Asks for user input
print("What level of brightness is required?")
brightness_level = int(input())

#Adjust brightness
print("\nAdjusting brightness...\n")

for brightness in range(2, brightness_level + 1, 2):
    print("Beep's brightness level", "*" * brightness)
    print("Bop's brightness level:", "*" * brightness)

print("Adjustments complete!")