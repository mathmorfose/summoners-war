import random
import json
class SubAttribute:
    def __init__(self, slot:int, name, degree=6):
        """
        slot: slot's number, 1-6
        degree: number of stars, 1-6
        """
        def get_value_from_json(degree, name):
            """
            return example: "HP%"
            """
            with open('Rune\\sub_values.json', 'r', encoding='utf-8') as archive:
                degrees = json.load(archive)
                degree_str = "degree"+str(degree)
                attribute = degrees[degree_str][name]

                return random.randint(attribute["min"], attribute["max"])

        self.name = name
        self.value = get_value_from_json(degree, name)

    def print_(self):
        if "%" in self.name:
            name = self.name.split("%")[0]
            return f"{name} +{self.value}%"
        else:
            name = self.name.split("+")[0]
            return f"{name} +{self.value}"
