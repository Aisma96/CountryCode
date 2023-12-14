class Country:
    def __init__(self, population, area, country_name, is_big = True):
        self.population = population
        self.area = area
        self.country_name = country_name
        self.is_big = is_big

    def pop_grater(self):
        if self.population > 20000000 or self.area > 3000000:
            print(True)
        else:
            print(False)

    def compare_pop(self):
        austr = australia.population / australia.area
        andor = andorra.population / andorra.area
        if andor > austr:
            print(f'{self.country_name} has a larger population density than Australia')
        else:
            print(f'{andorra} has a smaller population density than {australia}')


australia = Country(23545500, 7692024, "Australia")
andorra = Country(76098, 468, "Andorra")
