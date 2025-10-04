from bisection_method import bm

eq=bm("math.sin(x)")
value=eq.evaluate( 1,4,.00000000000000001,100)#(smaller value,bigger value)
	
