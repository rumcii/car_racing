class Championship:
    def __init__(self, laps, name, race):
        self.laps = laps
        self.name = name
        self.race = race
        self.race.race_name = name

    def start(self):
        race_count = 1

        while race_count <= self.laps:
            self.race.start_race()
            print("Race #{}".format(race_count))
            print("###### START ######")

            for racer in self.race.result[self.name]:
                print("{}: {}".format(racer,
                                      self.race.result[self.name][racer]))
            print("\n")

            for driver in self.race.crash_list:
                print("Unfortunately {} has crashed.".format(driver))

            race_count += 1
