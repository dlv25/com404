#Asks for user input
print("What is the weight of Beep?")
beep_weight = int(input())
    
print("What is the weight of Bop?")
bop_weight = int(input())

#function to work out the average of the user input
def calc_avg_weight():
    average = (beep_weight + bop_weight) / 2
    print(average)

#function to work out the sum of the user input
def sum_weights():
    sum = (beep_weight + bop_weight)
    print()
    print(sum)

#Defines the "run" function
def run():
    #Asks the user which optioon they would like to choose (sum or average)
    print("What would you like to calcluate (sum or average)?")
    choice = input()
    #runs a function based on the option the user has chosen
    if (choice == "sum"):
        sum_weights()
    elif (choice == "average"):
        calc_avg_weight()
    else:
        print()
        print("Please choose either sum or average")

#runs program
run()