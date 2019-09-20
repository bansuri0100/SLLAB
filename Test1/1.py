#Write a python function that accepts a string and calculates the number of upper case and lower case letters.Also it reverses the string and display its length.

def count(s):
	lCount=0
	uCount=0
	for i in s:
		if i.islower():
			lCount+=1
		elif i.isupper():
			uCount+=1
	print("Number of lower case letters = ",lCount)
	print("Number of upper case letters = ",uCount)

s=str(input("Enter the string:"))
count(s)

def reverse(s):
	s1=""
	length=0
	for i in s:
		s1=i+s1
		length+=1
	print("Reversed string = ",s1)
	print("Length of string = ",length)
reverse(s)
	
		
	


	
