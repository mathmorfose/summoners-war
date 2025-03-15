import random
import json

from main_attribute import MainAttribute
from sub_attribute import SubAttribute

class Rune:
    def __init__(self):
        def get_degree():
            #return random.randint(1, 6)
            return 6

        def get_slot():
            return random.randint(1, 6)

        def get_category():
            return random.choice( ['normal', 'magic', 'rare', 'hero', 'legend'] )

        def get_set():
            return random.choice(
                [
                    "Violent",
                    "Despair",
                    "Swift",
                    "Fatal",
                    "Rage",
                    "Vampire",
                    "Will",
                    "Blade",
                    "Revenge",
                    "Shield",
                    "Energy",
                    "Guard",
                    "Endure",
                    "Focus",
                    "Seal",
                    "Destroy",
                    "Fight",
                    "Intangible",
                    "Accuracy",
                    "Determination",
                    "Enhance"
                ]
            )

        def get_possible_sub_attributes(slot:int):
            with open('Rune\\sub_attr.json', 'r', encoding='utf-8') as archive:
                slot_types = json.load(archive)
                if slot % 2 == 0:
                    slot_number_type = "even_slot"
                    possible_attributes = slot_types[slot_number_type]
                else:
                    slot_number_type = "odd_slot"
                    slot_str = "slot"+str(slot)
                    possible_attributes = slot_types[slot_number_type][slot_str]

                possible_attributes = [f"{key}{value}" for key, values in possible_attributes.items() for value in values]
                
                return possible_attributes
            
            return ["HP+", "HP%","DEF+", "DEF%","ATK+", "ATK%",
                    "RES%", "ACC%", "Crit Rate%", "Crit Damage%", "SPD+"]

        def get_sub_attribute(possible_sub_attributes:list, sub_to_remove):
            if sub_to_remove in possible_sub_attributes:
                possible_sub_attributes.remove(sub_to_remove)

            sub_attribute = random.choice(possible_sub_attributes)
            return sub_attribute

        def get_fix_attr():
            # vai ter atributo fixo? se sim .. se não...
            return ""

        #self.name:str = self.create_name()
        self.degree:int = get_degree()
        self.slot:int = get_slot()
        self.category:str = get_category()
        self.set:str = get_set()
        self.level = 0
        self.main_attr = MainAttribute(self.slot)
        possible_sub_attributes = get_possible_sub_attributes(self.slot)
        self.sub_attr_1 = SubAttribute(self.slot, "sub", get_sub_attribute(possible_sub_attributes, self.main_attr.name))
        self.sub_attr_2 = SubAttribute(self.slot, "sub", get_sub_attribute(possible_sub_attributes, self.sub_attr_1.name))
        self.sub_attr_3 = SubAttribute(self.slot, "sub", get_sub_attribute(possible_sub_attributes, self.sub_attr_2.name))
        self.sub_attr_4 = SubAttribute(self.slot, "sub", get_sub_attribute(possible_sub_attributes, self.sub_attr_3.name))

    def printar(self):
        print(
            f"Name: +{self.level} Rune {self.set} ({self.slot})\n",
            f"Main Attr: {self.main_attr.print_()}\n",
            f"Sub 1: {self.sub_attr_1.name}\n",
            f"Sub 2: {self.sub_attr_2.name}\n",
            f"Sub 3: {self.sub_attr_3.name}\n",
            f"Sub 4: {self.sub_attr_4.name}",
        )

runa = Rune()

runa.printar()