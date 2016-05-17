import json
import random

from car import Car
from driver import Driver


class Race:

    def __init__(self, drivers, crash_chance, race_name="random race"):
        self.drivers = drivers
        self.crash_chance = crash_chance
        self.result = self.open_file()
        self.crash_list = []
        self.race_name = race_name

    # save result to json file
    def save_file(self):
        with open("result.json", "w") as f:
            json.dump(self.result, f, indent=4)

    # load json file
    def open_file(self):
        try:
            with open("result.json", "r") as f:
                file = json.load(f)
        except:
            file = {}
        return file

    # retur nlist with crash candidates
    def _random_choice(self):
        crash_chance = int(self.crash_chance * 10)

        return random.sample(list(range(0, len(self.drivers))), crash_chance)

    # return ramdom selected driver from random choice
    def _driver_crash_status(self, driver_crash_list):
        return random.choice(driver_crash_list)

    # return list with some number of driver index and -1 to 10th index if any
    def _populate_driver_crash_list(self, driver_to_crash):
        result = []

        for i in range(0, 10):
            if i <= self.crash_chance * 10:
                result.append(driver_to_crash)
            result.append(-1)
        return result

    # startrace, populate crash list and write to json file
    def start_race(self):
        for driver_index in self._random_choice():
            driver_status = self._driver_crash_status(
                self._populate_driver_crash_list(driver_index))
            if driver_status > -1:
                self.crash_list.append(self.drivers.pop(driver_index))

        self._write_to_file()

    # write result to json file
    def _write_to_file(self):
        race_result = {}
        ranking = [8, 6, 4]

        for rang in ranking:
            driver = random.choice(self.drivers)
            self.drivers.remove(driver)

            if self.race_name not in self.result:
                self.result[self.race_name] = {}

            if driver.nickname in self.result[self.race_name] and\
               self.race_name != "random race":
                self.result[self.race_name][driver.nickname] += rang
            else:
                self.result[self.race_name][driver.nickname] = rang
        for driver in self.drivers:
            if driver not in self.result[self.race_name]:
                self.result[self.race_name][driver.nickname] = 0

        self.save_file()

    def add_driver(self):
        car_brand = input("Enter car brand: ")
        car_model = input("Enter car model: ")
        car_max_speed = input("ente car max speed: ")

        car = Car(car_brand, car_model, car_max_speed)

        driver_name = input("enter driver name: ")
        driver_nickname = input("enter driver nickname: ")

        driver = Driver(driver_name, driver_nickname, car)

        print("New driver was created.")

        add_to_drivers = input("Do you want to add a driver to the race? ")

        if add_to_drivers == "yes":
            self.drivers.append(driver)
            print("New driver was added to the race.")
        else:
            print("OK")

    def clear_results(self):
        is_clear_result = input("Do you want to clear all results? ")

        if is_clear_result == "yes":
            self.result = {}
            print("Ok, it's clear.")
