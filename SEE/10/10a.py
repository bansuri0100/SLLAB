from functools import reduce
lis=[1,2,3,4,5,6]
print(lis,end="\n")
lis2=[x*3 for x in lis]
print(lis2,end="\n")
sum1=reduce(lambda a,b:a+b,lis)
sum2=reduce(lambda a,b:a+b,lis2)
print("Sum of 1st list = ",sum1," and sum of 2nd list = ",sum2)
