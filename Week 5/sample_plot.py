from pylab import *


def fitting(x,y,sy):

	S   = sum(1 / sy**2)
	Sx  = sum(x / sy**2)
	Sy  = sum(y / sy**2)
	Sxx = sum(x**2 / sy**2)
	Sxy = sum(x*y / sy**2)

	delta = S*Sxx - Sx**2

	n = (Sxx*Sy - Sx*Sxy) / delta
	m = (S*Sxy - Sx*Sy) / delta

	sn = sqrt(Sxx / delta)
	sm = sqrt(S / delta)

	return m,n,sm,sn



s=[]

t=[]










