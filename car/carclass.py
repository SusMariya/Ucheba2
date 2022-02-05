class CarClass:
    def __init__(self, brand, model, year, probeg):
        self.brand = brand
        self.model = model
        self.year = year
        self.probeg = probeg

    def show_car(self):
        print(f'{self.brand}, {self.model}, {self.year} г, {self.probeg} км')

if __name__ == "__main__":
    e = CarClass("Tesla", 'T', 2020, 95000)
    e.show_car()
