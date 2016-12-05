import re
def to_rna(strand=''):
	strand=strand.replace('G','1')
	strand=strand.replace('C','2')
	strand=strand.replace('T','3')
	strand=strand.replace('A','4')
	regw=re.compile('^[0-9]*$')

	if(not regw.match(strand)):
		return ''

	strand=strand.replace('1','C')
	strand=strand.replace('2','G')
	strand=strand.replace('3','A')
	strand=strand.replace('4','U')

	return strand
