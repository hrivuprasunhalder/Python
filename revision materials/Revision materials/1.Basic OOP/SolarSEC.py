class  Employee:
	organization ="SolarSEC"
	def __init__(self,name,salary):
		self.name=name
		self.salary=salary
	def __str__(self):
	  return f"{self.name} is an employee of {Employee.organization}.Currently they are paid {self.salary} USD"	
