#
# Skeleton file for the Python "Hello World" exercise.
#


def hello(name=''):
	if(name!='' and name!=None):
		return u'Hello, {0}!'.format(name)
	else:
		return u'Hello, World!'
