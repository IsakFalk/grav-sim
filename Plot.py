#the plot class
import random
import numpy as np
from pylab import *
import Planet
import Update
import Leapfrog

class Plot(object):

    def __init__(self):
        pass
        
    #n: number of times the leapfrog will iterate. up: an object of the update class (with a Leapfrog called). p1: a planet object
    #n recommended to be quite large, the smaller h is the larger n needs to be to see an orbit
    def static_plot(self, n, up, p1):
        
        #Make a new planet with the same values as the one from the input as we don't want to change any of the values of the actual planet
        p = Planet.Planet(p1.x, p1.y, p1.vx, p1.vy)
        
        #the two lists which we fill out with x and y of the planet
        l1 = []
        l2 = []
    
        for i in range(0, n):
            if ((p.x**2 + p.y**2)**0.5 < 0.2):
                break
            l1.append(p.x)
            l2.append(p.y)
            up.update(p)
        
        #Making numpy arrays
        X = np.array([l1])
        Y = np.array([l2])
        
        #plotting
        scatter(X, Y, 10)
        scatter(0.0, 0.0, 400, '#FFFF30')
        
        ylim(-8, 8)
        xlim(-8, 8)  

        show()
      
                
    def dynamic_plot(self, up, p1, dots = True):
    
        p = Planet.Planet(p1.x, p1.y, p1.vx, p1.vy)

        scatter(0.0, 0.0, 400, '#FFFF30')

        ylim(-8, 8)
        xlim(-8, 8)

        show(block = False)
        if dots:   
            while True:
                if ((p.x**2 + p.y**2)**0.5 < 0.4):
                    break
                scatter(p.x, p.y, 10)
                draw()
                up.update(p)
                
        else:
            while True:
                if ((p.x**2 + p.y**2)**0.5 < 0.2):
                    break
                s1 = scatter(p.x, p.y, 10)
                draw()
                s1.remove()
                up.update(p)
                
    def plotn(self, n, up):
    
        scatter(0.0, 0.0, 400, '#FFFF30')

        ylim(-8, 8)
        xlim(-8, 8)

        show(block = False)
        
        planets = []
        
        for i in range(0, n):
            x = random.uniform(-8, 8)
            y = random.uniform(-8, 8)
            vx = random.uniform(-1.5, 1.5)
            vy = random.uniform(-1.5, 1.5)
            planets.append(Planet.Planet(x, y, vx, vy))
            
