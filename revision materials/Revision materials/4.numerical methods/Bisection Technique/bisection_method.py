import math
class bm:

	def __init__(self,func):
		  self.func=func
		
	def evaluate(self,a,b,tol,N):
	    p_old=0	
	    for n in range(N):
	  	  p=(a+b)/2
	  	  fa=eval(self.func.replace('x',str(a)),{"math":math})	
	  	  fp=eval(self.func.replace('x',str(p)),{"math":math})
	  	  print(f" Iteration {n+1} : a = {a},b = {b},p = {p},FP = {fp}")
	  	  if fp==0 or (abs(p-p_old)/min(abs(a),abs(b)))<tol:
	  		  break
	  	  if fa*fp>0:
	  		  a=p
	  	  else : #an else statement is always associated with the most recent unmatched if,in this case fa*fp>0
	  		  b=p  		
	  	  p_old=p  
	  				
	  			
