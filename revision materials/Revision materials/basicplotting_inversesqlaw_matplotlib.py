import matplotlib.pyplot as plt
x=[2,3,4,5,6,7,8,9]
y=[7.77,7.23,6.76,6.37,6.053,5.75,5.55,5.33]
x2=[2,3,4,5,6,7,8,9]
y2=[7.81,7.22,6.81,6.36,6.01,5.65,5.5,5.2]

plt.plot(x,y,label="Group-1")
plt.plot(x2,y2,label="Group-2")
plt.title("Invesre square Law")
plt.xlabel("Distance(cm)")
plt.ylabel("lnI")
plt.legend()
plt.show()
