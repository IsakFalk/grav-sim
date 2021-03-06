#1:st try script

from random import uniform
import numpy as np
from pylab import *
import Planet
import Update
import Leapfrog

p1 = Planet.Planet(5., -3., 0.55, 0.4)
leap = Leapfrog.Leapfrog(5., 0.7, 0.2)
up = Update.Update(leap)

n = 40

scatter(0.0, 0.0, 400, '#FFFF30')

ylim(-8, 8)
xlim(-8, 8)
        
planets = []
s_list = []
        
for i in range(0, n):
    x = uniform(-8., 8.)
    y = uniform(-8., 8.)
    vx = uniform(-1.5, 1.5)
    vy = uniform(-1.5, 1.5)
    planets.append(Planet.Planet(x, y, vx, vy))
    
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
        s_list[i].set_visible(False)
        up.update(planets[i])
