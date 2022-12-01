class Car:
    def __init__(self, name, color):
        self.car_name = name
        self.car_color = color
    
    def displayCarDetails(self):
        print("Car name is ",self.car_name," and Car color is ",self.car_color)

    @staticmethod        # static method don't have self pointer and don't need object to call, it is called using class name
    def initialMessage():
        print("Nice Car !!!!!")

Car.initialMessage()     # called using class name
car1 = Car('XUV 700', 'Red')
car1.displayCarDetails()



class Calculation:
    @staticmethod
    def addTwoNums( num1, num2 ):
        print("Sum of two numbers = ", num1 + num2)
    
Calculation.addTwoNums(10,5)
