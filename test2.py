import numpy as np
import pylab


# np.matmul(inputs2,char2)
# np.linalg.matrix_power(char2,2)

import matplotlib.pyplot as plt
# np.random.triangular(min,mode,max,number)
# np.random.normal(mean, sd, number)
# np.random.uniform(min, max, number)
# np.random.randint(0,2,number)
trials = 20
orchard_life_years = np.random.triangular(45,50,55,trials)
pasture_life_years = np.random.triangular(15,20,25,trials)
print((orchard_life_years - 20))
