import Impact_Arrays as imp
import matplotlib.pyplot as plt
import numpy as np
from Conversions_Library import *


'''------------------------------MONTE CARLO INPUTS--------------------------------------------'''
trials = 10000

'''-------------------------------INVENTORY INPUTS-----------------------------------------'''

'''Pasture Parameters'''
dry_hay_tons_per_trt = 9.2
kg_per_hay_bale = 700
baling_silage_correction_factor = .23 #I don't know what this is or where it came from but Diana was using it???

'''Orchard Parameters'''
trees_per_acre = np.random.triangular(36,49,70,trials)
acres_per_trt = 1.32
ha_per_trt = acres_per_trt * ha_per_acre
trees_per_trt = acres_per_trt * trees_per_acre
orchard_life_years = np.random.triangular(45,50,55,trials)
pasture_life_years = np.random.triangular(15,20,25,trials)
orchard_years_to_production = np.random.triangular(9,10,12,trials)
orchard_years_for_establishment = 3

'''Wood Parameters'''
timber_density_lbs_ft3 = np.random.triangular(28,29,30,trials)
timber_length_lumber_ft = np.random.triangular(7,10,13,trials)
tree_diameter_breast_height_in = np.random.triangular(4,6,10)
timber_selling_price_usd_board_ft = np.random.triangular(3,5.5,8,trials)

'''Chestnut Parameters'''
chestnut_yield_lbs_acre = np.random.triangular(1000,2500,3500,trials)
chestnut_selling_price_usd_lb = np.random.triangular(2.45,3.1,3.5,trials)
chestnut_weight_nuts_lb = np.random.triangular(34,36,38,trials)
chestnut_diameter_in = np.random.triangular(1,1.12,1.25,trials)

'''Pasture Activities'''
is_tilled = np.random.randint(0,2,trials)
is_resown = np.random.randint(0,2,trials)
grass_seeding_rate_lb_acre = np.random.triangular(0,15,40,trials)

cutting_pasture_times_per_year = np.random.triangular(3,3.5,4,trials)

seed_delivery_miles_roundtrip = np.random.triangular(40,100,400,trials)
seed_delivery_mpg = np.random.triangular(5,20,40,trials)

pesticide_applications_btwn_rows_yr_2_3_count = np.random.triangular(2,4,6,trials)

'''Orchard Activities'''
#Orchard Pesticides
surflan_yr1_kgai_acre = np.random.triangular(0,2.31,3.5,trials)
surflan_yr2_3_kgai_acre = np.random.triangular(0, 4.6, 7, trials)
poast_yr1_kgai_acre = np.random.triangular(0, .51, 1, trials)
pesticide_wand_0_or_broadcaster_1 = np.random.randint(0,2,trials)
pesticide_applications_count = np.random.triangular(25,50,100,trials)
pesticide_kgai_per_acre_per_application = np.random.triangular(0,1.4,3,trials)
pesticide_ft2_rows_per_acre_yr1 = 2922 # Depends on number of trees planted, equations are in EInputs o42 to o48
pesticide_ft2_rows_per_acre_yr2on = 3652 # I don't understand this metric. equations are in Einputs o42 to o 48
pesticide_applications_yr1_count = np.random.triangular(1,2,3,trials)
pesticide_applications_yr2_3_count = np.random.triangular(2,4,6,trials)

#Orchard Fertilizers
fertilizer_DAP_kg_tree = np.random.triangular(0,1.4,2.8,trials)
fertilizer_DAP_fraction_N = .18
fertilizer_DAP_fraction_P2O5 = .46
fertilizer_potash_kg_tree = np.random.triangular(0,.69,1.4,trials)
fertilizer_potash_fraction_K2O = .6
urea_year2_kgN_tree = np.random.triangular(0, .23, .3, trials)
urea_year3_kgN_tree = np.random.triangular(0, .37, .4, trials)
urea_year4_kgN_tree = np.random.triangular(0, .51, .6, trials)
urea_year5_kgN_tree = np.random.triangular(0, .74, .8, trials)
urea_fraction_N = .46

#Nut Harvesting Activities
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

#Wood Harvesting Activities
tree_harvesting_rate_min_tree = np.random.triangular(1,2,3,trials)


'''-------------------------------------INVENTORY CALCULATOR------------------------------------------------'''

"""ESTABLISHMENT PHASE"""
#ESTABLISHMENT INVENTORY NUTS AND WOOD

#tree pesticide application hectares
nw_pesticide_application_yr1_ha_tree = acres_per_trt * ha_per_acre * pesticide_applications_yr1_count
nw_pesticide_application_yr2_3_ha_tree = acres_per_trt * ha_per_acre * pesticide_applications_yr2_3_count
nw_pesticide_application_ha_trt = nw_pesticide_application_yr1_ha_tree + nw_pesticide_application_yr2_3_ha_tree
nw_pesticide_application_ha_tree = nw_pesticide_application_ha_trt / trees_per_trt

#tree pesticide kg ai
surflan_yr1_kgai_trt = (surflan_yr1_kgai_acre * (pesticide_ft2_rows_per_acre_yr1/ft2_per_acre) *
                        acres_per_trt)
surflan_yr2_3_kgai_trt = (surflan_yr2_3_kgai_acre * (pesticide_ft2_rows_per_acre_yr2on/ft2_per_acre) *
                        acres_per_trt)
poast_yr1_kgai_trt = (poast_yr1_kgai_acre * (pesticide_ft2_rows_per_acre_yr1/ft2_per_acre) *
                        acres_per_trt)
nw_pesticide_kgai_trt = surflan_yr1_kgai_trt + surflan_yr2_3_kgai_trt + poast_yr1_kgai_trt
nw_pesticide_kgai_tree = nw_pesticide_kgai_trt / trees_per_trt

#kg N from urea years 2 and 3
nw_urea_yr2_kgN_trt = urea_year2_kgN_tree * trees_per_trt * urea_fraction_N
nw_urea_yr3_kgN_trt = urea_year3_kgN_tree * trees_per_trt * urea_fraction_N
nw_urea_kgN_trt = urea_year2_kgN_tree + urea_year3_kgN_tree
nw_urea_kgN_tree = nw_urea_kgN_trt / trees_per_trt

#ESTABLLISHMENT INVENTORY HAY

# kg N fertilizer (DAP)
hay_Nfertilizer_kg_trt = fertilizer_DAP_kg_tree * trees_per_trt * fertilizer_DAP_fraction_N
hay_Nfertilizer_kg_tree = hay_Nfertilizer_kg_trt / trees_per_trt

#kg P2O5 fertilizer
hay_P2O5fertilizer_kg_trt = fertilizer_DAP_kg_tree * trees_per_trt * fertilizer_DAP_fraction_P2O5
hay_P2O5fertilizer_kg_tree = hay_P2O5fertilizer_kg_trt / trees_per_trt

#kg K2O fertilizer
hay_potassium_chloride_kg_trt = fertilizer_potash_kg_tree * trees_per_trt * fertilizer_potash_fraction_K2O
hay_potassium_chloride_kg_tree = hay_potassium_chloride_kg_trt / trees_per_trt

#ha tillage
hay_tillage_ha_trt = acres_per_trt * ha_per_acre * is_tilled
hay_tillage_ha_tree = hay_tillage_ha_trt / trees_per_trt

#petrol used to deliver seeds to site
hay_petrol_seed_delivery_kg_trt = (seed_delivery_miles_roundtrip/seed_delivery_mpg) * petrol_kg_per_gal
hay_petrol_seed_delivery_kg_tree = hay_petrol_seed_delivery_kg_trt / trees_per_trt

#kg grass seed
hay_grass_seed_kg_trt = (grass_seeding_rate_lb_acre / lbs_per_kg) * acres_per_trt
hay_grass_seed_kg_tree = hay_grass_seed_kg_trt / trees_per_trt

#ha mowed
hay_mowing_ha_trt = ((ha_per_acre/trees_per_acre) * trees_per_trt * cutting_pasture_times_per_year *
                     orchard_years_for_establishment)
hay_mowing_ha_tree = hay_mowing_ha_trt / trees_per_trt

#ha pesticide applications
hay_pesticide_application_ha_trt = ha_per_trt * pesticide_applications_btwn_rows_yr_2_3_count
hay_pesticide_application_ha_tree = hay_pesticide_application_ha_trt / trees_per_trt

"""PRODUCTION PHASE"""
#Nut and Wood Production
#hectares applied by pesticide broadcaster
nw_prod_pesticide_application_ha_trt = (ha_per_trt * pesticide_applications_count *
                                        pesticide_wand_0_or_broadcaster_1)
nw_prod_pesticide_application_ha_tree = nw_prod_pesticide_application_ha_trt / trees_per_trt

#kg pesticide applied
nw_prod_pesticide_kg_trt = (pesticide_kgai_per_acre_per_application * (pesticide_ft2_rows_per_acre_yr2on/ft2_per_acre) *
                            pesticide_applications_count * acres_per_trt)
nw_prod_pesticide_kg_tree = nw_prod_pesticide_kg_trt / trees_per_trt

#kg N from Urea
nw_prod_urea_year4_kgN_tree = urea_year4_kgN_tree * trees_per_trt * urea_fraction_N
nw_prod_urea_year5_kgN_tree = urea_year5_kgN_tree * trees_per_trt * urea_fraction_N
nw_prod_urea_kgN_trt = nw_prod_urea_year4_kgN_tree + nw_prod_urea_year5_kgN_tree
nw_prod_urea_kgN_tree = nw_prod_urea_kgN_trt / trees_per_trt

#NUT PRODUCTION

#harvester - kilograms of unspecified ag machinery (I don't understand this metric)
nut_prod_harvester_kg_trt = (harvester_used * (acres_per_trt/harvester_speed_acres_hr) *
                            (harvester_mass_kg/harvester_lifespan_hr) * (orchard_life_years - orchard_years_to_production))
nut_prod_harvester_kg_tree = nut_prod_harvester_kg_trt / trees_per_trt

#shaker - kilograms of unspecified ag machinery (I don't understand this metric)
nut_prod_shaker_kg_trt = (shaker_used * (trees_per_trt/shaker_speed_trees_hr) *
                            (shaker_mass_kg/shaker_lifespan_hr) * (orchard_life_years - orchard_years_to_production))
nut_prod_shaker_kg_tree = nut_prod_shaker_kg_trt / trees_per_trt

#sweeper - kilograms of unspecified ag machinery (I don't understand this metric)
nut_prod_sweeper_kg_trt = (sweeper_used * (acres_per_trt/sweeper_speed_acres_hr) *
                            (sweeper_mass_kg/sweeper_lifespan_hr) * (orchard_life_years - orchard_years_to_production))
nut_prod_sweeper_kg_tree = nut_prod_sweeper_kg_trt / trees_per_trt

#kg diesel used in harvesting process
harvester_diesel_gal_trt = harvester_fuel_use_gal_hr * (acres_per_trt/harvester_speed_acres_hr) * harvester_used
shaker_diesel_gal_trt = shaker_fuel_use_gal_hr * (trees_per_trt/shaker_speed_trees_hr) * shaker_used
sweeper_diesel_gal_trt = sweeper_fuel_use_gal_hr * (acres_per_trt/sweeper_speed_acres_hr) * sweeper_used
nut_prod_diesel_harvesting_kg_trt = ((harvester_diesel_gal_trt + shaker_diesel_gal_trt + sweeper_diesel_gal_trt) *
                                     diesel_kg_per_gal * (orchard_life_years - orchard_years_to_production))
nut_prod_diesel_harvesting_kg_tree = nut_prod_diesel_harvesting_kg_trt / trees_per_trt

#HAY PRODUCTION PHASE (a lot of these variables should be made dependent on how much grass seed was put down?)

#hectares hayed
hay_prod_haying_before_resow_ha_trt = ((acres_per_trt * ha_per_acre) * cutting_pasture_times_per_year *
                                       pasture_life_years)
hay_prod_haying_after_resow_ha_trt = ((acres_per_trt * ha_per_acre) * cutting_pasture_times_per_year *
                                      (orchard_life_years - pasture_life_years)) * is_resown
hay_prod_haying_ha_trt = hay_prod_haying_before_resow_ha_trt + hay_prod_haying_after_resow_ha_trt
hay_prod_haying_ha_tree = hay_prod_haying_ha_trt / trees_per_trt

#hectares mowed
hay_prod_mowing_ha_trt = hay_prod_haying_ha_trt
hay_prod_mowing_ha_tree = hay_prod_haying_ha_tree

# number of 700 kg bales produced
hay_prod_baling_before_resow_p_trt = (dry_hay_tons_per_trt * (kg_per_ton/kg_per_hay_bale) *
                                       cutting_pasture_times_per_year * pasture_life_years *
                                       baling_silage_correction_factor)
hay_prod_baling_after_resow_p_trt = (dry_hay_tons_per_trt * (kg_per_ton/kg_per_hay_bale) *
                                       cutting_pasture_times_per_year * (orchard_life_years - pasture_life_years) *
                                       baling_silage_correction_factor) * is_resown
hay_prod_baling_p_trt = hay_prod_baling_before_resow_p_trt + hay_prod_baling_after_resow_p_trt
hay_prod_baling_p_tree = hay_prod_baling_p_trt / trees_per_trt

# number of 700 kg bales loaded
hay_prod_bale_loading_before_resow_p_trt = (dry_hay_tons_per_trt * (kg_per_ton/kg_per_hay_bale) *
                                           cutting_pasture_times_per_year * pasture_life_years)
hay_prod_bale_loading_after_resow_p_trt = (dry_hay_tons_per_trt * (kg_per_ton/kg_per_hay_bale) *
                                           cutting_pasture_times_per_year * (orchard_life_years - pasture_life_years)
                                            * is_resown)
hay_prod_bale_loading_p_trt = hay_prod_bale_loading_before_resow_p_trt + hay_prod_bale_loading_after_resow_p_trt
hay_prod_bale_loading_p_tree = hay_prod_bale_loading_p_trt / trees_per_trt

# kg petrol used in delivering seeds to site
hay_prod_petrol_seed_delivery_kg_tree = (seed_delivery_miles_roundtrip/seed_delivery_mpg) * (petrol_kg_per_gal/trees_per_trt) * is_resown
hay_prod_petrol_seed_delivery_kg_trt = hay_prod_petrol_seed_delivery_kg_tree * trees_per_trt

#kg grass seed spread
hay_prod_grass_seed_kg_trt = (grass_seeding_rate_lb_acre/lbs_per_kg) * acres_per_trt * is_resown
hay_prod_grass_seed_kg_tree = hay_prod_grass_seed_kg_trt / trees_per_trt

'''DESTRUCTION PHASE'''
#WOOD DESTRUCTION
#hours spent harvesting
wood_dest_harvesting_hr_tree = tree_harvesting_rate_min_tree/min_per_hr
wood_dest_harvesting_hr_trt = wood_dest_harvesting_hr_tree * trees_per_trt




'''-----------------------------SINGLE CROP, SINGLE PHASE IMPACT CALCULATORS---------------------------'''

'''ESTABLISHMENT PHASE'''

#Calculates Nut/Wood Establishment Impact Distributions by Category
def NW_estab_impact_calc():
    OzDep_NW_estab = []
    GWP_NW_estab = []
    Smog_NW_estab = []
    Acid_NW_estab = []
    Eut_NW_estab = []
    Cancer_NW_estab = []
    Non_Cancer_NW_estab = []
    Resp_NW_estab = []
    EcoTox_NW_estab = []
    FuelDep_NW_estab = []

    for i in range(trials):
        nut_estab_impact = nw_pesticide_application_ha_tree[i] * imp.pesticide_application_impact_dict + \
            nw_pesticide_kgai_tree[i] * imp.pesticide_impact_dict + \
            nw_urea_kgN_tree[i] * imp.urea_impact_dict

        OzDep_NW_estab.append(nut_estab_impact[0])
        GWP_NW_estab.append(nut_estab_impact[1])
        Smog_NW_estab.append(nut_estab_impact[2])
        Acid_NW_estab.append(nut_estab_impact[3])
        Eut_NW_estab.append(nut_estab_impact[4])
        Cancer_NW_estab.append(nut_estab_impact[5])
        Non_Cancer_NW_estab.append(nut_estab_impact[6])
        Resp_NW_estab.append(nut_estab_impact[7])
        EcoTox_NW_estab.append(nut_estab_impact[8])
        FuelDep_NW_estab.append(nut_estab_impact[9])

    return OzDep_NW_estab, GWP_NW_estab, Smog_NW_estab, Acid_NW_estab, Eut_NW_estab, Cancer_NW_estab, \
Non_Cancer_NW_estab, Resp_NW_estab, EcoTox_NW_estab, FuelDep_NW_estab


#Calculates Hay Establishment Impact by Category
def hay_estab_impact_calc():
    OzDep_hay_estab = []
    GWP_hay_estab = []
    Smog_hay_estab = []
    Acid_hay_estab = []
    Eut_hay_estab = []
    Cancer_hay_estab = []
    Non_Cancer_hay_estab = []
    Resp_hay_estab = []
    EcoTox_hay_estab = []
    FuelDep_hay_estab = []

    for i in range(trials):
        hay_estab_impact = hay_Nfertilizer_kg_tree[i] * imp.N_fertilizer_impact_dict + \
            hay_P2O5fertilizer_kg_tree[i] * imp.phosphate_fertilizer_impact_dict + \
            hay_potassium_chloride_kg_tree[i] * imp.potassium_chloride_fertilizer_impact_dict + \
            hay_tillage_ha_tree[i] * imp.tillage_impact_dict + \
            hay_petrol_seed_delivery_kg_tree[i] * imp.petrol_impact_dict + \
            hay_grass_seed_kg_tree[i] * imp.grass_seed_impact_dict + \
            hay_mowing_ha_tree[i] * imp.mowing_impact_dict + \
            hay_pesticide_application_ha_tree[i] * imp.pesticide_application_impact_dict

        OzDep_hay_estab.append(hay_estab_impact[0])
        GWP_hay_estab.append(hay_estab_impact[1])
        Smog_hay_estab.append(hay_estab_impact[2])
        Acid_hay_estab.append(hay_estab_impact[3])
        Eut_hay_estab.append(hay_estab_impact[4])
        Cancer_hay_estab.append(hay_estab_impact[5])
        Non_Cancer_hay_estab.append(hay_estab_impact[6])
        Resp_hay_estab.append(hay_estab_impact[7])
        EcoTox_hay_estab.append(hay_estab_impact[8])
        FuelDep_hay_estab.append(hay_estab_impact[9])

    return OzDep_hay_estab, GWP_hay_estab, Smog_hay_estab, Acid_hay_estab, Eut_hay_estab, Cancer_hay_estab, \
               Non_Cancer_hay_estab, Resp_hay_estab, EcoTox_hay_estab, FuelDep_hay_estab


'''PRODUCTION PHASE'''

#Nut/Wood Production Imapct by Category
def NW_prod_impact_calc():

    OzDep_NW_prod = []
    GWP_NW_prod = []
    Smog_NW_prod = []
    Acid_NW_prod = []
    Eut_NW_prod = []
    Cancer_NW_prod = []
    Non_Cancer_NW_prod = []
    Resp_NW_prod = []
    EcoTox_NW_prod = []
    FuelDep_NW_prod = []

    for i in range(trials):
        nw_prod_impact = nw_prod_pesticide_application_ha_tree[i] * imp.pesticide_application_impact_dict + \
            nw_prod_pesticide_kg_tree[i] * imp.pesticide_impact_dict + \
            nw_prod_urea_kgN_tree[i] * imp.urea_impact_dict

        OzDep_NW_prod.append(nw_prod_impact[0])
        GWP_NW_prod.append(nw_prod_impact[1])
        Smog_NW_prod.append(nw_prod_impact[2])
        Acid_NW_prod.append(nw_prod_impact[3])
        Eut_NW_prod.append(nw_prod_impact[4])
        Cancer_NW_prod.append(nw_prod_impact[5])
        Non_Cancer_NW_prod.append(nw_prod_impact[6])
        Resp_NW_prod.append(nw_prod_impact[7])
        EcoTox_NW_prod.append(nw_prod_impact[8])
        FuelDep_NW_prod.append(nw_prod_impact[9])

    return OzDep_NW_prod, GWP_NW_prod, Smog_NW_prod, Acid_NW_prod, Eut_NW_prod, Cancer_NW_prod, \
           Non_Cancer_NW_prod, Resp_NW_prod, EcoTox_NW_prod, FuelDep_NW_prod


#Nut Prdocution Impact by Category
def nut_prod_impact_calc():

    OzDep_nut_prod = []
    GWP_nut_prod = []
    Smog_nut_prod = []
    Acid_nut_prod = []
    Eut_nut_prod = []
    Cancer_nut_prod = []
    Non_Cancer_nut_prod = []
    Resp_nut_prod = []
    EcoTox_nut_prod = []
    FuelDep_nut_prod = []

    for i in range(trials):
        nut_prod_impact = nut_prod_harvester_kg_tree[i] * imp.unspecified_ag_machinery_impact_dict + \
            nut_prod_shaker_kg_tree[i] * imp.unspecified_ag_machinery_impact_dict + \
            nut_prod_sweeper_kg_tree[i] * imp.unspecified_ag_machinery_impact_dict + \
            nut_prod_diesel_harvesting_kg_tree[i] * imp.diesel_impact_dict

        OzDep_nut_prod.append(nut_prod_impact[0])
        GWP_nut_prod.append(nut_prod_impact[1])
        Smog_nut_prod.append(nut_prod_impact[2])
        Acid_nut_prod.append(nut_prod_impact[3])
        Eut_nut_prod.append(nut_prod_impact[4])
        Cancer_nut_prod.append(nut_prod_impact[5])
        Non_Cancer_nut_prod.append(nut_prod_impact[6])
        Resp_nut_prod.append(nut_prod_impact[7])
        EcoTox_nut_prod.append(nut_prod_impact[8])
        FuelDep_nut_prod.append(nut_prod_impact[9])

    return OzDep_nut_prod, GWP_nut_prod, Smog_nut_prod, Acid_nut_prod, Eut_nut_prod, Cancer_nut_prod, \
           Non_Cancer_nut_prod, Resp_nut_prod, EcoTox_nut_prod, FuelDep_nut_prod


#Total Chestnut Tree (nut inventory + NW inventory) Production Impact
def chestnut_tree_prod_impact_calc():
    chestnut_tree_prod_impact = []
    chestnut_tree_prod_impact_category = []

    nw_prod_impact = nut_prod_impact_calc()
    nut_prod_impact = NW_prod_impact_calc()

    for i in range(10):
        for j in range(trials):
            chestnut_tree_prod_impact_trial = nw_prod_impact[i][j] + nut_prod_impact[i][j]
            chestnut_tree_prod_impact_category.append(chestnut_tree_prod_impact_trial)
        chestnut_tree_prod_impact.append(chestnut_tree_prod_impact_category)
        chestnut_tree_prod_impact_category = []

    OzDep_chestnut_tree_prod = chestnut_tree_prod_impact[0]
    GWP_chestnut_tree_prod = chestnut_tree_prod_impact[1]
    Smog_chestnut_tree_prod = chestnut_tree_prod_impact[2]
    Acid_chestnut_tree_prod = chestnut_tree_prod_impact[3]
    Eut_chestnut_tree_prod = chestnut_tree_prod_impact[4]
    Cancer_chestnut_tree_prod = chestnut_tree_prod_impact[5]
    Non_Cancer_chestnut_tree_prod = chestnut_tree_prod_impact[6]
    Resp_chestnut_tree_prod = chestnut_tree_prod_impact[7]
    EcoTox_chestnut_tree_prod = chestnut_tree_prod_impact[8]
    FuelDep_chestnut_tree_prod = chestnut_tree_prod_impact[9]

    return OzDep_chestnut_tree_prod, GWP_chestnut_tree_prod, Smog_chestnut_tree_prod, Acid_chestnut_tree_prod, \
           Eut_chestnut_tree_prod, Cancer_chestnut_tree_prod,\
           Non_Cancer_chestnut_tree_prod, Resp_chestnut_tree_prod, EcoTox_chestnut_tree_prod, FuelDep_chestnut_tree_prod


#Hay Production Impact
def hay_prod_impact_calc():
    OzDep_hay_prod = []
    GWP_hay_prod = []
    Smog_hay_prod = []
    Acid_hay_prod = []
    Eut_hay_prod = []
    Cancer_hay_prod = []
    Non_Cancer_hay_prod = []
    Resp_hay_prod = []
    EcoTox_hay_prod = []
    FuelDep_hay_prod = []

    for i in range(trials):
        hay_prod_impact = hay_prod_mowing_ha_tree[i] * imp.mowing_impact_dict + \
                          hay_prod_haying_ha_tree[i] * imp.haying_impact_dict + \
                          hay_prod_baling_p_tree[i] * imp.baling_impact_dict + \
                          hay_prod_bale_loading_p_tree[i] * imp.bale_loading_impact_dict + \
                          hay_prod_petrol_seed_delivery_kg_tree[i] * imp.petrol_impact_dict + \
                          hay_prod_grass_seed_kg_tree[i] * imp.grass_seed_impact_dict

        OzDep_hay_prod.append(hay_prod_impact[0])
        GWP_hay_prod.append(hay_prod_impact[1])
        Smog_hay_prod.append(hay_prod_impact[2])
        Acid_hay_prod.append(hay_prod_impact[3])
        Eut_hay_prod.append(hay_prod_impact[4])
        Cancer_hay_prod.append(hay_prod_impact[5])
        Non_Cancer_hay_prod.append(hay_prod_impact[6])
        Resp_hay_prod.append(hay_prod_impact[7])
        EcoTox_hay_prod.append(hay_prod_impact[8])
        FuelDep_hay_prod.append(hay_prod_impact[9])

    return OzDep_hay_prod, GWP_hay_prod, Smog_hay_prod, Acid_hay_prod, Eut_hay_prod, Cancer_hay_prod, \
               Non_Cancer_hay_prod, Resp_hay_prod, EcoTox_hay_prod, FuelDep_hay_prod


'''DESTRUCTION PHASE'''
#Wood Destruction Phase Impact
def wood_dest_impact_calc():
    OzDep_wood_dest = []
    GWP_wood_dest = []
    Smog_wood_dest = []
    Acid_wood_dest = []
    Eut_wood_dest = []
    Cancer_wood_dest = []
    Non_Cancer_wood_dest = []
    Resp_wood_dest= []
    EcoTox_wood_dest = []
    FuelDep_wood_dest = []

    for i in range(trials):
        wood_dest_impact = wood_dest_harvesting_hr_trt[i] * imp.tree_harvesting_impact_dict

        OzDep_wood_dest.append(wood_dest_impact[0])
        GWP_wood_dest.append(wood_dest_impact[1])
        Smog_wood_dest.append(wood_dest_impact[2])
        Acid_wood_dest.append(wood_dest_impact[3])
        Eut_wood_dest.append(wood_dest_impact[4])
        Cancer_wood_dest.append(wood_dest_impact[5])
        Non_Cancer_wood_dest.append(wood_dest_impact[6])
        Resp_wood_dest.append(wood_dest_impact[7])
        EcoTox_wood_dest.append(wood_dest_impact[8])
        FuelDep_wood_dest.append(wood_dest_impact[9])

    return OzDep_wood_dest, GWP_wood_dest, Smog_wood_dest, Acid_wood_dest, Eut_wood_dest, Cancer_wood_dest, \
               Non_Cancer_wood_dest, Resp_wood_dest, EcoTox_wood_dest, FuelDep_wood_dest


'''-----------------------------SINGLE PHASE TOTAL IMPACT CALCULATORS (COMBINE ALL CROPS)---------------------------'''

'''ESTABLISHMENT PHASE'''
#calculates total establishment phase impact
def total_estab_impact_calc():
    total_estab_impact = []
    total_estab_impact_category = []

    hay_estab_impact = hay_estab_impact_calc()
    NW_estab_impact = NW_estab_impact_calc()

    for i in range(10):
        for j in range(trials):
            total_estab_impact_trial = hay_estab_impact[i][j] + NW_estab_impact[i][j]
            total_estab_impact_category.append(total_estab_impact_trial)
        total_estab_impact.append(total_estab_impact_category)
        total_estab_impact_category = []


    OzDep_total_estab = total_estab_impact[0]
    GWP_total_estab = total_estab_impact[1]
    Smog_total_estab = total_estab_impact[2]
    Acid_total_estab = total_estab_impact[3]
    Eut_total_estab = total_estab_impact[4]
    Cancer_total_estab = total_estab_impact[5]
    Non_Cancer_total_estab = total_estab_impact[6]
    Resp_total_estab = total_estab_impact[7]
    EcoTox_total_estab = total_estab_impact[8]
    FuelDep_total_estab = total_estab_impact[9]

    return OzDep_total_estab, GWP_total_estab, Smog_total_estab, Acid_total_estab, Eut_total_estab, Cancer_total_estab,\
           Non_Cancer_total_estab, Resp_total_estab, EcoTox_total_estab, FuelDep_total_estab


'''PRODUCTION PHASE'''

#Calculates Total Production Phase Impact
def total_prod_impact_calc():
    total_prod_impact = []
    total_prod_impact_category = []

    chestnut_tree_prod_impact = chestnut_tree_prod_impact_calc()
    hay_prod_impact = hay_prod_impact_calc()

    for i in range(10):
        for j in range(trials):
            total_prod_impact_trial = chestnut_tree_prod_impact[i][j] + hay_prod_impact[i][j]
            total_prod_impact_category.append(total_prod_impact_trial)
        total_prod_impact.append(total_prod_impact_category)
        total_prod_impact_category = []


    OzDep_total_prod = total_prod_impact[0]
    GWP_total_prod = total_prod_impact[1]
    Smog_total_prod = total_prod_impact[2]
    Acid_total_prod = total_prod_impact[3]
    Eut_total_prod = total_prod_impact[4]
    Cancer_total_prod = total_prod_impact[5]
    Non_Cancer_total_prod = total_prod_impact[6]
    Resp_total_prod = total_prod_impact[7]
    EcoTox_total_prod = total_prod_impact[8]
    FuelDep_total_prod = total_prod_impact[9]

    return OzDep_total_prod, GWP_total_prod, Smog_total_prod, Acid_total_prod, Eut_total_prod, Cancer_total_prod,\
           Non_Cancer_total_prod, Resp_total_prod, EcoTox_total_prod, FuelDep_total_prod


'''DESTRUCTION PHASE'''
# Calculates Total Destruction Phase impacts by category
def total_dest_impact_calc():
    total_dest_impact = wood_dest_impact_calc()

    return total_dest_impact


'''-----------------------------SINGLE CROP TOTAL IMPACT CALCULATORS (COMBINE ALL PHASES)---------------------------'''
#calculates Chestnut Tree Impact Totals for All Phases
def total_chestnut_tree_impact_calc():
    total_chestnut_tree_impact = []
    total_chestnut_tree_impact_category = []

    chestnut_tree_prod_impact = chestnut_tree_prod_impact_calc()
    NW_estab_impact = NW_estab_impact_calc()

    for i in range(10):
        for j in range(trials):
            total_chestnut_tree_impact_trial = chestnut_tree_prod_impact[i][j] + NW_estab_impact[i][j]
            total_chestnut_tree_impact_category.append(total_chestnut_tree_impact_trial)
        total_chestnut_tree_impact.append(total_chestnut_tree_impact_category)
        total_chestnut_tree_impact_category = []


    OzDep_total_chestnut_tree = total_chestnut_tree_impact[0]
    GWP_total_chestnut_tree = total_chestnut_tree_impact[1]
    Smog_total_chestnut_tree = total_chestnut_tree_impact[2]
    Acid_total_chestnut_tree = total_chestnut_tree_impact[3]
    Eut_total_chestnut_tree = total_chestnut_tree_impact[4]
    Cancer_total_chestnut_tree = total_chestnut_tree_impact[5]
    Non_Cancer_total_chestnut_tree = total_chestnut_tree_impact[6]
    Resp_total_chestnut_tree = total_chestnut_tree_impact[7]
    EcoTox_total_chestnut_tree = total_chestnut_tree_impact[8]
    FuelDep_total_chestnut_tree = total_chestnut_tree_impact[9]

    return OzDep_total_chestnut_tree, GWP_total_chestnut_tree, Smog_total_chestnut_tree, Acid_total_chestnut_tree, Eut_total_chestnut_tree, Cancer_total_chestnut_tree,\
           Non_Cancer_total_chestnut_tree, Resp_total_chestnut_tree, EcoTox_total_chestnut_tree, FuelDep_total_chestnut_tree


#calculates Hay Impact Totals for All Phases
def total_hay_impact_calc():
    total_hay_impact = []
    total_hay_impact_category = []

    hay_prod_impact = hay_prod_impact_calc()
    hay_estab_impact = hay_estab_impact_calc()

    for i in range(10):
        for j in range(trials):
            total_hay_impact_trial = hay_prod_impact[i][j] + hay_estab_impact[i][j]
            total_hay_impact_category.append(total_hay_impact_trial)
        total_hay_impact.append(total_hay_impact_category)
        total_hay_impact_category = []


    OzDep_total_hay = total_hay_impact[0]
    GWP_total_hay = total_hay_impact[1]
    Smog_total_hay = total_hay_impact[2]
    Acid_total_hay = total_hay_impact[3]
    Eut_total_hay = total_hay_impact[4]
    Cancer_total_hay = total_hay_impact[5]
    Non_Cancer_total_hay = total_hay_impact[6]
    Resp_total_hay = total_hay_impact[7]
    EcoTox_total_hay = total_hay_impact[8]
    FuelDep_total_hay = total_hay_impact[9]

    return OzDep_total_hay, GWP_total_hay, Smog_total_hay, Acid_total_hay, Eut_total_hay, Cancer_total_hay,\
           Non_Cancer_total_hay, Resp_total_hay, EcoTox_total_hay, FuelDep_total_hay


'''-----------------------------WHOLE PLOT IMPACT CALCULATOR (ALL CROPS, ALL PHASES)--------------------------------'''

# Calculates Total Impact of All Plants over all Phases by Category
def total_plot_impact_calc():
    total_plot_impact = []
    total_plot_impact_category = []

    total_prod_impact = total_prod_impact_calc()
    total_estab_impact = total_estab_impact_calc()
    total_dest_impact = total_dest_impact_calc()

    for i in range(10):
        for j in range(trials):
            total_plot_impact_trial = total_prod_impact[i][j] + total_estab_impact[i][j] + total_dest_impact[i][j]
            total_plot_impact_category.append(total_plot_impact_trial)
        total_plot_impact.append(total_plot_impact_category)
        total_plot_impact_category = []

    OzDep_total_plot = total_plot_impact[0]
    GWP_total_plot = total_plot_impact[1]
    Smog_total_plot = total_plot_impact[2]
    Acid_total_plot = total_plot_impact[3]
    Eut_total_plot = total_plot_impact[4]
    Cancer_total_plot = total_plot_impact[5]
    Non_Cancer_total_plot = total_plot_impact[6]
    Resp_total_plot = total_plot_impact[7]
    EcoTox_total_plot = total_plot_impact[8]
    FuelDep_total_plot = total_plot_impact[9]

    return OzDep_total_plot, GWP_total_plot, Smog_total_plot, Acid_total_plot, Eut_total_plot, Cancer_total_plot, \
           Non_Cancer_total_plot, Resp_total_plot, EcoTox_total_plot, FuelDep_total_plot


'''-------------------------BOX PLOT MAKING CODE---------------------------------------------------'''

#Makes Nut/Wood Estab Box Plots

x = total_plot_impact_calc()

my_file = open('out.txt', 'w')
my_file.write(str(x))
my_file.close()

fig = plt.figure()
ax0 = fig.add_subplot(2,5,1)
plt.boxplot(x[0])
ax1 = fig.add_subplot(2,5,2)
plt.boxplot(x[1])
ax2 = fig.add_subplot(2,5,3)
plt.boxplot(x[2])
ax3 = fig.add_subplot(2,5,4)
plt.boxplot(x[3])
ax4 = fig.add_subplot(2,5,5)
plt.boxplot(x[4])
ax5 = fig.add_subplot(2,5,6)
plt.boxplot(x[5])
ax6 = fig.add_subplot(2,5,7)
plt.boxplot(x[6])
ax7 = fig.add_subplot(2,5,8)
plt.boxplot(x[7])
ax8 = fig.add_subplot(2,5,9)
plt.boxplot(x[8])
ax9 = fig.add_subplot(2,5,10)
plt.boxplot(x[9])

fig.suptitle('Total Production Impacts')
ax0.title.set_text('Ozone Depletion (kg CFC11 eq)')
ax1.title.set_text('Global Warming Potential (kg CO2 eq)')
ax2.title.set_text('Smog (kg O3 eq)')
ax3.title.set_text('Acidification (kg SO2 eq)')
ax4.title.set_text('Eutrophication (kg N eq)')
ax5.title.set_text('Carcinogenics (CTUh)')
ax6.title.set_text('Non-Carcinogenics (CTUh)')
ax7.title.set_text('Respiratory Effects (kg PM2.5 eq)')
ax8.title.set_text('Ecotoxicity (CTUe)')
ax9.title.set_text('Fossil Fuel Depletion (MJ surplus)')
plt.show()