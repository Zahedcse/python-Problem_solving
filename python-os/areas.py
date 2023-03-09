
import math
def triangle(base, height):
  return base*height/2

def rectangle(base, height):
  return base*height

def circle(radious):
  return math.pi*(radious**2)

def donut(outside_radious,inside_radious ):
    return circle(outside_radious) - circle(outside_radious)
