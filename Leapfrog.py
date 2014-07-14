#Leapfrog updater
class Leapfrog(object):
    
    #we will give the parameters to all the methods of the class and thus don't have to initialize them in __init__. h is the stepsize, G is the gravitational constant, M is the mass of the sun
    def __init__(self, M, G, h):
        self.h = h
        self.G = G
        self.M = M
        
    #distance function
    def dist(self, x, y):
        return float((x**2 + y**2)**(0.5))
        
    #the acceleration at each position due to the gravitational force (power of 3 due to not using unit vector)
    def grav_acc(self, x, y):
        a = self.G*self.M*(1/self.dist(x, y)**3)
        return a
                
    #update the position of the object according to the gravitational force
    def update_pos(self, x, y, vx, vy):
        new_x = x + vx*self.h - 0.5*self.grav_acc(x,y)*x*self.h**2
        new_y = y + vy*self.h - 0.5*self.grav_acc(x,y)*y*self.h**2
        
        return new_x, new_y
        
    #update the velocity of the object according the the gravitational force
    def update_vel(self, x, y, vx, vy):
        x2, y2 = self.update_pos(x, y, vx, vy)
        new_vx = vx - 0.5*(self.grav_acc(x,y)*x + self.grav_acc(x2, y2)*x2)*self.h
        new_vy = vy - 0.5*(self.grav_acc(x,y)*y + self.grav_acc(x2, y2)*y2)*self.h
        
        return new_vx, new_vy
