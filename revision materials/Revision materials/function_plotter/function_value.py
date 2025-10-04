import math
class FunctionCalculator:
	
	def __init__(self,function_str):
		self.function_str=function_str
	
	def evaluate(self,x_value):
			result=eval(self.function_str.replace('x',str(x_value)),{"math":math})
			return result
