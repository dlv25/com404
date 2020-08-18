#creates a class under 'person'
class person:
    def __init__(self, name, age, weight):
        #Defines a default value (0) to 'name', 'age' and 'weight'
        self.name = name
        self.age = age
        self.weight = weight
        

    #defines a method to display the information   
    def display(self):
        print("{} is {} years old and weighs {}kg".format(self.name, self.age, self.weight))
    
    
daniel.display()
  