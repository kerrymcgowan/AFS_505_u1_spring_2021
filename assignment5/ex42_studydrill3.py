## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animial
class Dog(Animal):

    def __init__(self, name):
        ## From self, get the name attribute, and set it to name
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## From self, get the name attribute, and set it to name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## From self, get the name attribute, and set it to name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## Class Employee that takes a self parameter has-a __init__ that takes a name parameter
        super(Employee, self).__init__(name)
        ## From self, get the salary attribute, and set it to salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


# rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## From mary, get the pet attribute, and set it to satan
mary.pet = satan

## frank is-a Employee that takes Frank and 120000 parameters
frank = Employee("Frank", 120000)

## From frank, get the pet attribute, and set it to rover
frank.pet = rover

## flipper is a Fish
flipper = Fish("Flipper")

## crouse is a Salmon
crouse = Salmon("crouse")

## harry is a Halibut
harry = Halibut("harry")
