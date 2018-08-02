import sys
def update(bit,i,val,N):
    while i<=N:#logN
        bit[i]=max(bit[i],val)
        i+=(i&(-i))
        
def build(bit,a,N):#tc = 0(NlogN)
    for i in range(1,N+1):
        update(bit,i,a[i-1],N)
        
def query(bit,i):
    res = -sys.maxsize
    while i>0:
        res=max(res,bit[i])
        i-=(i&(-i))
    return res

if __name__=="__main__":
    a = [10,2,3,4,7,8]
    N=len(a)
    bit = [0]*(N+1)
    build(bit,a,N)
    print(query(bit,3))#returns the sum in range
