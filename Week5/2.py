#Write a python programs to count the frequncy of words i a given file.
from collections import Counter
def word_count(fname):
	with open(fname) as f:
		return Counter(f.read().split())
		
print("Number of words in the file :",word_count("test.txt"))		

"""
Output:
Number of words in the file : Counter({'the': 9, "I'm": 8, 'gonna': 8, "can't": 8, 'me': 8, 'tell': 8, "nothin'": 8, 'I': 7, 'You': 7, 'my': 7, 'to': 5, 'no': 4, 'town': 4, 'more': 4, 'nobody': 4, 'old': 4, "'til": 4, "Can't": 4, 'horse': 4, 'road': 4, 'ride': 4, 'take': 4, 'on': 4, 'is': 3, 'in': 3, 'a': 3, 'can': 2, 'Yeah,': 2, 'been': 2, 'got': 2, "Ridin'": 2, 'and': 2, 'black': 2, 'Bull': 1, 'horses': 1, 'bladder': 1, 'attached': 1, 'porch,': 1, 'life': 1, 'up': 1, 'Lean': 1, 'hat': 1, "ridin'": 1, 'Hat': 1, 'movie': 1, 'ask': 1, 'that': 1, 'off': 1, 'her': 1, 'booty': 1, 'horse,': 1, 'Horse': 1, 'Got': 1, 'boobies': 1, 'your': 1, 'go': 1, 'Porsche': 1, "that's": 1, 'baby': 1, 'My': 1, 'Wrangler': 1, 'valley': 1, 'Gucci': 1, 'from': 1, 'tack': 1, "ain't": 1, 'now': 1, 'match': 1, 'matte': 1, 'Kio)': 1, 'boots': 1, 'whip': 1, 'ha': 1, 'Cheated': 1, 'Cowboy': 1, 'all': 1, 'tractor': 1, '(Kio,': 1, 'back': 1})
"""
