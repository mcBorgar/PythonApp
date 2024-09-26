class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print ("opprettet")

    def greet(self):
        print (f"Jeg heter {self.name} og er {self.age}")

person = Person("Endre",31)
person.greet()