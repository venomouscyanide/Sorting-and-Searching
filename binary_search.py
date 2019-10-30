#binary search
l=[1,2,3,4,5]

def binary(mid,key):
	try:
		if(key==l[mid]):
			print(l[mid])
			print("Found!")
	except:
		print("Not found")
		return(None)
	if(key>l[mid]):
		binary(mid+1,key)
	if(key<l[mid]):
		binary(mid-1,key)

if __name__ == '__main__':
	key=1
	mid=int(len(l)/2)
	binary(mid,key)