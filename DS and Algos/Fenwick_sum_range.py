def update(bit,i,inc,N):
    while i<=N:#logN
        bit[i]+=inc
        i+=(i&(-i))
        
def build(a,N):#tc = 0(NlogN)
    for i in range(1,N):
        update(bit,i,a[i],N)
        
def query(bit,l,r):
    res=[0]*2
    i=l-1
    while i>0:
        res[0]+=bit[i]
        i-=(i&(-i))
    i=r
    while i>0:
        res[1]+=bit[i]
        i-=(i&(-i))
    return res[1]-res[0]#sum[r]-sum[l-1]

if __name__=="__main__":
    a = [1,2,3,4,7,8]
    N=len(a)
    bit = [0]*(N+1)
    build(a,N)
    print(query(bit,2,5))#returns the sum in range
