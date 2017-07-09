import cmath
import math
def roots(a,b,c):
    d=b**2-4*a*c
    str=[]
    str.append((-b-cmath.sqrt(d))/(2*a))
    str.append((-b+cmath.sqrt(d))/(2*a))
    return str                               
print(roots(1,2,1))
