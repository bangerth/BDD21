import numpy as np

"""
Dictionaries of data used in Fluidity_Optimize_Parallel_Example.py
Author: Patrick Ball.
"""

#------------------
# Source Compositions
#------------------

# Primitive Mantle Sources (PM)

# McDonough and Sun, 1995, Chem. Geol., Vol. 120.

PM_MS_1995 = {
    "La" : 0.648,
    "Ce" : 1.675,
    "Pr" : 0.254,
    "Nd" : 1.25,
    "Sm" : 0.406,
    "Eu" : 0.154,
    "Gd" : 0.544,
    "Tb" : 0.099,
    "Dy" : 0.674,
    "Ho" : 0.149,
    "Er" : 0.438,
    "Tm" : 0.068,
    "Yb" : 0.441,
    "Lu" : 0.0675,
    "Hf" : 0.283,
    "Rb" : 0.6,
    "Sr" : 19.9,
    "Th" : 0.0795,
    "U" : 0.0203,
    "Pb" : 0.15,
    "Nb" : 0.658,
    "Ti" : 1205.,
    "Zr" : 10.5,
    "Y" : 4.3,
    "Ta" : 0.037,
    "Li" : 1.6,
    "Sc" : 16.2,
    "V" : 82.,
    "Cr" : 2625.,
    "Ni" : 1960.,
    "Na" : 2670.,
    "K" : 240.,
    "Mn" : 1045.,
    "P" : 90.,
    "Co" : 105., 
    "Ba" : 6.6,
    "Ga" : 4.,
    "Cu" : 30., 
    "Zn" : 55.,
    "Cs" : 0.021
}

# McKenzie and O'Nions, 1995, J. Pet., Vol. 36.
# Combo of Mckenzie and O'Nions, 1991, 1995 and Hart and Zindler.

PM_MO_1995 = {
    "La" : 0.55,
    "Ce" : 1.4,
    "Pr" : 0.22,
    "Nd" : 1.08,
    "Sm" : 0.35,
    "Eu" : 0.13,
    "Gd" : 0.457,
    "Tb" : 0.084,
    "Dy" : 0.57,
    "Ho" : 0.13,
    "Er" : 0.372,
    "Tm" : 0.057,
    "Yb" : 0.372,
    "Lu" : 0.057,
    "Hf" : 0.25,
    "Rb" : 0.62,
    "Sr" : 20.,
    "Th" : 0.07,
    "U" : 0.018,
    "Pb" : 0.155,
    "Nb" : 0.54,
    "Ti" : 1020.,
    "Zr" : 8.51,
    "Y" : 3.45,
    "Ta" : 0.031,
    "Li" : 2.7,
    "Sc" : 12.,
    "V" : 103.,
    "Cr" : 3000.,
    "Ni" : 2000.,
    "Na" : 1800.,
    "K" : 200.,
    "Mn" : 1000.,
    "P" : 61.,
    "Co" : 105.,
    "Ba" : 6.5,
    "Ga" : 3.7,
    "Cu" : 40.,
    "Zn" : 68.,
    "Cs" : 0.01,
    "Ra" : (6.38 * 10**-9)
}

#------------------

# Depleted Mantle Sources (DM)

# McKenzie and O'Nions, 1995, J. Pet., Vol. 36.
# Referred to in original INVMEL code as NORM=6.
# Generated by assuming the continents were extracted from 40% of the mantle.
# Th reduced from 0.007 to 0.00464 so that Th/U = 2.58
# Rb reduced from 0.062 to 0.048 so that K/Rb = 420.
# Cs reduced from 0.001 to 0.00062 so that K/Cs = 32000.

DM_MO_1995 = {
    "La" : 0.206,
    "Ce" : 0.722,
    "Pr" : 0.143,
    "Nd" : 0.815,
    "Sm" : 0.299,
    "Eu" : 0.115,
    "Gd" : 0.419,
    "Tb" : 0.077,
    "Dy" : 0.525,
    "Ho" : 0.12,
    "Er" : 0.347,
    "Tm" : 0.054,
    "Yb" : 0.347,
    "Lu" : 0.057,
    "Hf" : 0.22,
    "Rb" : 0.048,
    "Sr" : 14.7,
    "Th" : 0.00464,
    "U" : 0.0018,
    "Pb" : 0.016,
    "Nb" : 0.39,
    "Ti" : 1020.,
    "Zr" : 7.19,
    "Y" : 3.18,
    "Ta" : 0.018,
    "Li" : 2.2,
    "Sc" : 12.,
    "V" : 100.,
    "Cr" : 3000.,
    "Ni" : 2000.,
    "Na" : 1550.,
    "K" : 20.,
    "Mn" : 1000.,
    "P" : 51.,
    "Co" : 105.,
    "Ba" : 0.65,
    "Ga" : 3.5,
    "Cu" : 40.,
    "Zn" : 68.,
    "Cs" : 0.00062,
    "Ra" : (6.38 * 10**-10)
}

# Salters and Stracke, 2004, G-Cubed, Vol. 5.

DM_SS_2004 = {
    "La" : 0.234,
    "Ce" : 0.772,
    "Pr" : 0.131,
    "Nd" : 0.713,
    "Sm" : 0.27,
    "Eu" : 0.107,
    "Gd" : 0.395,
    "Tb" : 0.075,
    "Dy" : 0.531,
    "Ho" : 0.122,
    "Er" : 0.371,
    "Tm" : 0.06,
    "Yb" : 0.401,
    "Lu" : 0.063,
    "Hf" : 0.199,
    "Rb" : 0.088,
    "Sr" : 9.8,
    "Th" : 0.0137,
    "U" : 0.0047,
    "Pb" : 0.0232,
    "Nb" : 0.21,
    "Ti" : 798.,
    "Zr" : 7.94,
    "Y" : 4.07,
    "Ta" : 0.0138,
    "Li" : 0.7,
    "Sc" : 16.3,
    "V" : 79.,
    "Cr" : 2500.,
    "Ni" : 1960.,
    "Na" : 2151.4,
    "K" : 60.,
    "Mn" : 1045.,
    "P" : 40.7,
    "Co" : 106.,
    "Ba" : 1.2,
    "Ga" : 3.2,
    "Cu" : 30.,
    "Zn" : 56.,
    "Cs" : 0.00132
}

#------------------
# Partition Coefficients
#------------------

# Listed in order: ol, opx, cpx, plg, spl, gnt.

# Partition Coefficients from McKenzie and O'Nions, 1995, JPet, Vol. 36.

D_MO_1995 = {}
D_MO_1995["La"] = np.array([0.0004, 0.002, 0.054, 0.27, 0.01, 0.01])
D_MO_1995["Ce"] = np.array([0.0005, 0.003, 0.098, 0.2, 0.01, 0.021])
D_MO_1995["Pr"] = np.array([0.0008, 0.0048, 0.15, 0.17, 0.01, 0.054])
D_MO_1995["Nd"] = np.array([0.001, 0.0068, 0.21, 0.14, 0.01, 0.087])
D_MO_1995["Sm"] = np.array([0.0013, 0.01, 0.26, 0.11, 0.01, 0.217])
D_MO_1995["Eu"] = np.array([0.0016, 0.013, 0.31, 0.73, 0.01, 0.32])
D_MO_1995["Gd"] = np.array([0.0015, 0.016, 0.3, 0.066, 0.01, 0.498])
D_MO_1995["Tb"] = np.array([0.0015, 0.019, 0.31, 0.06, 0.01, 0.75])
D_MO_1995["Dy"] = np.array([0.0017, 0.022, 0.33, 0.055, 0.01, 1.06])
D_MO_1995["Ho"] = np.array([0.0016, 0.026, 0.31, 0.048, 0.01, 1.53])
D_MO_1995["Er"] = np.array([0.0015, 0.03, 0.3, 0.041, 0.01, 2.])
D_MO_1995["Tm"] = np.array([0.0015, 0.04, 0.29, 0.036, 0.01, 3.])
D_MO_1995["Yb"] = np.array([0.0015, 0.049, 0.28, 0.031, 0.01, 4.03])
D_MO_1995["Lu"] = np.array([0.0015, 0.06, 0.28, 0.025, 0.01, 5.5])
D_MO_1995["Hf"] = np.array([0.01, 0.01, 0.22, 0.01, 0., 0.44])
D_MO_1995["Rb"] = np.array([0.00018, 0.0006, 0.001, 0.03, 0.0001, 0.0007])
D_MO_1995["Sr"] = np.array([0.00019, 0.007, 0.13, 2., 0., 0.0011])
D_MO_1995["Th"] = np.array([0.0001, 0.0001, 0.00026, 0.05, 0., 0.0001])
D_MO_1995["U"] = np.array([0.0001, 0.0001, 0.00036, 0.11, 0., 0.0001])
D_MO_1995["Pb"] = np.array([0.0001, 0.0013, 0.01, 0.36, 0., 0.0005])
D_MO_1995["Nb"] = np.array([0.005, 0.005, 0.02, 0.01, 0., 0.07])
D_MO_1995["Ti"] = np.array([0.02, 0.1, 0.18, 0.04, 0.15, 0.28])
D_MO_1995["Zr"] = np.array([0.01, 0.03, 0.1, 0.01, 0., 0.32])
D_MO_1995["Y"] = np.array([0.005, 0.005, 0.2, 0.03, 0., 2.11])
D_MO_1995["Ta"] = np.array([0.005, 0.005, 0.02, 0., 0., 0.04])
D_MO_1995["Li"] = np.array([0., 0., 0.59, 0., 0., 0.])
D_MO_1995["Sc"] = np.array([0.16, 0.33, 0.51, 0.02, 0., 2.27])
D_MO_1995["V"] = np.array([0.06, 0.9, 1.31, 0., 0., 1.57])
D_MO_1995["Cr"] = np.array([0.3, 1.5, 3., 0.05, 300., 5.5])
D_MO_1995["Ni"] = np.array([9.4, 9.4, 9.4, 0., 0., 0.])
D_MO_1995["Na"] = np.array([0.00001, 0.05, np.nan, 0.39, 0., 0.04])
D_MO_1995["K"] = np.array([0.00018, 0.001, 0.002, 0.18, 0.0001, 0.001])
D_MO_1995["Mn"] = np.array([0.5, 0.7, 0.44, 0.05, 0.25, 2.05])
D_MO_1995["P"] = np.array([0., 0.03, 0.03, 0., 0., 0.1])
D_MO_1995["Co"] = np.array([1., 2., 2., 0.05, 2., 2.])
D_MO_1995["Ba"] = np.array([0.0003, 0.0001, 0.0005, 0.33, 0.0001, 0.0005])
D_MO_1995["Ga"] = np.array([0.04, 0.2, 0.74, 0., 5., 5.])
D_MO_1995["Cu"] = np.array([0., 0., 0.36, 0., 0., 0.])
D_MO_1995["Zn"] = np.array([0., 0., 0., 0., 0., 0.])
D_MO_1995["Cs"] = np.array([0.00005, 0.0001, 0.0002, 0.025, 0.0001, 0.0002])

# Partition Coefficients from Gibson and Geist, 2010, EPSL. Vol. 300

D_GG_2010 = {}
D_GG_2010["La"] = np.array([0.0005, 0.0031, 0.049, 0., 0., 0.001])
D_GG_2010["Ce"] = np.array([0.0005, 0.004, 0.08, 0., 0., 0.005])
D_GG_2010["Pr"] = np.array([0.0008, 0.0048, 0.126, 0., 0., 0.14])
D_GG_2010["Nd"] = np.array([0.00042, 0.012, 0.178, 0., 0., 0.052])
D_GG_2010["Sm"] = np.array([0.0011, 0.02, 0.293, 0., 0., 0.25])
D_GG_2010["Eu"] = np.array([0.0016, 0.013, 0.335, 0., 0., 0.496])
D_GG_2010["Gd"] = np.array([0.0011, 0.0065, 0.35, 0., 0., 0.848])
D_GG_2010["Tb"] = np.array([0.0015, 0.019, 0.403, 0., 0., 1.477])
D_GG_2010["Dy"] = np.array([0.0027, 0.011, 0.4, 0., 0., 2.2])
D_GG_2010["Ho"] = np.array([0.0016, 0.026, 0.427, 0., 0., 3.315])
D_GG_2010["Er"] = np.array([0.013, 0.045, 0.42, 0., 0., 4.4])
D_GG_2010["Tm"] = np.array([0.0015, 0.04, 0.40968, 0., 0., 5.495])
D_GG_2010["Yb"] = np.array([0.02, 0.08, 0.4, 0., 0., 6.6])
D_GG_2010["Lu"] = np.array([0.02, 0.12, 0.376, 0., 0., 7.1])
D_GG_2010["Hf"] = np.array([0.0022, 0.03, 0.284, 0., 0., 0.4])
D_GG_2010["Rb"] = np.array([0.0003, 0.0002, 0.0004, 0., 0., 0.002])
D_GG_2010["Sr"] = np.array([0.00004, 0.0007, 0.091, 0., 0., 0.0007])
D_GG_2010["Th"] = np.array([0.00005, 0.002, 0.0059, 0., 0., 0.009])
D_GG_2010["U"] = np.array([0.00038, 0.002, 0.0094, 0., 0., 0.028])
D_GG_2010["Pb"] = np.array([0.003, 0.009, 0.012, 0., 0., 0.005])
D_GG_2010["Nb"] = np.array([0.0005, 0.004, 0.015, 0., 0., 0.015])
D_GG_2010["Ti"] = np.array([0.015, 0.086, 0.35, 0., 0., 0.6])
D_GG_2010["Zr"] = np.array([0.0033, 0.013, 0.119, 0., 0., 0.27])
D_GG_2010["Y"] = np.array([0.0099, 0.052, 0.426, 0., 0., 3.1])
D_GG_2010["Ta"] = np.array([0.0005, 0.004, 0.015, 0., 0., 0.015])
D_GG_2010["Sc"] = np.array([0.17, 0.53, 1.19, 0., 0., 3.96])
D_GG_2010["K"] = np.array([0.00002, 0.0001, 0.001, 0., 0., 0.013])
D_GG_2010["Ba"] = np.array([0.000005, 0.000006, 0.0004, 0., 0., 0.00007])
D_GG_2010["Cs"] = np.array([0.00005, 0.000015, 0.002, 0., 0., 0.002])
# All other elements below from McKenzie and O'Nions, 1995
D_GG_2010["Y"] = np.array([0.005, 0.005, 0.2, 0.03, 0., 2.11])
D_GG_2010["Ta"] = np.array([0.005, 0.005, 0.02, 0., 0., 0.04])
D_GG_2010["Li"] = np.array([0., 0., 0.59, 0., 0., 0.])
D_GG_2010["Sc"] = np.array([0.16, 0.33, 0.51, 0.02, 0., 2.27])
D_GG_2010["V"] = np.array([0.06, 0.9, 1.31, 0., 0., 1.57])
D_GG_2010["Cr"] = np.array([0.3, 1.5, 3., 0.05, 300., 5.5])
D_GG_2010["Ni"] = np.array([9.4, 9.4, 9.4, 0., 0., 0.])
D_GG_2010["Na"] = np.array([0.00001, 0.05, np.nan, 0.39, 0., 0.04])
D_GG_2010["K"] = np.array([0.00018, 0.001, 0.002, 0.18, 0.0001, 0.001])
D_GG_2010["Mn"] = np.array([0.5, 0.7, 0.44, 0.05, 0.25, 2.05])
D_GG_2010["P"] = np.array([0., 0.03, 0.03, 0., 0., 0.1])
D_GG_2010["Co"] = np.array([1., 2., 2., 0.05, 2., 2.])
D_GG_2010["Ba"] = np.array([0.0003, 0.0001, 0.0005, 0.33, 0.0001, 0.0005])
D_GG_2010["Ga"] = np.array([0.04, 0.2, 0.74, 0., 5., 5.])
D_GG_2010["Cu"] = np.array([0., 0., 0.36, 0., 0., 0.])
D_GG_2010["Zn"] = np.array([0., 0., 0., 0., 0., 0.])
D_GG_2010["Cs"] = np.array([0.00005, 0.0001, 0.0002, 0.025, 0.0001, 0.0002])

#------------------
# Major Element Compositions of Mineral Phases
#------------------

# Major element proportions of each mineral phase in wt%
# Listed in order: SiO2, TiO2, Al2O3, Cr2O3, FeO, MnO, MgO, CaO, Na2O, K2O, NiO.
# Dict. listed in order 6-8: Molecular Weight, num. cations, num oxygen atoms.
Mag_MO_1995 = {}
Mag_MO_1995["6"] = np.array([60.09, 79.9, 102., 151.99, 71.85, 70.94, 40.30, 56.08, 61.98, 94.2, 74.7])
Mag_MO_1995["7"] =  np.array([1., 1., 2., 2., 1., 1., 1., 1., 2., 2., 1.])
Mag_MO_1995["8"] =  np.array([2., 2., 3., 3., 1., 1., 1., 1., 1., 1., 1.])

#------------------
# Radii in co-ordination number of VI, VIII.
# Shannon Acta. Cryst. 1976
# Radii for REE from Watson and Green 1981, EPSL (1080 oC).
#------------------

Element_Sizes = {}
Element_Sizes["La"] =  np.array([1.032, 1.16])
Element_Sizes["Ce"] =  np.array([1.01, 1.143])
Element_Sizes["Pr"] =  np.array([0.99, 1.126])
Element_Sizes["Nd"] =  np.array([0.983, 1.109])
Element_Sizes["Sm"] =  np.array([0.958, 1.079])
Element_Sizes["Eu"] =  np.array([0.947, 1.066])
Element_Sizes["Gd"] =  np.array([0.938, 1.053])
Element_Sizes["Tb"] =  np.array([0.923, 1.04])
Element_Sizes["Dy"] =  np.array([0.912, 1.027])
Element_Sizes["Ho"] =  np.array([0.901, 1.015])
Element_Sizes["Er"] =  np.array([0.89, 1.004])
Element_Sizes["Tm"] =  np.array([0.88, 0.994])
Element_Sizes["Yb"] =  np.array([0.868, 0.985])
Element_Sizes["Lu"] =  np.array([0.861, 0.977])
Element_Sizes["Hf"] =  np.array([0.71, 0.83])
Element_Sizes["Rb"] =  np.array([1.52, 1.61])
Element_Sizes["Sr"] =  np.array([1.18, 1.26])
Element_Sizes["Zr"] =  np.array([0.72, 0.84])
Element_Sizes["Th"] =  np.array([0.94, 1.05])
Element_Sizes["Pb"] =  np.array([0.775, 0.94])
Element_Sizes["U"] =  np.array([0.89, 0.975])
Element_Sizes["Nb"] =  np.array([0.64, 0.74])
Element_Sizes["Ti"] =  np.array([0.605, 0.74])
Element_Sizes["Y"] =  np.array([0.9, 1.019])
Element_Sizes["Ta"] =  np.array([0.64, 0.74])
Element_Sizes["Sc"] =  np.array([0.745, 0.87])
Element_Sizes["V"] =  np.array([0.355, 0.54])
Element_Sizes["Cr"] =  np.array([0.615, 0.615])
Element_Sizes["Ni"] =  np.array([0.69, 0.69])
Element_Sizes["Na"] =  np.array([1.02, 1.18])
Element_Sizes["K"] =  np.array([1.38, 1.51])
Element_Sizes["Mn"] =  np.array([0.83, 0.96])
Element_Sizes["P"] =  np.array([0.17, 0.38])
Element_Sizes["Co"] =  np.array([0.745, 0.9])
Element_Sizes["Ba"] =  np.array([1.35, 1.42])
Element_Sizes["Ga"] =  np.array([0.62, 0.62])
Element_Sizes["Cs"] =  np.array([1.67, 1.74])
Element_Sizes["Ra"] =  np.array([1.48, 1.48])

#------------------
# Valency
#------------------

Valency = {
    "La" : 3.,
    "Ce" : 3.,
    "Pr" : 3.,
    "Nd" : 3.,
    "Sm" : 3.,
    "Eu" : 3.,
    "Gd" : 3.,
    "Tb" : 3.,
    "Dy" : 3.,
    "Ho" : 3.,
    "Er" : 3.,
    "Tm" : 3.,
    "Yb" : 3.,
    "Lu" : 3.,
    "Hf" : 4.,
    "Rb" : 1.,
    "Sr" : 2.,
    "Zr" : 4.,
    "Th" : 4.,
    "Pb" : 4.,
    "U" : 4.,
    "Nb" : 5.,
    "Ti" : 4.,
    "Y" : 3.,
    "Ta" : 5.,
    "Sc" : 3.,
    "V" : 5.,
    "Cr" : 3.,
    "Ni" : 2.,
    "Na" : 1.,
    "K" : 1.,
    "Fe" : 2.,
    "Mg" : 2.,
    "Ca" : 2.,
    "Mn" : 2.,
    "P" : 5.,
    "Co" : 2.,
    "Ba" : 2.,
    "Ga" : 3.,
    "Cs" : 1.,
    "Ra" : 2.
}