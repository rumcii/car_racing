class Car:

    def __init__(self, car, model, max_speed):
        self.car = car
        self.model = model
        self.max_speed = max_speed

    def __str__(self):
        return "Car: {car} ## Model: {model} ## Max Speed: {max_speed}".format(
            model=self.model, car=self.car, max_speed=self.max_speed)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.car == other.car and self.model == other.model

    def __hash__(self):
        return hash(self.__str__())
