class Vehicle:
    def __init__(self, clean, number, wheels):
        self.__speed = 0
        self.clean = clean
        self.number = number
        self.wheels = wheels

    def print_speedometer(self):
        print(f"{self.__speed}km/h")

    def accelerate_up(self, value):
        if value > 30:
            print("Cannot accelerate more than 30")
        elif value < 0:
            pass
        else:
            self.__speed += value
            if self.__speed > 250:
                self.__speed = 250

    def slow_down(self, value):
        if value < 0:
            pass
        else:
            self.__speed -= value
            if self.__speed < 0:
                self.__speed = 0


class PW(Vehicle):
    def __init__(self, clean, number, wheels, countdoors, type):
        super().__init__(clean, number, wheels)
        self.countdoors = countdoors
        self.type = type


class LKW(Vehicle):
    def __init__(self, clean, number, wheels, payload):
        super().__init__(clean, number, wheels)
        self.payload = payload


