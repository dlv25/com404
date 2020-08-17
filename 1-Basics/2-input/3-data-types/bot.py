#Read in user data
print("What is your name human?")
name = input()
print("How old are you (in years)?")
age = int(input())
print("How tall are you (in meters)?")
height = float(input())
print("How much do you weigh (in kilograms)?")
weight = float(input())

#Calculate BMI
bmi = weight / (height ** 2)

#display result
print(name, "you are", age, "years old. And your BMI is", bmi)