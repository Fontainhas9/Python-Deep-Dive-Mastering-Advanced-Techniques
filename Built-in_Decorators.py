class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        print("Setting value")
        self._temperature = value


class Sunrise:
    sunrise_hour = None

    def __init__(self, day="Sunday"):
        self.day = day

    @staticmethod
    def set_today(today):
        # self.day=today #This sends an error
        return today

    @classmethod
    def set_sunsire_class_method(cls, sunrise_hour):
        cls.sunrise_hour = sunrise_hour

    def set_sunrise(self, hour):
        self.sunrise_hour = hour


if __name__ == '__main__':
    # c = Celsius(25)
    # c.temperature = 30
    # print(c.temperature)

    s = Sunrise()
    print(Sunrise.sunrise_hour)
    Sunrise.set_sunsire_class_method(6)
    print(Sunrise.sunrise_hour)

    print("-" * 10)
    s.set_sunrise(7)
    print("Instance sunrise hour:", s.sunrise_hour)
    print("Class sunrise hour:", Sunrise.sunrise_hour)
