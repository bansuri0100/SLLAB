def OddRange(num1,num):
	l=[]
	for i in range(num1,num2):
		if(i%2!=0):
			l.append(i)
	return(l)
num1=int(input("Enter num1 :"))
num2=int(input("Enter num2 :"))	
print("The odd numbers are : ",OddRange(num1,num2))			
