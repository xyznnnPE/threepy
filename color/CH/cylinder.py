import sphere
import color.Red
import color.Green
import color.Blue
import color.white
import math
def Cylinder(X,Y,Z):
     CylinderXY = 'Cylinder.X+ Cylinder.Y'
     CylinderYZ = 'Cylinder.Y+ Cylinder.Z'
     CylinderZX = 'Cylinder.Z + Cylinder.X'
     CylinderXYZ = 'Cylinder.X + Cylinder.Y + Cylinder.Z'
     return [CylinderXY,CylinderYZ,CylinderZX,CylinderXYZ]

def CylindetXY():
    element1 = (
     [[0][1][0][1],
      [1][0][1][0],
      [0][0][0][1],
      [0][0][0][0]])
    element2 = (
     [[0][1][0][1],
      [0][0][1][0],
      [0][1][0][1],
      [0][0][0][0]])
    element3 = (
     [[0][1][0][1],
      [0][0][1][0],
      [0][0][0][1],
      [0][0][1][0]])
    element4 = (
     [[0][1][0][1],
      [0][0][1][0],
      [0][0][0][1],
      [1][0][0][0]])
    return [element1,element2,element3,element4]
def CylinderYZ():
    element5 = (
     [[1][0][1][0],
      [0][1][0][0],
      [0][0][1][0],
      [0][0][0][1]])

    element6 = (
     [[1][0][0][0],
      [0][1][0][1],
      [0][0][1][0],
      [0][0][0][1]])

    element7 = (
    [[1][0][0][0],
      [0][1][0][0],
      [0][0][1][0],
      [0][1][0][1]])

    element8 = (
     [[1][0][0][0],
      [0][1][0][0],
      [1][0][1][0],
      [0][0][0][1]])
    return [element5,element6,element7,element8]
def CylinderXZ():
    element9 = (
     [[0][1][0][1],
      [1][0][1][0],
      [0][0][0][1],
      [0][0][0][0]])
 
    element10 = (
    [[0][1][0][1],
      [0][0][1][0],
      [0][1][0][1],
      [0][0][0][0]])

    element11 = (
     [[0][1][0][1],
      [0][0][1][0],
      [0][0][0][1],
      [0][0][1][0]])
 
    element12 = (
     [[0][1][0][1],
      [0][0][1][0],
      [0][0][0][1],
      [1][0][0][0]])
    return[element9, element10, element11, element12]

def CylinderXYZ():
    element13 = (
     [[1][0][1][0],
      [0][0][0][1],
      [1][0][0][0],
      [0][1][0][0]])
 
    element14 = (
     [[0][0][1][0],
      [0][1][0][1],
      [1][0][0][0],
      [0][1][0][0]])
 
    element15 = (
     [[0][0][1][0],
      [0][0][0][1],
      [1][0][1][0],
      [0][1][0][0]])

    element16 = (
     [[0][0][1][0],
      [0][0][0][1],
      [1][0][0][0],
      [0][1][0][1]])

    element17 = (
     [[0][1][0][0],
      [1][0][0][0],
      [0][1][0][0],
      [1][0][1][0]])

    element18 = (
     [[0][0][0][0],
      [1][0][1][0],
      [0][1][0][0],
      [1][0][1][0]])

    element19 = (
     [[0][0][0][0],
      [1][0][0][0],
      [0][1][0][1],
      [0][0][1][0]])

    element20 = (
     [[0][0][0][1],
      [1][0][0][0],
      [0][1][0][0],
      [0][0][1][0]])
