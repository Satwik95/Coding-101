def update(bit,i,val,N):
    while i<=N:#logN
        bit[i]+=val
        i+=(i&(-i))
                
def query(bit,i):
    res = 0
    while i>0:
        res+=bit[i]
        i-=(i&(-i))
    return res

def countInv(a,bit,N):
    i=N
    ans=0
    while i>=1:
        ans+=query(bit,a[i-1]-1)
        update(bit,a[i-1],1,N)
        i-=1
    return ans

if __name__=="__main__":
    a = [5,2,1,4,3]
    N=len(a)
    bit = [0]*(max(a)+1)
    print(countInv(a,bit,N))
