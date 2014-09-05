"""
>>> D(0,0).score()
[0, 0]
>>> D(1,0).score()
[15, 0]
>>> D(2,0).score()
[30, 0]
>>> D(3,0).score()
[40, 0]
>>> D(0,1).score()
[0, 15]
>>> D(1,2).score()
[15, 30]
>>> D(2,2).score()
[30, 30]
>>> D(2,3).score()
[30, 40]
>>> D(3,3).score()
['Douce']
>>> D(4,3).score()
['Adv', 40]
>>> D(3,4).score()
[40, 'Adv']
>>> D(4,4).score()
['Douce']
>>> D(5,4).score()
['Game', 'less']
>>> D(4,5).score()
['less', 'Game']
"""
class D:
	scores = [0, 15, 30, 40,'Adv','Game']

	def __init__(self, j1, j2):
		self.j1 = j1
		self.j2 = j2

	def score(self):
		if ((self.j1 < 3 and self.j2 < 3)) or ((self.j1 == 'Adv') and (self.j2 != 'Adv')) or ((self.j1 != 'Adv') and (self.j2 == 'Adv')):
			return [self.scores[self.j1], self.scores[self.j2]]
		if ((self.j1 == 3) and (self.j2 == 3)) or ((self.j1 == 4) and (self.j2 == 4)) :
			return ["Douce"]
		elif ((self.j1 == 3) and (self.j2 != 3)) or ((self.j1 != 3) and (self.j2 == 3)):	
			return [self.scores[self.j1], self.scores[self.j2]]
		if (self.j1 == 5):
			return ['Game','less']
		if (self.j2 == 5):
			return ['less','Game']

if __name__ == "__main__":
    import doctest
    doctest.testmod()
