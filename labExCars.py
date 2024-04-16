class Cars:
    def __init__(self, name, speed, mileage):
        self.name = name
        self.speed = speed
        self.mileage = mileage

    def get_name(self):
        return self.name

    def get_mileage_multiplied_by_10(self):
        return self.mileage * 10


# Example usage:
car1 = Cars("Toyota", 120, 25)
print("Car Name:", car1.get_name())
print("Mileage multiplied by 10:", car1.get_mileage_multiplied_by_10())
