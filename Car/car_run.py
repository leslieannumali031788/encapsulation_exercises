class Car:
    def __init__(self, year_model, make):
        self.year_model = year_model
        self.make = make
        self.__current_speed = 0

    def accelerate(self):
       self.__current_speed += 5

    def brake(self):
        if self.__current_speed >=5:
            self.__current_speed -= 5
        else:
            self.__current_speed =0

    def get_speed(self):
        return self.__current_speed

    def get_model_info(self):
