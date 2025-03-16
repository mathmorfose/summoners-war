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

        #self.name:str = self.create_name()
        self.degree:int = get_degree()
        self.slot:int = get_slot()
        self.category:str = get_category()
        #self.category:str = "magic"
        self.set:str = get_set()
        self.level = 0
        self.main_attr = MainAttribute(self.slot)
        self.possible_sub_attr = get_possible_sub_attributes(self.slot)
        print(self.possible_sub_attr)
        self.fix_attr = None
        self.sub_attr_1 = None
        self.sub_attr_2 = None
        self.sub_attr_3 = None
        self.sub_attr_4 = None
        self.define_attributes()


    def define_attributes(self):
        def will_be_there_fix_attr():
            return random.choice([True, True])
        
        if self.category == "legend":
            if will_be_there_fix_attr():
                self.fix_attr = SubAttribute(self.get_sub_attribute(self.possible_sub_attr, self.main_attr.name))
                self.sub_attr_1 = SubAttribute(self.get_sub_attribute(self.possible_sub_attr, self.fix_attr.name))
            else:
                self.sub_attr_1 = SubAttribute(self.get_sub_attribute(self.possible_sub_attr, self.main_attr.name))

            self.sub_attr_2 = SubAttribute(self.get_sub_attribute(self.possible_sub_attr, self.sub_attr_1.name))
            self.sub_attr_3 = SubAttribute(self.get_sub_attribute(self.possible_sub_attr, self.sub_attr_2.name))
            self.sub_attr_4 = SubAttribute(self.get_sub_attribute(self.possible_sub_attr, self.sub_attr_3.name))
        elif self.category == "hero":
            if will_be_there_fix_attr():
                self.fix_attr = SubAttribute(self.get_sub_attribute(self.possible_sub_attr, self.main_attr.name))
                self.sub_attr_1 = SubAttribute(self.get_sub_attribute(self.possible_sub_attr, self.fix_attr.name))
            else:
                self.sub_attr_1 = SubAttribute(self.get_sub_attribute(self.possible_sub_attr, self.main_attr.name))

            self.sub_attr_2 = SubAttribute(self.get_sub_attribute(self.possible_sub_attr, self.sub_attr_1.name))
            self.sub_attr_3 = SubAttribute(self.get_sub_attribute(self.possible_sub_attr, self.sub_attr_2.name))
        elif self.category == "rare":
            if will_be_there_fix_attr():
                self.fix_attr = SubAttribute(self.get_sub_attribute(self.possible_sub_attr, self.main_attr.name))
                self.sub_attr_1 = SubAttribute(self.get_sub_attribute(self.possible_sub_attr, self.fix_attr.name))
            else:
                self.sub_attr_1 = SubAttribute(self.get_sub_attribute(self.possible_sub_attr, self.main_attr.name))

            self.sub_attr_2 = SubAttribute(self.get_sub_attribute(self.possible_sub_attr, self.sub_attr_1.name))
        elif self.category == "magic":
            if will_be_there_fix_attr():
                self.fix_attr = SubAttribute(self.get_sub_attribute(self.possible_sub_attr, self.main_attr.name))
                self.sub_attr_1 = SubAttribute(self.get_sub_attribute(self.possible_sub_attr, self.fix_attr.name))
            else:
                self.sub_attr_1 = SubAttribute(self.get_sub_attribute(self.possible_sub_attr, self.main_attr.name))
        else: #normal
            if will_be_there_fix_attr():
                self.fix_attr = SubAttribute(self.get_sub_attribute(self.possible_sub_attr, self.main_attr.name))

    def get_sub_attribute(self, possible_sub_attributes:list, sub_to_remove):
        if sub_to_remove in possible_sub_attributes:
            possible_sub_attributes.remove(sub_to_remove)

        sub_attribute = random.choice(possible_sub_attributes)
        return sub_attribute

    def power_up_one_level(self):
        self.level += 1
        self.main_attr.power_up(self.level)
        if self.category == "legend":
            if self.level in [3, 6, 9, 12]:
                chosen_sub = random.choice( [self.sub_attr_1, self.sub_attr_2,
                                            self.sub_attr_3, self.sub_attr_4] )
                chosen_sub.power_up()
        
        elif self.category == "hero":
            if self.level in [3, 6, 9]:
                chosen_sub = random.choice( [self.sub_attr_1, self.sub_attr_2,
                                            self.sub_attr_3] )
                chosen_sub.power_up()
            elif self.level == 12:
                self.sub_attr_4 = SubAttribute(self.get_sub_attribute(self.possible_sub_attr, self.sub_attr_3.name))
        elif self.category == "rare":
            if self.level in [3, 6]:
                chosen_sub = random.choice( [self.sub_attr_1, self.sub_attr_2] )
                chosen_sub.power_up()
            elif self.level == 9:
                self.sub_attr_3 = SubAttribute(self.get_sub_attribute(self.possible_sub_attr, self.sub_attr_2.name))
            elif self.level == 12:
                self.sub_attr_4 = SubAttribute(self.get_sub_attribute(self.possible_sub_attr, self.sub_attr_3.name))
        elif self.category == "magic":
            if self.level == 3:
                self.sub_attr_1.power_up()
            elif self.level == 6:
                self.sub_attr_2 = SubAttribute(self.get_sub_attribute(self.possible_sub_attr, self.sub_attr_1.name))
            elif self.level == 9:
                self.sub_attr_3 = SubAttribute(self.get_sub_attribute(self.possible_sub_attr, self.sub_attr_2.name))
            elif self.level == 12:
                self.sub_attr_4 = SubAttribute(self.get_sub_attribute(self.possible_sub_attr, self.sub_attr_3.name))
        elif self.category == "normal":
            
            if self.level == 3:
                if self.fix_attr:
                    self.sub_attr_1 = SubAttribute(self.get_sub_attribute(self.possible_sub_attr, self.fix_attr.name))
                else:
                    self.sub_attr_1 = SubAttribute(self.get_sub_attribute(self.possible_sub_attr, self.main_attr.name))
            elif self.level == 6:
                self.sub_attr_2 = SubAttribute(self.get_sub_attribute(self.possible_sub_attr, self.sub_attr_1.name))
            elif self.level == 9:
                self.sub_attr_3 = SubAttribute(self.get_sub_attribute(self.possible_sub_attr, self.sub_attr_2.name))
            elif self.level == 12:
                self.sub_attr_4 = SubAttribute(self.get_sub_attribute(self.possible_sub_attr, self.sub_attr_3.name))



                if self.fix_attr:
                    self.sub_attr_1 = SubAttribute(self.get_sub_attribute(self.possible_sub_attr, self.fix_attr.name))
                else:
                    self.sub_attr_1 = SubAttribute(self.get_sub_attribute(self.possible_sub_attr, self.main_attr.name))
                self.sub_attr_2 = SubAttribute(self.get_sub_attribute(self.possible_sub_attr, self.sub_attr_1.name))
                self.sub_attr_3 = SubAttribute(self.get_sub_attribute(self.possible_sub_attr, self.sub_attr_2.name))
                self.sub_attr_4 = SubAttribute(self.get_sub_attribute(self.possible_sub_attr, self.sub_attr_3.name))
        

    def power_up(self, new_level):
        upgrades = new_level - self.level
        for _ in range(upgrades):
            self.power_up_one_level()

    def show(self):
        print(
            f"Name: +{self.level} Rune {self.set} ({self.slot})\n",
            f"Category: {self.category}\n",
            f"Main Attr: {self.main_attr.print_()}\n",
            f"Fix: {self.fix_attr.print_()}\n" if self.fix_attr else "",
            f"Sub 1: {self.sub_attr_1.print_()}\n" if self.sub_attr_1 else "",
            f"Sub 2: {self.sub_attr_2.print_()}\n" if self.sub_attr_2 else "",
            f"Sub 3: {self.sub_attr_3.print_()}\n" if self.sub_attr_3 else "",
            f"Sub 4: {self.sub_attr_4.print_()}"if self.sub_attr_4 else "",
        )

rune = Rune()
rune.power_up(15)
rune.show()
