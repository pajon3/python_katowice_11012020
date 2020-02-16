class ElectricCar:
    def __init__(self, max_range):
        self.max_range = max_range
        self.traveled= 0

    def drive(self, kilometers):

        to_travel =min(self.traveled+kilometers,self.max_range-self.traveled)
        self.traveled += to_travel
        return to_travel

    def charge(self):
        self.traveled = 0


class TestElectricCar:
    def test_initializatiom(self):
        car = ElectricCar(100)
        assert car

    def test_drive(self):
        car = ElectricCar(100)
        assert car.drive(70) == 70
        assert car.drive(70) == 30
        car.charge()
        assert car.drive(110) == 100
