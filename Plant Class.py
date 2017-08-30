import Impact_Arrays as imp
import matplotlib.pyplot as plt
import numpy as np

class Plant():
    ''' A Plant Object returns a management practice inventory and impact assessment array.  This object can be
    the inventory and impact of a single plant (e.g. one tree), several of one type of plants (e.g. 5*Plant(one_tree)),
    several different plant species or several of the same species managed differently (e.g. Plant(1) + Plant(2)).
    This way, you can build up a full farm scenario as combinations of instantiations of different plants and their
    mgmt strategies'''

    def __init__(self):
        ''' Asks a lot of questions about management of this specific Plant Type to instantiate it as a variable.  This
            will entail a lot of weird logic flow structuring
                - Functional Unit (by area, by count)
                - Life Span : Based on Life Span, asks about mgmt practices from year to year (? maybe better to just
                        do freq/duration for every inventory item)
                - Inventory : see impact array file for inventory categories/build out this set of includable inventory
                        items, include freq/duration of activities where applicable
                        Inventory should request distribution desired (normal, triangular, yes/no,
                            custom (set of specified values), specified value (value*ones(trials), uniform) and request
                            further inputs based on distribution requested (norm - mean/sd, tri - min,prob,max, etc)
                - Yield Data (per FU)
                - Economic Data (this is an impact more than an inventory, cost of any given management practice,
                        as well as profit from yield per FU/per yield unit/per activity)
                - Impact Calc
                - Ultimately, I want to provide default options for different plant types - e.g. you intitiate a 'hay'
                    Plant() object, and are only presented with managment options relevant to hay, rather than like...
                    shaker machinery, etc.)
                '''

    def __add__(self, other):
        ''' combines multiple plant class objects (e.g. the total_plot_impact_calc() function in the
                impact calculator'''

    def __mul__(self, other):
        ''' calculates impact of several of the same plant class objects.  probably similar code to the __add__ fn
        just slightly tweaking it for mult rather than add
        also keeps track of how many of this instantiated object there are, to be read out later (instantiation defaults
        to one of a particular type, but can be edited either in __init__ or by ten_of_plant_one = 10 * Plant(1)'''

    def save(self):
        '''saves plant object to text or excel'''

    def tell(self):
        '''prints inventory array and impact array neatly and clearly - this might be broken into different functions,
        e.g. inventory(self) - prints management inputs inventory
        counts(self) - prints number of each type of plant included in the overall  plant object
            (e.g. counts(3*Plant(hay) + 5 * Plant(chestnut)) returns st like '3 ha of hay, 5 chestnut trees in object')
        impact_median(self)/impact_mean(self) - prints median/mean of impact array'''

    def edit(self):
        '''allows mgmt of inventory items in the object to be edited, recalculating the impact arrays'''

    def plot(self):
        '''generates plots of impact assessments. nicely labeled box plots and anything else that seems relevant'''

    def allocation(self):
        '''also one that probably will involve multiple different functions - allocate_mass(self), allocate_volume(self),
        allocate_cash(self), allocate_energy(self), etc.  I don't really know how this function will work yet. Will need
        to instantiate products and associated details somehow???'''

'''Eventually, code analysis functions of the instantiated scenario - what mgmt options can optimize different outputs of
your farm, whether by doing things differently to the crops given, or by planting different crops'''