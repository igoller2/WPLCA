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

bale_loading_impact_dict = {
    "OzDep":6.559E-08,
    "GWP":2.847E-01,
    "Smog":8.353E-02 ,
    "Acid":2.643E-03 ,
    "Eut":2.446E-04 ,
    "Cancer":1.818E-10 ,
    "NonCancer":6.226E-07 ,
    "Resp":3.703E-04 ,
    "EcoTox":3.377E-01,
    "Fuel":5.796E-01
}

baling_impact_dict = {
    "OzDep":6.669E-07 ,
    "GWP":5.153E+00,
    "Smog":9.092E-01,
    "Acid":3.504E-02 ,
    "Eut":8.705E-03 ,
    "Cancer":8.258E-08 ,
    "NonCancer":4.533E-06 ,
    "Resp":5.034E-03 ,
    "EcoTox":9.355E+00,
    "Fuel":1.622E+01
}

diesel_impact_dict = {
    "OzDep":1.836E-06 ,
    "GWP":1.123E+00,
    "Smog":9.052E-02 ,
    "Acid":1.045E-02 ,
    "Eut":3.858E-03 ,
    "Cancer":2.912E-08 ,
    "NonCancer":1.216E-07 ,
    "Resp":9.083E-04 ,
    "EcoTox":2.938E+00,
    "Fuel":1.626E+01
}

#is this supposed to have a negative non-cancer impact?
grass_seed_impact_dict = {
    "OzDep":2.144E-07 ,
    "GWP":2.481E+00,
    "Smog":1.759E-01 ,
    "Acid":1.757E-02 ,
    "Eut":2.788E-02 ,
    "Cancer":1.323E-07 ,
    "NonCancer":-2.205E-08 ,
    "Resp":1.712E-03 ,
    "EcoTox":1.495E+01,
    "Fuel":2.142E+00
}

haying_impact_dict = {
    "OzDep":1.553E-06 ,
    "GWP":6.710E+00,
    "Smog":2.185E+00 ,
    "Acid":6.844E-02 ,
    "Eut":6.163E-03 ,
    "Cancer":4.320E-09 ,
    "NonCancer":1.695E-05 ,
    "Resp":8.276E-03 ,
    "EcoTox":9.068E+00,
    "Fuel":1.372E+01
}

tree_harvesting_impact_dict = {
    "OzDep": 1.203E-05,
    "GWP":4.942E+01,
    "Smog":5.167E+00 ,
    "Acid":1.996E-01 ,
    "Eut":4.526E-02 ,
    "Cancer":8.810E-08 ,
    "NonCancer":1.397E-06 ,
    "Resp":1.768E-02 ,
    "EcoTox":4.908E+01,
    "Fuel":1.065E+02
}

mowing_impact_dict = {
    "OzDep":4.407E-06 ,
    "GWP":2.542E+01,
    "Smog":4.796E+00 ,
    "Acid":1.914E-01 ,
    "Eut":6.016E-02 ,
    "Cancer":1.660E-06 ,
    "NonCancer":3.283E-05 ,
    "Resp":3.446E-02 ,
    "EcoTox":1.496E+02,
    "Fuel":3.978E+01
}

N_fertilizer_impact_dict = {
    "OzDep":8.993E-07 ,
    "GWP":3.376E+00,
    "Smog":2.283E-01 ,
    "Acid":4.142E-02 ,
    "Eut":2.576E-02 ,
    "Cancer":3.028E-07 ,
    "NonCancer":1.879E-06 ,
    "Resp":5.440E-03 ,
    "EcoTox":5.411E+01,
    "Fuel":8.552E+00
}

pesticide_application_impact_dict = {
    "OzDep":2.006E-06 ,
    "GWP":1.232E+01,
    "Smog":2.323E+00 ,
    "Acid":9.647E-02 ,
    "Eut":3.477E-02 ,
    "Cancer":9.502E-07 ,
    "NonCancer":2.346E-05 ,
    "Resp":1.233E-02 ,
    "EcoTox":9.496E+01,
    "Fuel":1.825E+01
}

pesticide_impact_dict = {
    "OzDep":1.971E-05 ,
    "GWP":1.025E+01,
    "Smog":7.618E-01 ,
    "Acid":9.612E-02 ,
    "Eut":8.088E-02 ,
    "Cancer":5.017E-07 ,
    "NonCancer":3.347E-06 ,
    "Resp":8.948E-03,
    "EcoTox":1.468E+02,
    "Fuel":1.906E+01
}

petrol_impact_dict = {
    "OzDep":1.769E-06 ,
    "GWP":1.360E+00,
    "Smog":9.778E-02 ,
    "Acid":1.124E-02,
    "Eut":4.008E-03 ,
    "Cancer":3.217E-08 ,
    "NonCancer":1.480E-07 ,
    "Resp":9.883E-04,
    "EcoTox":3.728E+00,
    "Fuel":1.619E+01
}

phosphate_fertilizer_impact_dict= {
    "OzDep":4.582E-07 ,
    "GWP":1.720E+00,
    "Smog":1.163E-01 ,
    "Acid":2.110E-02 ,
    "Eut":1.312E-02 ,
    "Cancer":1.543E-07 ,
    "NonCancer":9.571E-07,
    "Resp":2.772E-03,
    "EcoTox":2.757E+01,
    "Fuel":4.357E+00
}

potassium_chloride_fertilizer_impact_dict= {
    "OzDep":6.377E-08 ,
    "GWP":4.561E-01,
    "Smog":2.487E-02 ,
    "Acid":2.331E-03 ,
    "Eut":1.593E-03 ,
    "Cancer":3.693E-08,
    "NonCancer":2.534E-07,
    "Resp":2.809E-04,
    "EcoTox":9.452E+00,
    "Fuel":9.886E-01
}

tillage_impact_dict = {
    "OzDep":2.395E-05 ,
    "GWP":1.216E+02,
    "Smog":2.791E+01 ,
    "Acid":1.002E+00,
    "Eut":2.189E-01 ,
    "Cancer":5.113E-06 ,
    "NonCancer":1.028E-04 ,
    "Resp":1.873E-01,
    "EcoTox":4.691E+02,
    "Fuel":2.140E+02
}

#can we get specified ag machinery impact data? - harvester, shaker, sweeper
unspecified_ag_machinery_impact_dict = {
    "OzDep":5.762E-07 ,
    "GWP":4.170E+00,
    "Smog":1.988E-01 ,
    "Acid":1.742E-02 ,
    "Eut":2.191E-02 ,
    "Cancer":9.968E-07 ,
    "NonCancer":2.005E-06 ,
    "Resp":5.027E-03,
    "EcoTox":5.345E+01,
    "Fuel":3.842E+00
}

urea_impact_dict = {
    "OzDep":1.094E-06 ,
    "GWP":4.453E+00,
    "Smog":1.185E-01 ,
    "Acid":3.133E-02 ,
    "Eut":1.033E-02 ,
    "Cancer":1.035E-07 ,
    "NonCancer":7.578E-07 ,
    "Resp":4.547E-03,
    "EcoTox":2.749E+01,
    "Fuel":1.023E+01
}