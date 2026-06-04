class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=SLOW, radius=5.0, color="blue", on=False):
        self.speed = speed
        self.radius = float(radius)
        self.color = str(color)
        self.on = bool(on)

    def speed(self):
        return self.__speed

    def speed(self, value):
        if value in [Fan.SLOW, Fan.MEDIUM, Fan.FAST]:
            self.__speed = value

    def radius(self, value):
        return self.__radius

    def radius(self, value):
        if value > 0:
            self.__radius = float(value)

    def color(self):
        return self.__color

    def color(self, value):

