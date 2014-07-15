#The Update class
class Update(object):
    
    #Takes a Leapfrog object as an argument
    def __init__(self, leap):
        self.leap = leap

    #updates all the values of the planet
    def update(self, planet):
        planet.x, planet.y = self.leap.update_pos(planet.x, planet.y, planet.vx, planet.vy)
        planet.vx, planet.vy = self.leap.update_vel(planet.x, planet.y, planet.vx, planet.vy)     
