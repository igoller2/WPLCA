import Impact_Arrays as dict
import numpy as np

class test():
    def __init__(self, name, number=1, **inputs):
        self.name = name
        self.number = number
        self.plantcounts = {self.name : self.number}
        self.inputs = {}
#        self.impacts = []
        for i in inputs:
            if i.upper() == 'BALING':
                self.inputs['Baling'] = inputs[i]
                self.impacts = inputs[i] * dict.baling_impact_dict * self.number
            else :
                print('Impact dictionary not found for ' + i)



    def __add__(self,other):
        var = {}
        for key in self.plantcounts.keys():
            if key in other.plantcounts.keys():
                var[key] = self.plantcounts[key] + other.plantcounts[key]
            else:
                var[key] = self.plantcounts[key]

#       var = {**self.plantcounts, **other.plantcounts}
        return var

    def __mul__(self, other):
        var = {k : other * self.plantcounts[k] for k in self.plantcounts}
        return var





#for i in range(10):
#    var = test('chestnut', 1, baling = 8.5 * 2 * np.random.rand())
#    print(var.impacts)



#for k in var:
#    var[k] = 2*var[k]


