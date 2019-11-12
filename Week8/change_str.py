def ChangeString(s):
	new=[]
	for i in s:
		new.append(i)
		
		
	new1=[]	
	new2=[]
	for i in new:
		
		if(i.isalpha() and i!='z'):
			new1.append(chr(ord(i)+ 1 ))
		elif(i=='z'):
			new1.append('a')	
		else:
			new1.append(i)
			
				
			
		
	for i in new1:
		
		if (i=='a'or i=='e'or i=='i'or i=='o'or i=='u'):
			
			new2.append(i.upper())
		else:
			new2.append(i)	
			
	str1=""
	
	return(	str1.join(new2))	


s=str(input("Enter the string : "))
print("Modified string =",ChangeString(s))			
