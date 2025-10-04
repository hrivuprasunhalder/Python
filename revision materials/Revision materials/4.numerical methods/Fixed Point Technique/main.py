from fixed_point import fp

eq=fp(".5*((10-x**3)**.5)")
value=eq.evaluate(1.5,.00000000000000000000000000001,100)
