from OOP.PlanetSystem_Euler import solarsystem, planet
import numpy as np
import matplotlib.pyplot as plt

#use 100000 steps to see long term effects
n = 1000
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

Model1 = solarsystem(h, n, planetlist)

Model1.run()
kenergies1, penergies1, AngMoments1 = Model1.showConservation(False)

#changes the class of solarsystem so that it uses the VV method
from OOP.PlanetSystem_VV import solarsystem, planet

Model2 = solarsystem(h, n, planetlist)

Model2.run()

kenergies2, penergies2, AngMoments2 = Model2.showConservation(False)

#plots for both energies and angular momentum for both euler and VV
for i in range(len(planetlist)):
    plt.plot(range(n), kenergies1[:,i], label=planetlist[i][5]+"Euler")
    plt.plot(range(n), kenergies2[:,i], label=planetlist[i][5]+"VV")
plt.legend()
plt.title("Kinetic Energy of the system over {} steps".format(n))
plt.show()

for i in range(1,len(planetlist)):
    plt.plot(range(n), penergies1[:,i-1], label=planetlist[i][5]+"Euler")
    plt.plot(range(n), penergies2[:,i-1], label=planetlist[i][5]+"VV")
plt.legend()
plt.title("Potential Energy of the system over {} steps".format(n))
plt.show()

for i in range(1,len(planetlist)):
    plt.plot(range(n), AngMoments1[:,i-1], label=planetlist[i][5]+"Euler")
    plt.plot(range(n), AngMoments2[:,i-1], label=planetlist[i][5]+"VV")
plt.legend()
plt.title("Potential Energy of the system over {} steps".format(n))
plt.show()
