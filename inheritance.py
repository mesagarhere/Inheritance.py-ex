#Create a Motorcycle class that inherits from Vehicle and adds a has_sidecar attribute.

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

class Motorcycle(Vehicle):
    def __init__(self, make, model, has_sidecar):
        super().__init__(make, model)
        self.has_sidecar = has_sidecar
        # Example usage
motorcycle = Motorcycle("Harley-Davidson", "Street 750", False)
print(motorcycle.make)        # Output: Harley-Davidson

#Create a Developer class that inherits from both Person and Employee and adds a programming_language attribute.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Employee:
    def __init__(self, employee_id, position):
        self.employee_id = employee_id
        self.position = position

class Developer(Person, Employee):
    def __init__(self, name, age, employee_id, position, programming_language):
        Person.__init__(self, name, age)
        Employee.__init__(self, employee_id, position)
        self.programming_language = programming_language
        print(f"Congratulations! You guessed the number {actual_number} in {attempts} attempts.")
        print(f"Congratulations! You guessed the number {actual_number} in {attempts} attempts.")
        break
        print(f"Congratulations! You guessed the number {actual_number} in {attempts} attempts.")
        print("Congratulations! You guessed the number", actual_number, "in", attempts, "attempts."):
        self.programming_language = programming_language
# Example usage
developer = Developer("Alice", 30, "E123", "Software Engineer", "Python")
print(developer.name)              # Output: Alice
print(developer.age)               # Output: 30
print(developer.employee_id)      # Output: E123
print(developer.position)         # Output: Software Engineer
print(developer.programming_language)  # Output: Python

#Create a Bird class inheriting from Animal and override eat(). Add a fly() method.
class Animal:
    def eat(self):
        print("This animal eats food.")

class Bird(Animal):
    def eat(self):
        print("This bird eats seeds.")

    def fly(self):
        print("This bird can fly.")
# Example usage
bird = Bird()
bird.eat()  # Output: This bird eats seeds.
bird.fly()  # Output: This bird can fly.

#Implement multiple inheritance: Create Amphibian inheriting from Swimmer and Walker (define Walker with a walk() method).
class Swimmer:
    def swim(self):
        print("This animal can swim.")
class Walker:
    def walk(self):
        print("This animal can walk.")

class Amphibian(Swimmer, Walker):
    def hop(self):
        print("This amphibian can hop.")
# Example usage
amphibian = Amphibian()
amphibian.swim()  # Output: This animal can swim.
amphibian.walk()  # Output: This animal can walk.  # Output: This amphibian can hop.
amphibian.hop()  # Output: This amphibian can hop.

#subclass Use super() in a class to extend a method.
class Amphibian(Swimmer, Walker):
    def hop(self):
        print("This amphibian can hop.")

    def swim(self):
        super().swim()
        print("This amphibian can also swim.")
# Example usage
amphibian = Amphibian()
amphibian.swim()  # Output: This animal can swim.
                  #         This amphibian can also swim.
amphibian.walk()  # Output: This animal can walk.
amphibian.hop()  # Output: This amphibian can hop.

#Write a polymorphic function that takes a list of shapes (e.g., Circle, Rectangle inheriting from Shape) and calls area() on each
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

def print_areas(shapes):
    for shape in shapes:
        print(shape.area())

# Example usage
shapes = [Circle(5), Rectangle(4, 6)]
print_areas(shapes)
# Output: 78.5
#         24
        print(developer.programming_language)  # Output: Python
