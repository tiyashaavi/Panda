s=int(input())
l=list(map(int,input().split()))
m1=max(l)
c=l
c.remove(m1)
m2=max(c)
a=(m1+m2)/2
l=l+[m1]
for i in range(len(l)):
    if(l[i]<a):
        l[i]=0
l=list(map(str,l))
print("".join(l))

##WORKING WITH GITHUB
