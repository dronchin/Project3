from OOP.PlanetSystem_Euler import solarsystem, planet
import numpy as np
import matplotlib.pyplot as plt
import time

n = 10000
h = 0.1

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


n_list = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
times_euler = []
for n in n_list:
    #Euler method is still imported
    Model1 = solarsystem(h, n, planetlist)
    start = time.time()
    Model1.run()
    end = time.time()
    total1 = end-start
    times_euler.append(total1)
    print("Eulers method took: ",total1)


#switch to VV method
from OOP.PlanetSystem_VV import solarsystem, planet
times_vv = []
for n in n_list:
    Model2 = solarsystem(h, n, planetlist)
    start = time.time()
    Model2.run()
    end = time.time()
    total2 = end - start
    times_vv.append(total2)
    print("VV method took: ",total2)

plt.plot(n_list, times_euler, label="Euler")
plt.plot(n_list, times_vv, label="Velocity Verlet")
plt.xlabel("number of steps")
plt.ylabel("time (sec)")
plt.title("Eulers method vs Velocity Verlet method timing")
plt.legend()
plt.show()
