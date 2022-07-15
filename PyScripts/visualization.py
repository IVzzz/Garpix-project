import logging
import numpy as np
from myplot import plot_verticles
import pymesh


from PyScripts.box import Box

box = Box(1, 2, 3, 4, 5, 6)
box.setPosition(5, 5, 5)

plot_verticles(vertices = box.getVertices(), isosurf = False)
