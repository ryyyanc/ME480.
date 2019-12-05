#!/usr/bin/env python
# coding: utf-8

# In[18]:


r = viewscad.Renderer(openscad_exec='C:\Program Files\OpenSCAD\openscad.exe')
from solid import *
from solid.utils import *
import numpy as np
import this
import viewscad

x= int( input("x - Number of Holes: "))
y= int( input("y - Number of Holes: "))
xx=(x-1)*7.97
yy=(y-1)*7.97

c1 = cylinder(3.69,1)
c2 = translate([xx,yy,0])(c1)
c3 = translate([0,yy,0])(c1)
c4 = translate([xx,0,0])(c1)
b = hull()(c1,c2,c3,c4)     #Base

xi=np.linspace(0,xx,x).tolist()
yi=np.linspace(0,yy,y).tolist()

ct=translate([0,0,1])(cylinder(r=2.35,h=7.76))
#r.render(ct)

cm=0
for x in xi:
    for y in yi:
        cm=cm+translate([x,y,0])(ct)
#r.render(cm)


t = b + cm
r.render(t)


# In[16]:


r = viewscad.Renderer(openscad_exec='C:\Program Files\OpenSCAD\openscad.exe')
from solid import *
from solid.utils import *
import numpy as np
import this
import viewscad

x= int( input("x - Number of Holes: "))
y= int( input("y - Number of Holes: "))
xx=(x-1)*7.97
yy=(y-1)*7.97

c1 = cylinder(3.69,7.76)
c2 = translate([xx,yy,0])(c1)
c3 = translate([0,yy,0])(c1)
c4 = translate([xx,0,0])(c1)
b = hull()(c1,c2,c3,c4)     #Base

xi=np.linspace(0,xx,x).tolist()
yi=np.linspace(0,yy,y).tolist()

cc = cylinder(r=2.4,h=7.76)
cb = cylinder(r=3.1,h=0.8)
c=cc + cb
ct=translate([0,0,6.96])(cylinder(r=3.1,h=0.8))+c
#r.render(ct)

cm=0
for x in xi:
    for y in yi:
        cm=cm+translate([x,y,0])(ct)
#r.render(cm)


t = b - cm
r.render(t)

