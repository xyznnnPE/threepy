import color.Red
import color.Green
import color.Blue
import color.white
import math
def SpherePoint(r,theta,fai):
   x = r * math.cos(theta)
   y = r * math.sin(theta) * math.sin(fai)
   z = r * math.cos(fai)
   T = r * math.sin(theta)
   return [x,y,z,T]
def xyz():
    x = super.Red
    y = super.Green
    z = super.Blue
    T = super.anti
    return [x,y,z,T]
def SphereRadius(x,y,z):
   SphereRadiusx = math.sin(x) + math.cos(y) 
   SphereRadiusy = math.sin(y) + math.cos(x) 
   SphereRadiusz = math.sin(z) + math.cos(y)
   return [SphereRadiusx,SphereRadiusy,SphereRadiusz]
def RGB(self,x,y,z,t):
    x = self.Red
    y = self.Green
    z = self.Red
    t = self.anti
print("x,y,z,t")
