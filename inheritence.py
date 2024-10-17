class Animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        return "generic sound"


class Dog():
    def __init__(self,bread):
        self.bread=bread

    # method overriding
    def speak(self):
        return "gew gew"
    
class GermanShepard(Animal,Dog):
    def __init__(self, name,bread,age):
        # multiple inheritence
        Animal.__init__(self,name)
        Dog.__init__(self,bread)
        # access modifiers:private
        self.__age=age
    

dog=GermanShepard("poppy","german shepard",3)
print(dog.__age)