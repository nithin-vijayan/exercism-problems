
def is_pangram(string=''):
	for i in range(ord('a'),ord('z')+1):
		if(chr(i) not in string.lower()):
			return False
	return True