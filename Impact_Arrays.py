import numpy as np

Names = [
    'Ozone Depletion (kg CFC11 eq)',
    'Global Warming Potential (kg CO2 eq)',
    'Smog (kg O3 eq)',
    'Acidification (kg SO2 eq)',
    'Eutrophication (kg N eq)',
    'Carcinogenics (CTUh)',
    'Non-Carcinogenics (CTUh)',
    'Respiratory Effects (kg PM2.5 eq)',
    'Ecotoxicity (CTUe)',
    'Fossil Fuel Depletion (MJ surplus)'
]

bale_loading_impact_dict = np.array([
    6.559E-08,
    2.847E-01,
    8.353E-02,
    2.643E-03,
    2.446E-04,
    1.818E-10,
    6.226E-07,
    3.703E-04,
    3.377E-01,
    5.796E-01
])


baling_impact_dict = np.array([
    6.669E-07 ,
    5.153E+00,
    9.092E-01,
    3.504E-02 ,
    8.705E-03 ,
    8.258E-08 ,
    4.533E-06 ,
    5.034E-03 ,
    9.355E+00,
    1.622E+01
])

diesel_impact_dict = np.array([
    1.836E-06 ,
    1.123E+00,
    9.052E-02 ,
    1.045E-02 ,
    3.858E-03 ,
    2.912E-08 ,
    1.216E-07 ,
    9.083E-04 ,
    2.938E+00,
    1.626E+01
])

#is this supposed to have a negative non-cancer impact?
grass_seed_impact_dict = np.array([
    2.144E-07 ,
    2.481E+00,
    1.759E-01 ,
    1.757E-02 ,
    2.788E-02 ,
    1.323E-07 ,
    -2.205E-08 ,
    1.712E-03 ,
    1.495E+01,
    2.142E+00
])

haying_impact_dict = np.array([
    1.553E-06 ,
    6.710E+00,
    2.185E+00 ,
    6.844E-02 ,
    6.163E-03 ,
    4.320E-09 ,
    1.695E-05 ,
    8.276E-03 ,
    9.068E+00,
    1.372E+01
])

mowing_impact_dict = np.array([
    4.407E-06 ,
    2.542E+01,
    4.796E+00 ,
    1.914E-01 ,
    6.016E-02 ,
    1.660E-06 ,
    3.283E-05 ,
    3.446E-02 ,
    1.496E+02,
    3.978E+01
])

N_fertilizer_impact_dict = np.array([
    8.993E-07 ,
    3.376E+00,
    2.283E-01 ,
    4.142E-02 ,
    2.576E-02 ,
    3.028E-07 ,
    1.879E-06 ,
    5.440E-03 ,
    5.411E+01,
    8.552E+00
])

pesticide_application_impact_dict = np.array([
    2.006E-06 ,
    1.232E+01,
    2.323E+00 ,
    9.647E-02 ,
    3.477E-02 ,
    9.502E-07 ,
    2.346E-05 ,
    1.233E-02 ,
    9.496E+01,
    1.825E+01
])

pesticide_impact_dict = np.array([
    1.971E-05 ,
    1.025E+01,
    7.618E-01 ,
    9.612E-02 ,
    8.088E-02 ,
    5.017E-07 ,
    3.347E-06 ,
    8.948E-03,
    1.468E+02,
    1.906E+01
])

petrol_impact_dict = np.array([
    1.769E-06 ,
    1.360E+00,
    9.778E-02 ,
    1.124E-02,
    4.008E-03 ,
    3.217E-08 ,
    1.480E-07 ,
    9.883E-04,
    3.728E+00,
    1.619E+01
])

phosphate_fertilizer_impact_dict= np.array([
    4.582E-07 ,
    1.720E+00,
    1.163E-01 ,
    2.110E-02 ,
    1.312E-02 ,
    1.543E-07 ,
    9.571E-07,
    2.772E-03,
    2.757E+01,
    4.357E+00
])

potassium_chloride_fertilizer_impact_dict= np.array([
    6.377E-08 ,
    4.561E-01,
    2.487E-02 ,
    2.331E-03 ,
    1.593E-03 ,
    3.693E-08,
    2.534E-07,
    2.809E-04,
    9.452E+00,
    9.886E-01
])

tillage_impact_dict = np.array([
    2.395E-05 ,
    1.216E+02,
    2.791E+01 ,
    1.002E+00,
    2.189E-01 ,
    5.113E-06 ,
    1.028E-04 ,
    1.873E-01,
    4.691E+02,
    2.140E+02
])

tree_harvesting_impact_dict = np.array([
    1.203E-05,
    4.942E+01,
    5.167E+00 ,
    1.996E-01 ,
    4.526E-02 ,
    8.810E-08 ,
    1.397E-06 ,
    1.768E-02 ,
    4.908E+01,
    1.065E+02
])

#can we get specified ag machinery impact data? - harvester, shaker, sweeper
unspecified_ag_machinery_impact_dict = np.array([
    5.762E-07 ,
    4.170E+00,
    1.988E-01 ,
    1.742E-02 ,
    2.191E-02 ,
    9.968E-07 ,
    2.005E-06 ,
    5.027E-03,
    5.345E+01,
    3.842E+00
])

urea_impact_dict = np.array([
    1.094E-06 ,
    4.453E+00,
    1.185E-01 ,
    3.133E-02 ,
    1.033E-02 ,
    1.035E-07 ,
    7.578E-07 ,
    4.547E-03,
    2.749E+01,
    1.023E+01
])

