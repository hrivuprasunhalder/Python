import numpy as np
from matplotlib import pyplot as plt 
from function_value import FunctionCalculator
func="sin(x)"
function=	FunctionCalculator("math."+func)
p=np.linspace(0,6*3.14159265358979323846,1000)     #for smooth graphing np.linspace(start,stop,num)                   
q=np.array([function.evaluate(x) for x in p])
plt.plot(p,q,"m-")#[color:b,g,r,c,m,y,k,w][line style:-,.,--][marker:o,s,^,d,x]
plt.title(f" y={func}")
plt.show()
