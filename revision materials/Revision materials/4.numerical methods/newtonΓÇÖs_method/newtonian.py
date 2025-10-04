from  sympy import symbols,diff
class nm:
	
	def __init__(self,func):
		self.func=func
	
	def evaluate(self,p0,tol,N):
		for n in range(N):
			print(f"Iteration { n+1}: p={p0}")
			fp=eval(self.func.replace('x',str(p0)))
			x=symbols('x')
			df=diff(self.func,x)
			df=str(df)
			dfvalue=eval(df.replace('x',str(p0)))
			p=p0-(fp/dfvalue)
			if abs(p-p0)<tol:
				break
			else:
				p0=p			
