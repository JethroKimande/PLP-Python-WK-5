# Assignment 1: Superhero Class with Inheritance
import os
os.environ["PYTHONIOENCODING"] = "utf-8"
class Hero:
    def __init__(self, name, strength):
        self._name = name  # Encapsulation
        self.strength = strength
    
    def fight(self):
        print(f"{self._name} fights with strength {self.strength}!")

class Superhero(Hero):  # Inheritance
    def __init__(self, name, strength, power):
        super().__init__(name, strength)
        self.power = power
    
    def use_power(self):  # Polymorphism potential
        print(f"{self._name} uses {self.power}!")

# Example
hero = Hero("Warrior", 80)
superhero = Superhero("Superman", 100, "flight")
hero.fight()
superhero.use_power()
superhero.fight()

# Activity 2: Polymorphism Challenge

class Vehicle:
    def move(self):
        pass  # Base method

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Example
car = Car()
plane = Plane()
car.move()
plane.move()