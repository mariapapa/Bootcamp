import math
a= input ("Enter first side of the triangle")
b= input ("Enter second side of the triangle")
c= input ("Enter third side of the triangle")
a= int (a)
b= int (b)
c= int (c)
r= (1/4) *math.sqrt((a+b+c)*(-a+b+c)*(a-b+c)*(a+b-c))
print ("The area of the triangle is r", r)
