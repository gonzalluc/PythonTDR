class Dog():
    def __init__(self, my_name, my_gender, my_age): #Initialize atributes
        self.name = my_name
        self.gender = my_gender
        self.age = my_age

    def eat(self):
        if self.gender == "Male":
            print("Here" + self.name + "Good Boy!")
        else:
            print("Here" + self.name + "Good Girl!")
    def bark(self, is_loud):
        if is_loud:
            print("WOOF")
        else:
            print("woof...")
    def compute_age(self):
        dog_years = self.age*7
        print(self.name + "is" + str(dog_years))

Dog1 = Dog("Spot","Male",3)
Dog2 = Dog("Kady","Female",12)

print(Dog1.name)
print(Dog2.gender)

#Call methods
Dog1.eat()
Dog2.eat()
print()

Dog1.bark(True)
Dog2.bark(False)

Dog1.compute_age()
Dog2.compute_age()