class Car:
    def __init__(self,Model,Brand):
        self.model = Model
        self.brand = Brand

    def display(self):
        print(f"{self.model} {self.brand} is starting")