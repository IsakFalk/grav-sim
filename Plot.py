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
        #filling up the lists with the position of the planet(s)
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
        
        #set screen limits
        ylim(-8, 8)
        xlim(-8, 8)  

        show()
      
    #a plot where we can see the planet moving in real time, dots regulates if it leaves a trail of dots or not            
    def dynamic_plot(self, up, p1, dots = True):
        #initiating a copy of the given planet and a scatter of the sun
        p = Planet.Planet(p1.x, p1.y, p1.vx, p1.vy)
        
        #Set sun object with corresponding colour in hex
        scatter(0.0, 0.0, 400, '#FFFF30')
    
        #set axes
        ylim(-8, 8)
        xlim(-8, 8)

        #show begins the window, if, else to catch the case with the dots. Each of these plots the coordinate of the planet, adds it to the plot then update the planets position
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
                
    #plots n planets randomly in the third quadrant of the coordinate system
    def plotn(self, n, up, dots = False):
    
        scatter(0.0, 0.0, 400, '#FFFF30')

        ylim(-8, 8)
        xlim(-8, 8)
        
        planets = []
        s_list = []
        
        #fill out the planet list
        for i in range(0, n):
            x = uniform(0., 8.)
            y = uniform(-8.0, 0.)
            vx = uniform(0., 1.)
            vy = uniform(0., 1.)
            planets.append(Planet.Planet(x, y, vx, vy))
        
        #Essentially the same working as plot_dynamic but handle n planets instead of 1.    
        show(block = False)
        k = 0
        while True:
            for i in range(len(planets)):
                if k == 0:
                    s_list.append(scatter(planets[i].x, planets[i].y, 10))
                    if i == len(planets) - 1:
                        k = 1
                else:
                    s_list[i] = scatter(planets[i].x, planets[i].y, 10)
              
            draw()
            
            for i in range(len(planets)):
                if dots == False:
                    s_list[i].set_visible(False)
                up.update(planets[i])

if __name__ == "__main__":
    p1 = Planet.Planet(5., -3., 0.55, 0.4)
    leap = Leapfrog.Leapfrog(5., 0.7, 0.2)
    up = Update.Update(leap)
    
    plotn(10, up, dots = False)
    
