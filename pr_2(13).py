#13
import math
x=float(17.421)
y=float(10.365*10**(-3))
z=float(0.828*10**5)
s=((y+((x-1)**(1/3)))**(1/4))/((abs(x-y))*(((math.sin(z))**2)+math.tan(z)))
print(s)