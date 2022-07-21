"""
1. Single inheritance
2. Multiple inheritance
3. Multilevel inheritance
4. Hierarchical inheritance
5. Hybrid inheritance

Single inheritance
When a child class inherits from only one parent class, it is called single inheritance

Multiple inheritance
When a child class inherits from multiple parent classes, it is called multiple inheritance
"""

#Single inheritance
# class Car:
#       def __init__(self, car_brand):
#             self.brand = car_brand

# class Jaguar(Car):
#       def __init__(self, car_model):
#             super().__init__("Jaguar")
#             self.model = car_model
 

# Multiple Inheritance
class Car:
    def __init__(self, car_brand="Jaguar"):
        self.brand = car_brand
        print("Car is invoked")
        super().__init__()
    
    def message(self):
        print("Hello from Car")
    
    def hola(self):
        print("Hola from Car")

class Tata:
    def __init__(self):
        self.company = "Tata & Son Group"
        print("Tata is invoked")
        super().__init__()
    def hola(self):
        print("Hola from Tata")

class Jaguar(Car, Tata):
    def __init__(self, car_model):
        super().__init__()
        self.model = car_model
        
    def hola(self):
        print("Hola from Jaguar")
        super().hola()

if __name__ == "__main__":
    # sapna_car = Jaguar("XUC14", "Land Rover")
    # # print(sapna_car.brand, sapna_car.model)
    # print(sapna_car.model, sapna_car.company)
    # sapna_car.message()
    # sapna_car.hola()

    sapna_car = Jaguar("XUC14")
    print(sapna_car.brand, sapna_car.model, sapna_car.company)
    sapna_car.hola()
