
import math
a= input ("Enter a")
b= input ("Enter b")
c= input ("Enter c")
a= int (a)
b= int (b)
c= int (c)
if b**2 - 4*a*c <0 :
    print ("No real-valued solutions exist")
else :
    x1= (-b + math.sqrt(b**2 - 4*a*c))/ (2*a)
    x2= (-b - math.sqrt(b**2 - 4*a*c))/ (2*a)
    print (" x1=", x1, "and x2=", x2)
