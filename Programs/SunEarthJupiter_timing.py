import numpy as np
import matplotlib.pyplot as plt
from OOP.PlanetSystem_VV import solarsystem, planet
import time

def Euler(x, v, h):
    return x + h*v

def acceleration(x, r, massfac):
    return -4*np.pi**2*x/(r**3)*massfac

def VV(x,y,vx,vy, otherx, othery, othermass):
    r1 = np.sqrt(x**2+y**2)
    r2 = np.sqrt((otherx-x)**2 + (othery-y)**2)
    ax = acceleration(x, r1, 1) + acceleration((x-otherx), r2, othermass)
    ay = acceleration(y, r1, 1) + acceleration((y-othery), r2, othermass)

    x_new = x + h*vx + (h**2/2)*ax
    y_new = y + h*vy + (h**2/2)*ay
    r1_new = np.sqrt(x_new**2+y_new**2)
    r2_new = np.sqrt((otherx-x_new)**2 + (othery-y_new)**2)

#     ax_new = acceleration(x_new, r_new)
    ax_new = acceleration(x_new, r1_new, 1) + acceleration((x_new-otherx), r2_new, othermass)
#     ay_new = acceleration(y_new, r_new)
    ay_new = acceleration(y_new, r1_new, 1) + acceleration((y_new-othery), r2_new, othermass)

    vx_new = vx + h/2*(ax + ax_new)
    vy_new = vy + h/2*(ay + ay_new)

    return x_new, y_new, vx_new, vy_new

n = 500
h = 0.01

Earth_mass = 0.0001
Sun_mass = 1
Jupiter_mass = 0.001

Earth_posx = 1
Earth_posy = 0
Jupiter_posx = 2
Jupiter_posy = 0
Sun_posx = 0
Sun_posy = 0

Earth_velx = 0
Earth_vely = np.pi*2
Jupiter_velx = 0
Jupiter_vely = np.pi*2/np.sqrt(2)

N_list = [500,1000,1500,2000,2500,3000, 3500,4000,4500,5000]

noOOPtimes = []
for N in N_list:
    xEarth = []
    yEarth = []
    xJupiter = []
    yJupiter = []
    start1 = time.time()
    for i in range(N):
        Earth_posx, Earth_posy, Earth_velx, Earth_vely = VV(Earth_posx, Earth_posy, Earth_velx, Earth_vely,
                                                           Jupiter_posx, Jupiter_posy, Jupiter_mass)
        Jupiter_posx, Jupiter_posy, Jupiter_velx, Jupiter_vely = VV(Jupiter_posx, Jupiter_posy, Jupiter_velx, Jupiter_vely,
                                                           Earth_posx, Earth_posy, Earth_mass)
        xEarth.append(Earth_posx)
        yEarth.append(Earth_posy)
        xJupiter.append(Jupiter_posx)
        yJupiter.append(Jupiter_posy)
    end1 = time.time()
    noOOPtime = end1-start1
    noOOPtimes.append(noOOPtime)

planetlist = [[0,0,0,0,1, "sun"],
             [Earth_posx,Earth_posy,Earth_velx,Earth_vely, Earth_mass, "earth"],
             [Jupiter_posx,Jupiter_posy,Jupiter_velx,Jupiter_vely, Jupiter_mass, "jupiter"]]
OOPtimes = []
for N in N_list:
    start2 = time.time()
    Model = solarsystem(h, N, planetlist)
    Model.run()
    end2 = time.time()
    OOPtime = end2 - start2
    OOPtimes.append(OOPtime)



plt.plot(N_list, noOOPtimes, label='no OOP')
plt.plot(N_list, OOPtimes, label='OOP')
plt.xlabel('N number of steps')
plt.ylabel('run time (sec)')
plt.title('Run Time of OOP vs No OOP as a function of N steps')
plt.legend()
plt.show()
