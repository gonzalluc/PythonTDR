class Dog():
    def __init__(self, my_name, my_gender, my_age): #Initialize atributes
        self.name = my_name
        self.gender = my_gender
        self.age = my_age

    def eat(self):
        if self.gender == "Male":
            print("Here" + self.name + " Good Boy!")
        else:
            print("Here" + self.name + " Good Girl!")
    def bark(self, is_loud):
        if is_loud:
            print("WOOF")
        else:
            print("woof...")
    def compute_age(self):
        dog_years = self.age*7
        print(self.name + "is" + str(dog_years))

class Beagle(Dog):  
    #Specific type of dog
    def __init__(self, my_name, my_gender, my_age, is_gun_shy):
        #Call the initialitzation of of the super (parent) class
        super().__init__(my_name, my_gender, my_age)
        self.is_gun_shy = is_gun_shy
    
    def hunt(self):
        if  not self.is_gun_shy:
            self.bark(True)
            print(self.name + " just came back with a duck")
        else:
            print(self.name + " is not a good hunting dog")

    def bark(self, is_loud):
        if is_loud:
            print("HOWL")
        else:
            print("howl")
     

beagle = Beagle("kady", "female", 10, False)
beagle.eat()
beagle.bark(False)
beagle.compute_age()
beagle.hunt()

dog1 = Dog("spotty","male", 3)
#dog1.hunt()
dog1.bark(True)