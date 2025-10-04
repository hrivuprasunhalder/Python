from function_calculator import FunctionCalculator
function=FunctionCalculator("math.sin(x)+x**2")
value=function.evaluate(5)
print(f"{value}")
