#!/usr/bin/python
a=[1,2,3,4,5]
def mysum(x,y):
	return x+y+10
print(reduce(mysum, a))

print 1+2+10+3+10+4+10+5+10