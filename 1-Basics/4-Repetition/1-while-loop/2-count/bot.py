#Asks for user input
print("How many lives cables should I avoid?")
cables_to_avoid = int(input())

#Sets variable
cables_avoided = 0

#Avoid cables
print()

while (cables_avoided < cables_to_avoid):
    print("Avoiding...", end="")
    cables_avoided = cables_avoided + 1
    print("Done!", cables_avoided, "cables avoided")