#Stupid program to help me try to learn OOP

from math import *

class Calculator:

    def add(a,b):
        return a + b

    def sub(a,b):
        return a - b

    def multi(a,b):
        return a * b

    def div(a,b):
        return a / b

    def power(a,b):
        return a ** b

    def factorial(a):
        if a == 1:
            return a 
        else:
            return a * Calculator.factorial(a - 1)

    def root(a,b):
        return a ** (1/b)

    def cos(a):
        return cos(a)
    def sin(a):
        return sin(a)
    def tan(a):
        return tan(a)


print(Calculator.sin(0))
