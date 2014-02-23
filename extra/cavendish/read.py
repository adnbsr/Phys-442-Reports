from pylab import *


filename= open('kadir-adnan.txt','r')

lines=filename.readlines()

filename.close()


for i in range(len(lines)):
	
	lines[i]=lines[i].split(' ')
	

cloumns=[]


for i in range(len(lines)):
	lines[i]=lines[i][0].replace(',','.')
	cloumns.append(lines[i].split('\t'))

for i in range(len(cloumns)):
	cloumns[i][0]=float(cloumns[i][0])
	cloumns[i][1]=float(cloumns[i][1].split('\r')[0])
	

x=[]
y=[]

for i in range(len(cloumns)):
	x.append(cloumns[i][0])
	y.append(cloumns[i][1])

plot(x,y,'b-')
xlabel('Time')
ylabel('Voltage')
show()



	
