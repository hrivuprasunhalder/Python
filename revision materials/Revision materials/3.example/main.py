# main.py
from mypackage.module1 import greet
from mypackage.module2 import depart
from mypackage.mysubpackage.module3 import people

for person in people:
    greet(person)
    depart(person)
