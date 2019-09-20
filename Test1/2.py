#Using list comprehension, write a program to print the list after removing the even numbered elements in [12,24,35,70,88,120,155]. Also check if the remaining elements are divisible by 5 or 7.

l=[12,24,35,70,88,120,155]
print("Before : ",l)
l=[x for x in l if x%2!=0]
print("After removing even elements :",l)
for i in l :
	if i%5==0 and i%7==0:
		print(i," is divisible by both 5 and 7")
	else:
		if i%5==0:
			print(i," is divisible by 5")
		
		elif i%7==0:
			print(i," is divisible by 7")
		elif i%5!=0 and i%7!=0:
			print(i," is neither divisible by 5 nor 7")			
		
