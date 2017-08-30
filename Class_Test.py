import Impact_Dictionaries as dict





class Chestnut:
    # initializes Chestnut Object - asking for relevant inputs (replace input statements with for loops for monte carlo)
    def __init__(self, name):
        self.name = name
        self.number = input('number of ' + self.name + ' plants on plot?')
        self.harvesting = input('number of kg diesel used in harvesting each plant')

    # calculates Chestnut impact from inputs
    def impact(self):
        diesel_harvesting_impact = {}
        for key in dict.diesel_impact_dict: # See "test.py" for a potentially easieer way to write this - list comprehension rather than a loop
            diesel_harvesting_impact[key] = float(self.harvesting) * int(self.number) * dict.diesel_impact_dict[key]

        print('The total impact from ' + self.name + " plants on the farm is:")
        print(diesel_harvesting_impact)

class Hay:
    #initializes Hay object - asking for relevant inputs
    def __init__(self, name):
        self.name = name
        self.hectares = input('number of hectares of ' + self.name + ' on plot?')

    #calculates Hay impact from inputs
    def impact(self):
        hay_mowing_impact = {}
        for key in dict.mowing_impact_dict: #use a list comprehension rather than a loop!
            hay_mowing_impact[key] = float(self.hectares) * dict.mowing_impact_dict[key]

        print('The total impact from ' + self.name + " plants on the farm is:")
        print(hay_mowing_impact)





