n=int(input("Enter the no of elements\n"))
lis=[]
print("Enter the elements\n")
for i in range(n):
	lis.append(input())
min=lis[0]
max=lis[0]
for i in lis:
	if(i<min):
		min=i;
print("Minimum element = ",min)			
for i in lis:
	if(i>max):
		max=i;
print("Maximum element = ",max)
print("List = ",lis)
lis.insert(0,7)
print(lis)
del lis[0]
print(lis)
key=input("Enter an element to be searched")
if key in lis:
	print("Element found\n")
else:
	print("Element not found\n")		

