import random
import json
class SubAttribute:
    def __init__(self, name, degree=6):
        """
        slot: slot's number, 1-6
        degree: number of stars, 1-6
        """
        def get_values_from_json(degree, name):
            """
            return example: "HP%"
            """
            with open('Rune\\sub_values.json', 'r', encoding='utf-8') as archive:
                degrees = json.load(archive)
                degree_str = "degree"+str(degree)
                attribute = degrees[degree_str][name]

                return attribute["min"], attribute["max"]

        self.name = name
        self.min, self.max = get_values_from_json(degree, name)
        self.base_value = random.randint(self.min, self.max)
        self.value = self.base_value
        self.power_ups = []


    def power_up(self):
        value = random.randint(self.min, self.max)
        self.value += value
        self.power_ups.append(value)

    def print_(self):
        if "%" in self.name:
            name = self.name.split("%")[0]
            return f"{name} +{self.value}% -- {self.base_value}-{self.power_ups}"
        else:
            name = self.name.split("+")[0]
            return f"{name} +{self.value} -- {self.base_value}-{self.power_ups}"
