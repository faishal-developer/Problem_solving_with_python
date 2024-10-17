# purpose: provides an interface for creating objects, but allows subclasses to alter the type of objects that will created.creating
# usecase: when you need to create objects dynamically without specifying the exact class


class Dog:
    def speak(self):
        return "woof"

class Cat:
    def speak(self):
        return "Meow"
    
class AnimalFactory:
    @staticmethod
    def get_animal(animal_type):
        if animal_type=="dog":
            return Dog()
        elif animal_type=="cat":
            return Cat()
        else:
            return None