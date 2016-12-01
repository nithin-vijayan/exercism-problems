def hello(leap=''):
	if(leap%4==0 or leap%400==0):
		if(leap%100!=0 and leap%400!=0):
			return 'non leap'
		return 'leap'