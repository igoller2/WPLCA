import Impact_Dictionaries as dict

#Calculates Impacts of Rotary Mowing per Tree
hay_mowing_ha = input("number of ha mowed per tree")
hay_mowing_impact = {}
for key in dict.mowing_impact_dict:
    hay_mowing_impact[key]= float(hay_mowing_ha) * dict.mowing_impact_dict[key]

print(hay_mowing_impact)

#Calculates Impacts of Diesel Used in Harvesting per Tree
diesel_harvesting_kg = input("number of kg diesel per tree")
diesel_harvesting_impact = {}
for key in dict.diesel_impact_dict:
    diesel_harvesting_impact[key] = float(diesel_harvesting_kg) * dict.diesel_impact_dict[key]

print(diesel_harvesting_impact)


