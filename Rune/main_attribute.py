import random
import json
class MainAttribute:
    def __init__(self, rune_slot:int, rune_degree=6):
        """
        slot: slot's number, 1-6
        degree: number of stars, 1-6
        """
        def get_main_attr_from_json(slot:int):
            """
            return example: "HP%"
            """
            with open('Rune\\main_attr.json', 'r', encoding='utf-8') as archive:
                slots = json.load(archive)
                slot_str = "slot"+str(slot)
                possibles_attr = slots[slot_str]
                name = random.choice( list( possibles_attr.keys() ) )
                #category: + or %
                category = random.choice( slots[slot_str][name] )
                return name + category

        def get_values_from_json(degree, name):
            with open('Rune\\main_attr_values.json', 'r', encoding='utf-8') as archive:
                degrees = json.load(archive)
                degree_str = "degree"+str(degree)
                attribute = degrees[degree_str][name]

                return attribute["init"], attribute['increase'], attribute['max']

        self.name = get_main_attr_from_json(rune_slot)
        self.value, self.increase_value_in, self.max_value = get_values_from_json(rune_degree, self.name)
        

    def power_up(self, rune_level:int):
        if rune_level < 15:
            self.value += self.increase_value_in
        else:
            self.value = self.max_value

    def print_(self):
        if "%" in self.name:
            name = self.name.split("%")[0]
            return f"{name} +{self.value}%"
        else:
            name = self.name.split("+")[0]
            return f"{name} +{self.value}"
