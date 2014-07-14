#1:st try script

import numpy as np
from pylab import *
import Planet
import Update
import Leapfrog

p1 = Planet.Planet(5., -3., 0.55, 0.4)
leap = Leapfrog.Leapfrog(5., 0.7, 0.2)
up = Update.Update(leap)

"""l1 = [0.0]
l2 = [0.0]
    
for i in range(0, 40000):
    l1.append(p1.x)
    l2.append(p1.y)
    up.update(p1)
    
X = np.array([l1])
Y = np.array([l2])

scatter(X, Y, 5)
scatter(0.0, 0.0, 400, '#FFFF30')
show()"""
plot = True

scatter(0.0, 0.0, 400, '#FFFF30')

ylim(-10, 10)
xlim(-10, 10)

show(block = False)

planets = [p1]
   
while plot:
    if ((planets[0].x**2 + planets[0].y**2)**0.5 < 0.4):
        plot = False
        
    s1 = scatter(planets[0].x, planets[0].y, 10)
    draw()
    s1.remove()
    up.update(planets[0])

"""s_list = []
        while True:
            k = 0
            for i in range(len(planets)):
                if k == 0:
                    s_list.append(scatter(planets[i].x, planets[i].y, 10))
                    k += 1
                else:
                    s_list[i] = scatter(planets[i].x, planets[i].y, 10)
                
            draw()
            
            for i in range(len(planets)):
                s_list[i].remove()
                up.update(planets[i])"""
    
    
