from collections import Counter
from functools import reduce
def word_count(fname):
	with open(fname) as f:
		return Counter(f.read().split())
d=word_count("lose_yourself.txt")
print(d)		
print(type(d))
lis=list(d.items())
print(lis)
lis.sort(reverse=True,key=lambda x:x[1])
print(lis)
print("\nThe top 10 most occured words are:")
lis2=[]
for i in range(10):
	print(lis[i][0],"\n")
	lis2.append(lis[i][1])
avg=reduce(lambda a,b:a+b,lis2)/len(lis2)
print("Average is :",avg)
lis2=[x*x for x in lis2 if x%2 != 0]
print("Final list = ",lis2) 	

	
	
		
