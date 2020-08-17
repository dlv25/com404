#Read bot data
print("Please enter the number of lives")
lives = int(input())
print("Please enter the energy level")
energy = int(input())
print("please enter the shield level")
shield = int(input())

#Input complete message
print("Health has been set")

#Display bot data
print("Lives:", "♥" * lives)
print("Energy:", "♦" * energy)
print("Shield:", "♦" * shield)