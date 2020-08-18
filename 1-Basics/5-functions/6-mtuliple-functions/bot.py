def display_ladder(steps):
  for steps in range(steps):
    print("| |")
    print("***")
  
def create_ladder():
  print("Please enter the number of steps: ")
  steps = int(input())
  display_ladder(steps)
  
create_ladder()