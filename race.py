import json
import sys

from car import Car
from driver import Driver
from racing import Race
from championship import Championship


def main():
    print(sys.argv)
    if len(sys.argv) == 1:
        print("Hello PyRacer!")
        print("Please, call command with the proper argument:")
        print("\t$ python3 race.py start <name> <races_count> -> \
This will start a new championship with the given name,\
races count and drivers from cars.json")
        print("\t$ python3 race.py standings ->\
This will print the standings for each championship\
that has ever taken place.")
    elif sys.argv[1] == "start" or sys.argv[1] == "Start":
    # try:
        name = sys.argv[2]
        race_count = sys.argv[3]

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

        race = Race([ruci, tsekach, ciki, vesela, tsetsko], 0.1)

        championship = Championship(int(race_count), name, race)
        championship.start()

        # except:
        #     print("Wrong number of arguments!")


if __name__ == '__main__':
    main()
