import color.Red
import color.Green
import color.Blue
import color.white
import math
def SpherePoint(r,theta,fai):
   x = r * cos(theta)
   y = r * sin(theta) * sin(fai)
   z = r * cos(fai)
   T = r * sin(theta)
   return [x,y,z,T]
   
def xyz():
    x = super.Red
    y = super.Green
    z = super.Blue
    T = super.white
    return [x,y,z,T]
   
def SphereRadius(x,y,z):
   SphereRadiusx = sin(x) + cos(y) 
   SphereRadiusy = sin(y) + cos(x) 
   SphereRadiusz = sin(z) + cos(y)
   return [SphereRadiusx,SphereRadiusy,SphereRadiusz]
   
def RGB(self,x,y,z,t):
    x = self.Red
    y = self.Green
    z = self.Red
    t = self.white
print("x,y,z,t")
