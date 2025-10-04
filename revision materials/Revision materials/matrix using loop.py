matrix=[[1,3,5],[7,9,12],[15,17,19]]
for x in matrix:                #if we start from x=0 that means the are using the [1,3,5]
	for y in range(len(x)):       #for x=0,there are 3 components in that list [1,3,5],so range=3
		x[y]=x[y]*2		              #y is the component in this list,it iterates from 0 to 2,so x[y]=0[0]=1
		                            #0[1]=3,0[2]=5. After that x changes and increases to x=1 and the loop continues               
print(matrix)		
