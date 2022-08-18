n=int(input("enter a number"))
c=0
for i in range(2,n+1):
    if n%i==0:
        c+=1
if c==1:
    print("{} is a prime number".format(n))
else:
    print("{} is not a prime number".format(n))


