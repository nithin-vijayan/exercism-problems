def distance(firstDna='', secondDna=''):
		if(len(firstDna)!=len(secondDna)):
			raise ValueError 
		hamminglength=0
		for firstChar,secondChar in zip(firstDna,secondDna):
			if(firstChar!=secondChar):
				hamminglength=hamminglength+1
		return hamminglength
