class Country:
    def __init__(self, population, area, country_name):
        self.population = population
        self.area = area
        self.country_name = country_name
        self.is_big = self.check_is_big()
        self.population_density = self.population / self.area

    def check_is_big(self):
        return self.population > 20000000 or self.area > 3000000

    def compare_pop(self, other_country):
        if self.population_density > other_country.population_density:
            return f'{self.country_name} has bigger density than {other_country.country_name}'
        elif self.population_density < other_country.population_density:
            return f'{self.country_name} has less density tahn {other_country.country_name}'
        else:
            return f'{self.country_name} has same density as {other_country.country_name}'


australia = Country(23545500, 7692024, "Australia")
andorra = Country(76098, 468, "Andorra")
print(australia.is_big)
print(andorra.is_big)
print(australia.population_density)
print(andorra.population_density)
print(andorra.compare_pop(australia))
print(australia.compare_pop(andorra))
