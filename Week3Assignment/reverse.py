#Reverse 3 strings based on descending order of number of vowels in them.

l=[]
class Reverse:
	def __init__(self,s):
		self.s=s
		
	def reverse(self):
		n=0
		for i in self.s:
			if i=='a'or i=='A'or i=='e'or i=='E'or i=='o'or i=='O'or i=='i'or i=='I'or i=='u'or i=='U':
				n+=1
		
		r = ' '.join(reversed(self.s.split(' ')))
		tup=(n,r)
		l.append(tup)
	
for i in range(0,3):
	obj=Reverse(str(input("Enter string :")))
	obj.reverse()
l.sort(reverse=True)
print(l)
for i in range(0,3):
	print(l[i][1])


'''Output
Enter string :aa aa
Enter string :a a
Enter string :aaa aaa
[(6, 'aaa aaa'), (4, 'aa aa'), (2, 'a a')]
aaa aaa
aa aa
a a
'''	
									
				
			
			

