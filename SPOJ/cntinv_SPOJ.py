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
    a = [100,2,-82,3,100]
    b = sorted(set(a))
    h = {}
    i=1
    a_new = []
    #coordinate compression
    for x in b:
        h[x]=i
        i+=1
    for i in range(0,len(a)):
        a_new.append(h[a[i]])
    N=len(a_new)
    bit = [0]*(max(a_new)+1)
    print(countInv(a_new,bit,N))
