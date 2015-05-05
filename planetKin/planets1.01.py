class body:
    def __init__(self, parent, bodyName, x, y, z, mass, Vx, Vy, Vz):
        self.parent = parent
        self.name = bodyName
        self.x = x
        self.y = y
        self.z = z
        self.Vx = Vx
        self.Vy = Vy
        self.Vz = Vz
        self.ax = 0
        self.ay = 0
        self.az = 0

        self.mass = mass

    def getForcesOnBody(self):
        tempxForce = 0.0
        tempyForce = 0.0
        tempzForce = 0.0
        for body in self.parent.bodyList:
            # We don't have any force on ourself.
            if self != body:
                # Catch division by zero errors.
                # It just means we've got two planets at same location on one axis.
                try:
                    tempxForce += self.parent.G * self.mass * body.mass / float(( self.x-body.x )**2)
                    tempyForce += self.parent.G * self.mass * body.mass / float(( self.y-body.y )**2)
                    tempzForce += self.parent.G * self.mass * body.mass / float(( self.z-body.z )**2)
                except ZeroDivisionError:
                    pass
        return [tempxForce, tempyForce, tempzForce]

    def updateAcceleration(self):
        tempForces = self.getForcesOnBody()
        self.ax = tempForces[0] / self.mass
        self.ay = tempForces[1] / self.mass
        self.az = tempForces[2] / self.mass

    def updateVelocity(self, timetep):
        self.Vx += self.ax*timetep
        self.Vy += self.ay*timetep
        self.Vz += self.az*timetep

    def updatePosition(self, timetep):
        self.x += self.Vx*timetep + (1.0/2)*self.ax*timetep**2
        self.y += self.Vy*timetep + (1.0/2)*self.ay*timetep**2
        self.z += self.Vz*timetep + (1.0/2)*self.az*timetep**2

class nBodySimulation:
    def __init__(self):
        self.bodyList = []
        self.G = 6.674*10**-11

    def createBody(self, bodyName, x, y, z, mass, Vx, Vy, Vz):
        self.bodyList.append( body(self, bodyName, x, y, z, mass, Vx, Vy, Vz) )

    def simulation(self, iterations, timestep):
        for iteration in range(0,iterations):
            # Calculate acceleration and forces before changing positions so things don't get wonky.
            for body in self.bodyList:
                body.updateAcceleration()
                body.updateVelocity(timestep)
            # Now we'll calculate all of the new positions.
            for body in self.bodyList:
                body.updatePosition(timestep)


SolarSystem = nBodySimulation()
SolarSystem.createBody(     'sun',     1.0 ,1.0, 1.0 ,1.9801 * (10 **30), 200.0,         200.0,         200.0)
SolarSystem.createBody('Mercury', -32000000.0,  37400000.0,     6010000.0, 3.3022 * (10 ** 23),-48983.0,    -26756.0,   -2.31)
SolarSystem.createBody(  'Venus',   7.0, 7.0, 7.0, 4.8685 * (10 ** 24),10000000.0,         100000.0,         30000.0)
SolarSystem.createBody(  'Earth',   -105 * (10 **9), -106 * (10 ** 9), 5004000.0 ,5.9736 * (10 ** 24),20500.0,    -21507.0, -0.0895)
SolarSystem.createBody(   'Mars',    -219908870.0, 1.720 * (10 ** 10), 1168359373.0, 6.4185 * (10 ** 23),-10383.0,-19470.0,-153.0)
SolarSystem.createBody( 'Jupiter', 160069722 ,-761453163 ,-404840000, 1.8986 * (10 ** 27),12600,         3300,         -297)
SolarSystem.createBody( 'Saturn',  -1.285 * (10 ** 9), 5.326 * (10 ** 8), 41.9 * (10 ** 6), 5.6846 * (10 ** 26),-4206,-8945         ,         323)
SolarSystem.createBody( 'Uranus',  2.947 * (10 ** 9), -5.67 * (10 ** 8), -40.3 * (10 ** 6), 8.6810 * (10 ** 25),1.24 * (10 ** 3),6.37 * (10 ** 3),7.56)
SolarSystem.createBody('Neptune', 3.55 * (10 ** 9), -2.77 * (10 ** 9), -24.9 * (10 ** 6), 10.243 * (10 ** 25),3.31 * (10 ** 3),4.32 * (10 ** 3),-165)
SolarSystem.createBody(  'Pluto',  -47.3 * (10 ** 6),-4.68 * (10 ** 9),5.15 * (10 ** 8), 1.25 *   (10 ** 22),5.53 * (10 ** 3),-1095,-1480)

SolarSystem.simulation(2112, 1)


