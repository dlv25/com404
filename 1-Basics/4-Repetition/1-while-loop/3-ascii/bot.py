#Asks for user input
print("How many bars should be charged?")
bars_to_charge = int(input())

#Sets variable
bars_charged = 0

#Display bars
print()

while (bars_charged < bars_to_charge):
    bars_charged = bars_charged + 1
    print("Charging:", "█" * bars_charged)
print()
print("The battery is fully charged")
