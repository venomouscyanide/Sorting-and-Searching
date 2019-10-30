#insertion sort in python
l=[2,3,4,1]

for i in range(0,len(l)):
	j=i
	while(j>0 and l[j]<l[j-1]):
		l[j],l[j-1]=l[j-1],l[j]
		j-=1

print(l)