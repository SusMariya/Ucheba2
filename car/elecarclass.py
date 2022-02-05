from car import carclass

class ElectroCar(carclass.CarClass):
    def __init__(self,brand, model, year, probeg):
        super().__init__(brand, model, year, probeg)
        self.battary = 100

    def description_batarry(self):
        print(f"Этот автомобиль имеет можность {self.battary}%")
