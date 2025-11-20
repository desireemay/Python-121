#Shape Area
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
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

circle = Circle(5)
rect = Rectangle(4, 6)
print("Circle Area:", circle.area())
print("Rectangle Area:", rect.area())


#Employment Payment
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_pay(self):
        pass

class HourlyEmployee(Employee):
    def __init__(self, rate, hours):
        self.rate = rate
        self.hours = hours

    def calculate_pay(self):
        return self.rate * self.hours

class SalariedEmployee(Employee):
    def __init__(self, salary):
        self.salary = salary

    def calculate_pay(self):
        return self.salary

h_emp = HourlyEmployee(100, 8)
s_emp = SalariedEmployee(30000)

print("Hourly Employee Pay:", h_emp.calculate_pay())
print("Salaried Employee Pay:", s_emp.calculate_pay())
