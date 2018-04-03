from OOP.PlanetSystem_VV import solarsystem, planet
import numpy as np

Earth_mass = 6.0E24/2.0E30
Jupiter_mass = 1.9E27/2.0E30
Mars_mass = 6.6E23/2.0E30
Venus_mass = 4.9E24/2.0E30
Saturn_mass = 5.5E26/2.0E30
Mercury_mass = 3.3E23/2.0E30
Uranus_mass = 8.8E25/2.0E30
Neptune_mass = 1.03E26/2.0E30
Pluto_mass = 1.31E22/2.0E30

#data taken from HORIZONS web interface program
masterplanetlist = [[1.306159282417647E-03,6.513468272378295E-03,-6.395720460933692E-06*365.242,4.453045697891337E-06*365.242,1, "sun"],
    [-9.946414304930705E-01,-2.932158320553592E-02,3.391477521295081E-04*365.242,-1.725555172164105E-02*365.242, Earth_mass, "earth"],
    [-3.862930711302167E+00,-3.790635360952593E+00, 5.195720281733852E-03*365.242,-5.028017251762835E-03*365.242, Jupiter_mass, "jupiter"],
    [-9.369424526925297E-01,-1.219977161192441E+00, 1.163437286258813E-02*365.242,-7.300031899775550E-03*365.242, Mars_mass, "mars"],
    [5.191693262879332E-01,5.105990652325588E-01, -1.417705639210480E-02*365.242, 1.441171715692769E-02*365.242, Venus_mass, "venus"],
    [4.747680212109861E-01,-1.004672756913739E+01, 5.265240358666952E-03*365.242, 2.453328284802944E-04*365.242, Saturn_mass, "saturn"],
    [-2.998949742334473E-01,1.785453996219961E-01, -1.973106624063550E-02*365.242,-2.324417603639305E-02*365.242, Mercury_mass, "mercury"],
    [1.757372841696595E+01,9.330671445594209E+00, -1.873384253877698E-03*365.242, 3.290521747756050E-03*365.242, Uranus_mass, "uranus"],
    [2.875186018417908E+01,-8.346262862932090E+00, 8.545835965514583E-04*365.242,3.033739601934005E-03*365.242, Neptune_mass, "neptune"],
    [1.102415247442523E+01,-3.165695356906997E+01, 3.041176499071855E-03*365.242, 3.772251131115861E-04*365.242, Pluto_mass, "pluto"]
    ]

#need 
h = 0.01
n = 1000
fullModel = solarsystem(h, n, masterplanetlist)


fullModel.run()
fullModel.displaypaths()

kenergies, penergies, AngMoments = fullModel.showConservation(True)

x = fullModel.planets[1].x
y = fullModel.planets[1].y
x_actual = -9.973731440204546E-01
y_actual = -2.391306583344388E-02
print("final x ", x, "x_actual", x_actual)
print("final y ", y, "y_actual", y_actual)
print("percent error of x", np.abs((x-x_actual)/x_actual)*100)
print("percent error of y", np.abs((y-y_actual)/y_actual)*100)
