import Impact_Arrays as imp
import matplotlib.pyplot as plt
import numpy as np
from Conversions_Library import *


'''------------------------------MONTE CARLO INPUTS--------------------------------------------'''
trials = 10000


'''-------------------------------INVENTORY INPUTS-----------------------------------------'''


'''SITE VARIABLES'''
trees_per_acre = np.random.triangular(36,49,70,trials)
acres_per_trt = 1.32
trees_per_trt = acres_per_trt * trees_per_acre
orchard_life_years = np.random.triangular(45,50,55,trials)
orchard_years_to_production = np.random.triangular(9,10,12,trials)
orchard_years_for_establishment = 3
pasture_life_years = np.random.triangular(15,20,25,trials)
dry_hay_tons_per_trt = 9.2
kg_per_hay_bale = 700
cutting_pasture_times_per_year = np.random.triangular(3,3.5,4,trials)
is_resown = np.random.randint(0,2,trials)
is_tilled = np.random.randint(0,2,trials)

surflan_yr1_kgai_acre = np.random.triangular(0,2.31,3.5,trials)
surflan_yr2_3_kgai_acre = np.random.triangular(0, 4.6, 7, trials)
poast_yr1_kgai_acre = np.random.triangular(0, .51, 1, trials)

fertilizer_DAP_kg_tree = np.random.triangular(0,1.4,2.8,trials)
fertilizer_DAP_fraction_N = .18
fertilizer_DAP_fraction_P2O5 = .46
fertilizer_potash_kg_tree = np.random.triangular(0,.69,1.4,trials)
fertilizer_potash_fraction_K2O = .6

pesticide_wand_0_or_broadcaster_1 = np.random.randint(0,2,trials)
pesticide_applications_count = np.random.triangular(25,50,100,trials)
pesticide_kgai_per_acre_per_application = np.random.triangular(0,1.4,3,trials)
pesticide_ft2_rows_per_acre_yr1 = 2922 # Depends on number of trees planted, equations are in EInputs o42 to o48
pesticide_ft2_rows_per_acre_yr2on = 3652 # I don't understand this metric. equations are in Einputs o42 to o 48

pesticide_applications_count_establishment = np.random.triangular(2,4,6,trials)

urea_year2_kgN_tree = np.random.triangular(0, .23, .3, trials)
urea_year3_kgN_tree = np.random.triangular(0, .37, .4, trials)
urea_year4_kgN_tree = np.random.triangular(0, .51, .6, trials)
urea_year5_kgN_tree = np.random.triangular(0, .74, .8, trials)
urea_fraction_N = .46

harvester_used = np.random.randint(0, 2, trials)
harvester_mass_kg = 5760
harvester_lifespan_hr = 9000
harvester_fuel_use_gal_hr = np.random.triangular(3, 3.3, 4, trials)
harvester_speed_acres_hr = np.random.triangular(1, 1.2, 1.5, trials)

shaker_used = np.random.randint(0,2,trials)
shaker_mass_kg = 5443
shaker_lifespan_hr = 9000
shaker_fuel_use_gal_hr = np.random.triangular(3,3.5,4,trials)
shaker_speed_trees_hr = np.random.triangular(50,60,70,trials)

sweeper_used = np.random.randint(0,2,trials)
sweeper_mass_kg = 4853
sweeper_lifespan_hr = 9000
sweeper_fuel_use_gal_hr = np.random.triangular(1.5,2,2.5,trials)
sweeper_speed_acres_hr = np.random.triangular(1,1.2,1.5,trials)

seed_delivery_miles_roundtrip = np.random.triangular(40,100,400,trials)
seed_delivery_mpg = np.random.triangular(5,20,40,trials)

grass_seeding_rate_lb_acre = np.random.triangular(0,15,40,trials)

#Chestnut Destruction Phase
tree_harvesting_rate_min_tree = np.random.triangular(1,2,3,trials)