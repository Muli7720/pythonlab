
a=int(input())
b=int(input())
m=min(a,b)
for i in range(1,m+1):
	if(a%i==0)and(b%i==0):
             	hcf=i
print(hcf)
