import json
import random


class Race:

    def __init__(self, drivers, crash_chance, race_name="random race"):
        self.drivers = drivers
        self.crash_chance = crash_chance
        self.result = self.open_file()
        self.crash_list = []
        self.race_name = race_name

    def save_file(self):
        with open("result.json", "w") as f:
            json.dump(self.result, f, indent=4)

    def open_file(self):
        try:
            with open("result.json", "r") as f:
                file = json.load(f)
        except:
            file = {}
        return file

    def _random_choice(self):
        crash_chance = int(self.crash_chance * 10)

        return random.sample(list(range(0, len(self.drivers))), crash_chance)

    def _driver_crash_status(self, driver_crash_list):
        return random.choice(driver_crash_list)

    def _populate_driver_crash_list(self, driver_to_crash):
        result = []

        for i in range(0, 10):
            if i <= self.crash_chance * 10:
                result.append(driver_to_crash)
            result.append(-1)
        return result

    def start_race(self):
        for driver_index in self._random_choice():
            driver_status = self._driver_crash_status(
                self._populate_driver_crash_list(driver_index))
            if driver_status > -1:
                self.crash_list.append(self.drivers.pop(driver_index))

    def _write_to_file(self, first_place, second_place, third_place):
        race_result = {}
        ranking = [8, 6, 4]

        for rang in ranking:
            driver = random.choice(drivers)
            self.drivers.remove(driver)
            if driver in self.result[self.race_name] and\
               self.race_name != "random race":
                self.result[self.race_name][driver.nickname] += rang
            else:
                self.result[self.race_name][driver.nickname] = rang

        for driver in self.drivers:
            if driver not in self.result[self.race_name]:
                self.result[self.race_name][driver.nickname] = 0

        self.save_file()
