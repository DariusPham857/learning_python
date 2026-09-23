class Calculator: 

  def  __init__(self):
     self.on= False
     self.name = "calculator"

  def add(self,a,b):
       print(a+b)
  def minus(self,a,b):
      print(a-b)
  def multiply(self,a,b):
      print(a*b)
  def divide(self,a,b):
      print(a/b)





a_calc = Calculator()

a_calc.minus(100, 10)
a_calc.add(90,10)
a_calc.multiply(3,4)
a_calc.divide(10,5)
