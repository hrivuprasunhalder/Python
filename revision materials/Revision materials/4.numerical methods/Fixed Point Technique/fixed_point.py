import math
class fp:

	def __init__(self,func):
		  self.func=func
		
	def evaluate(self,p0,tol,N):
	    for n in range(N):
	  	  p=eval(self.func.replace('x',str(p0)),{"math":math})	
	  	  print(f" Iteration {n+1} : x={p0}")
	  	  if abs(p-p0)<tol:
	  		  break
	  	  else : 
	  		  p0=p  
	  				
