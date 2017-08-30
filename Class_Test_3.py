import Impact_Dictionaries as d
import numpy as np

class Plant:
    def __init__(self,name):
        self.name = name.upper()
        if self.name == "CHESTNUT":
            Plant.chestnut(self)
        elif self.name == "HAY":
            Plant.hay(self)

    def chestnut(self):
        number = input('number of ' + self.name + ' plants on plot?')
        harvesting = input('number of kg diesel used in harvesting each plant')
        diesel_harvesting_impact = {}
        for key in d.diesel_impact_dict:  # See "test.py" for a potentially easieer way to write this - list comprehension rather than a loop
            diesel_harvesting_impact[key] = float(harvesting) * int(number) * d.diesel_impact_dict[key]

        print('The total impact from ' + self.name + " plants on the farm is:")
        return diesel_harvesting_impact

    def hay(self):
        hectares = input('number of hectares of ' + self.name + ' on plot?')
        hay_mowing_impact = {}
        for key in d.mowing_impact_dict:  # use a list comprehension rather than a loop!
            hay_mowing_impact[key] = float(hectares) * d.mowing_impact_dict[key]

        print('The total impact from ' + self.name + " plants on the farm is:")
        return hay_mowing_impact




