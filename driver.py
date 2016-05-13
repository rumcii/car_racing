from exceptions import NameAlreadyExsistsError


class Driver:

    nickname_list = []

    def __init__(self, name, nickname, car):
        self.name = name
        self.car = car
        self.nickname = nickname
        self._add_to_nickname_list(nickname)

    def __str__(self):
        return "Name: {name} ## car: {car}".format(
            name=self.name, car=self.car)

    def __eq__(self, other):
        return self.name == other.name and self.car == other.car

    def __hash__(self):
        return hash(self.__str__())

    def _add_to_nickname_list(self, nickname):
        if nickname in self.nickname_list:
            raise NameAlreadyExsistsError(
                "The nickname is already used! Choose another one."
            )
        self.nickname_list.append(nickname)
