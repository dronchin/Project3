from OOP.PlanetSystem_VV import solarsystem, planet
import numpy as np

n = 10000
h = 0.01

Earth_mass = 6.0E24/2.0E30
Sun_mass = 1

Earth_posx = 1.0
Earth_posy = 0

Sun_posx = 0
Sun_posy = 0

Earth_velx = 0

velocitys = np.linspace(8.5, 9.5, num=100)

#Grid search over posible velocities
for Earth_vely in velocitys:
    planetlist = [[0,0,0,0,1, "sun"],
                 [Earth_posx,Earth_posy,Earth_velx,Earth_vely, Earth_mass, "earth"]]
    Model = solarsystem(h, n, planetlist)
    Model.run()
    print("ending radius ", np.sqrt(Model.planets[1].x**2+Model.planets[1].y**2), " for a velocity of ", Earth_vely)

    #accepts the velocity as escape velocit if it gets pas 100AU
    if np.sqrt(Model.planets[1].x**2+Model.planets[1].y**2) > 100:
        print("Escape velocity in (AU/day): ", Earth_vely)
        break

Model.displaypaths()
