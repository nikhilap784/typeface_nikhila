def con(n):
	if(n==0):
		return
	a=n%3
	n=n//3
	if(a<0):
		n=n+1
	con(n)
	if (a<0):
		print(a+(-3),end="")
	else:
		print(a,end="");
n=int(input())
if (n!=0):
	con(n)
else:
	print("0",end="")
