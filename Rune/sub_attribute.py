import random
import json
class SubAttribute:
    def __init__(self, slot:int, type_:str, sub_attribute=None, degree=6):
        """
        tipe_: "main", "sub" or "fix"
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

        def get_value_from_json(degree):
            #if type_ == "main" else sub_attribute
            return degree

        self.type_ = type_
        self.name = get_main_attr_from_json(slot) if type_ == "main" else sub_attribute
        self.value = get_value_from_json(degree)
