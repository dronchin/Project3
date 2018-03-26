from OOP.PlanetSystem_VV import solarsystem, planet
import numpy as np

n = 500
tf = 100
ti = 0
h = 0.01

Earth_mass = 0.0001
Sun_mass = 1
Jupiter_mass = 0.001

Earth_posx = 1.0
Earth_posy = 0
Jupiter_posx = 2
Jupiter_posy = 0
Sun_posx = 0
Sun_posy = 0

Earth_velx = 0
Earth_vely = np.pi*2
Jupiter_velx = 0
Jupiter_vely = np.pi*2/np.sqrt(2)
planetlist = [[0,0,0,0,1, "sun"],
             [Earth_posx,Earth_posy,Earth_velx,Earth_vely, Earth_mass, "earth"],
             [Jupiter_posx,Jupiter_posy,Jupiter_velx,Jupiter_vely, Jupiter_mass, "jupiter"]]

Model = solarsystem(h, n, planetlist)

Model.run()
Model.displaypaths()

Model.showConservation()
