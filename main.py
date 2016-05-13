from car import Car
from driver import Driver
from racing import Race
from championship import Championship


def main():
    opel = Car("Opel", "Astra", 160)
    alfa = Car("Alfa Romeo", "GT", 240)
    ford = Car("Ford", "Fiesta", 160)
    vectra = Car("Opel", "Vectra", 180)
    galaxy = Car("Ford", "Galaxy", 160)

    ruci = Driver("Rumen", "ruci", opel)
    tsekach = Driver("Tsvetan", "tsekach", alfa)
    ciki = Driver("Ciklama", "ciki", ford)
    vesela = Driver("Vesela", "vesela", vectra)
    tsetsko = Driver("Tsvetan", "tsetsko", galaxy)

    race = Race([ruci, tsekach, ciki, vesela, tsetsko], 0.1, "hohoho")

    championship = Championship(3, "test", race)
    championship.start()


if __name__ == '__main__':
    main()
