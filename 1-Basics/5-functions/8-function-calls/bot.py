#Asks for user for input
print("Please enter a word")
word = input()

#Displays the user input in a box
def display_box():
    print("*" * (len(word) + 10))
    print("*", word, "*")
    print("*" * (len(word) + 10))

#Displays the user input in lower case
def display_lower():
    print("Your new word is: ", word.lower())

#Displays the user input in upper case
def display_upper():
    print("Your new word is: ", word.upper())

#Mirrors the user input
def display_mirror():
    for position in range(len(word) - 1, -1, -1):
        print(word[position], end="")

def repeat():
        print("How many times would you like to repeat your word?")
        times_repeat = int(input())
        print()

        for times_repeat in range (times_repeat):
            print(word.lower())
            print(word.upper())
        
        print()

def run():
    print("""
    Please select the option (number) you would like to run:
    1) Display in a Box – display the word in an ascii art box
    2) Display Lower-case – display the word in lower-case e.g. hello
    3) Display Upper-case – display the word in upper-case e.g. HELLO
    4) Display Mirrored – display the word with its mirrored word e.g. Hello | olleH
    5) Repeat – ask the user how many times to display the word and then display the word that many times alternating between upper-case and lower-case.
    """)
    select = int(input())

    if (select == 1):
        display_box()
    elif (select == 2):
        display_lower()
    elif (select == 3):
        display_upper()
    elif (select == 4):
        display_mirror()
    elif (select == 5):
        repeat()
    else:
        print("Please select a number between 1-5")

run()