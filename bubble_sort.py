#bubble sort
l=[2,3,4,1]

for i in range(0,len(l)):
	for j in range(0,len(l)-i-1):
		if(l[j]>l[j+1]):
			l[j],l[j+1]=l[j+1],l[j]
print(l)