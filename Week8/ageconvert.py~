from datetime import datetime,timedelta
def AgeConvert(s):
	year =int(s[0]+s[1]+s[2]+s[3])
	if(s[5].isdigit() and s[5]!='0'):
		month=int(s[5]+s[6])
	elif(s[5]=='0'):
		month=int(s[6])
	else:
		month=int(s[5])
	if(s[8].isdigit() and s[8]!='0'):
		day=int(s[8]+s[9])
	elif(s[8]=='0'):
		day=int(s[9])
	else:
		day=int(s[8])			
	s= str(datetime.today()-datetime(year,month,day))
	s1=""
	for i in s :
		if(i==' '):
			break
		else:
			s1+=i
	return(int(int(s1)/365))			
		
	
print("Your age is : ",AgeConvert(input("Enter dob in YYYY-MM-DD :")))	
	

