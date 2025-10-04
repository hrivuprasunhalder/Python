from matplotlib import pyplot as plt
import numpy as np

x=np.arange(0,21)#arange(start,stop,steps)
x1=np.arange(0,21)
x2=x1**2
plt.plot(x,x1,"b-")
plt.plot(x,x2,"g-")
plt.xticks(np.arange(0,21,5))
plt.xlabel("days of reading ")
plt.ylabel("amount of python learned")
plt.title("python learned reading real python vs other sites")
plt.legend(["other site","real python"])
plt.savefig("Real Python",format='png',dpi=300,bbox_inches='tight')

plt.show()
