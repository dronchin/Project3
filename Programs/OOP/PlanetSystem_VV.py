import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display,clear_output

class planet():
    def __init__(self, posx, posy, velx, vely, mass, name):
        self.x = posx
        self.y = posy
        self.vx = velx
        self.vy = vely
        self.mass = mass
        self.id = name
        self.xpos = []
        self.ypos = []

    def distance(self, otherplanet):
        return np.sqrt((otherplanet.x-self.x)**2 + (otherplanet.y-self.y)**2)
    def kineticEnergy(self):
        return 0.5*self.mass*(self.vx**2+self.vy**2)
    def potentialEnergy(self, sun):
        return -4.0*np.pi**2*self.mass/(2*self.distance(sun))
    def angularMomentum(self, sun):
        return self.mass*self.distance(sun)*np.sqrt(self.vx**2+self.vy**2)


class solarsystem():
    def __init__(self, h, N, planetlist):
        self.h = h
        self.N = N
        self.planets = []
        for i in planetlist:
            a = planet(i[0], i[1], i[2], i[3], i[4], i[5])
            self.planets.append(a)

    def Accel(self, CURplanet):
        accelx = 0
        accely = 0
        for other in self.planets:
            r = CURplanet.distance(other)
            if r != 0:
                accelx += -4*np.pi**2*(CURplanet.x - other.x)/(r**3)*other.mass
                accely += -4*np.pi**2*(CURplanet.y - other.y)/(r**3)*other.mass
        return accelx, accely

    def VV(self, CURplanet):
        ax, ay = self.Accel(CURplanet)

        CURplanet.x = CURplanet.x + self.h*CURplanet.vx + (self.h**2/2)*ax
        CURplanet.y = CURplanet.y + self.h*CURplanet.vy + (self.h**2/2)*ay

        ax_new, ay_new = self.Accel(CURplanet)

        CURplanet.vx = CURplanet.vx + self.h/2*(ax + ax_new)
        CURplanet.vy = CURplanet.vy + self.h/2*(ay + ay_new)

    def step(self):
        for CURplanet in self.planets:
            self.VV(CURplanet)
            CURplanet.xpos.append(CURplanet.x)
            CURplanet.ypos.append(CURplanet.y)

    def run(self):
        for i in range(self.N):
            self.step()

    def displaypaths(self):
        for CURplanet in self.planets:
            plt.plot(CURplanet.xpos,CURplanet.ypos, label=CURplanet.id)
        plt.title("Planet Paths after {} steps".format(self.N))
        plt.legend()
        plt.axis('equal')
        plt.show()

    def showConservation(self):
        kenergies = []
        penergies = []
        AngMoments = []
        for i in range(self.N):
            #increments through system steps
            self.step()

            #saves variables from the system from each step
            kenergystep = []
            penergystep = []
            AngMomentstep = []
            for CURplanet in self.planets:
                kenergy = CURplanet.kineticEnergy()
                if CURplanet.id != "sun":
                    penergy = CURplanet.potentialEnergy(self.planets[0]) #assumes the sun is always the first planet
                    penergystep.append(penergy)
                    AngMoment = CURplanet.angularMomentum(self.planets[0]) #assumes the sun is always the first planet
                    AngMomentstep.append(AngMoment)
                kenergystep.append(kenergy)
            kenergies.append(kenergystep)
            penergies.append(penergystep)
            AngMoments.append(AngMomentstep)

        kenergies = np.asarray(kenergies)
        penergies = np.asarray(penergies)
        AngMoments = np.asarray(AngMoments)
        for i in range(len(self.planets)):
            plt.plot(range(self.N), kenergies[:,i], label=self.planets[i].id)
        plt.legend()
        plt.title("Kinetic Energy of the system over steps")
        plt.show()

        for i in range(1,len(self.planets)):
            plt.plot(range(self.N), penergies[:,i-1], label=self.planets[i].id)
        plt.legend()
        plt.title("Potential Energy of the system over steps")
        plt.show()

        for i in range(1,len(self.planets)):
            plt.plot(range(self.N), AngMoments[:,i-1], label=self.planets[i].id)
        plt.legend()
        plt.title("Angular Momentum of the system over steps")
        plt.show()
