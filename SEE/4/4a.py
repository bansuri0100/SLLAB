class Rectangle:
	def __init__(self,l,b,a):
		self.l=l
		self.b=b
		self.a=a
	def area(self):
		self.a=self.l*self.b
		print("Area of the rectangle is :",self.a," units\n")
	
		
print("Enter length and breadth of the rectangle :\n")
l=float(input())
b=float(input())
obj=Rectangle(l,b,1)
obj.area()		 	
			
