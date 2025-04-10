import math
def Cartesian(r, phi, theta):
  return [
    r * math.cos(phi) * math.sin(theta),
    r * math.sin(phi) * math.sin(theta),
    r * math.cos(theta)
  ]
def Cartesian():
  Length = 1; 
  r = Length
  vertices = [
    super.Red(0,0,1),  
    super.Blue(math.arccos(-1/3), 0, 0), 
    super.Green(0, -math.arccos(-1/3),0), 
    super.white(0,0,math.arccos(-1/3)), 
  ]
  
