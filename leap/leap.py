def is_leap_year(leap=''):
	if(leap%400==0):
		return True
	elif(leap%4==0 and leap%100!=0):
		return True
	else:
		return False