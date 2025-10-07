import math
def Cartesian(r, phi, theta):
  return [
    r * cos(phi) * sin(theta),
    r * sin(phi) * sin(theta),
    r * cos(theta)
  ]
def Cartesian():
  Length = 1; 
  r = Length
  vertices = [
    super.Red(0,0,1),  
    super.Blue(arccos(-1/3), 0, 0), 
    super.Green(0, -arccos(-1/3),0), 
    super.white(0,0,arccos(-1/3)), 
  ]
  

