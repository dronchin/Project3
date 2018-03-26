from OOP.PlanetSystem_VV import planet, solarsystem

class solarsystem(solarsystem):
    '''Inherits all methods from the solarsystem class in PlanetSystem_VV but
    changes steps to use the new Euler method'''
    def Euler(self, CURplanet):
        ax, ay = self.Accel(CURplanet)
        CURplanet.x = CURplanet.x + CURplanet.vx*self.h
        CURplanet.y = CURplanet.y + CURplanet.vy*self.h
        CURplanet.vx = CURplanet.vx + ax*self.h
        CURplanet.vy = CURplanet.vy + ay*self.h
        CURplanet.xpos.append(CURplanet.x)
        CURplanet.ypos.append(CURplanet.y)

    def step(self):
        for CURplanet in self.planets:
            self.Euler(CURplanet)
            CURplanet.xpos.append(CURplanet.x)
            CURplanet.ypos.append(CURplanet.y)
