#Write a python program to read in a list of elements.
#Create a new list that holds all the eemets minus teh duplicate (Use functions).

list =[]
n=int(input("Enter number of elements"))
print("Enter the elements")
for i in range(n) :
	list.append(int(input()))
def remove_dup(list):
	list2=[]
	for i in list:
		if i not in list2:
			list2.append(i)
	print(list2)
remove_dup(list)

#Write a python program to read in a list of numbers
#Use one-line coprehensions of create a new list of even numbers.
#Create another list reversing the elements.

S= [x**2 for x in range (10)] #Read elements to the list
M= [x for x in S if x%2==0]

print(S)
print(M)
M.reverse()
print(M)	

"""Output
Enter number of elements5
Enter the elements
1
1
2
3
4
[1, 2, 3, 4]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 4, 16, 36, 64]
[64, 36, 16, 4, 0]
"""

