def HourMinute(num):
	hours=int(num/60)
	mini=num%60
	s=str(hours)+":"+str(mini)
	return(s)

print("Time in hours and minutes is :",HourMinute(int(input("Enter the number of minutes "))))	
