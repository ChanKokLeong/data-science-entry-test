Task 1
# Define a class named Car with attributes: make, model, year
# Initialize these attributes in the __init__ method
# Add a method named describe_car() that prints information about the car as "Year Make Model"

class Car:
  def __init__(self, make, model, year):
    self.make = make     # initialize 'make' attribute
    self.model = model   # initialize 'model' attribute
    self.year = year     # initialize 'year' attribute

  def describe_car(self): 
    print(f'Car is: {self.make}, Model: {self.model}, Year: {self.year}')
    


Task 2
# Create an instance of the Car class with the following attributes and call describe_car method:
# - Make: Toyota, Model: Corolla, Year: 2020

my_car = Car('Toyota', 'Corolla', 2020)

my_car.describe_car()
