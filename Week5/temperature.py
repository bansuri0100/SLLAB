list1=[]
list2=[]
def c_to_f(cel):
	cel_con=float((cel*9/5)+32)
	print("Temp in farenheit = ", cel_con);
	tup=(cel,cel_con)
	list1.append(tup)
def f_to_c(far):
	far_con=float((far-32)*5/9)
	print("Temp in celsius = ", far_con);
	tup=(far,far_con)
	list2.append(tup)
while(True):
	print("1.Convert celsius to farenheit\n2.Convert farenheit to celsius\n3.Enter 0 to exit\n4.Display history of 1.\n5.Display history of 2.\nEnter your choice :")
	choice=int(input())
	if(choice==1):
		print("Enter temp in celsius:")
		cel=float(input())
		c_to_f(cel)
	elif(choice ==2):
			
		print("Enter temp in farenheit:")
		far=float(input())
		f_to_c(far)
	elif(choice ==3):
		sys.exit()
	elif(choice ==4):
		print(list1)
	elif(choice==5):
		print(list2)			
				
