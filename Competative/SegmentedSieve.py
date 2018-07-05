import math

def sieve(x):
    
    p = [1]*x

    for i in range(3,x,2):
        if p[i]:
            for j in range(i*i,x,i):
                p[j]=0
                
    p[0] = p[1] = 0

    for i in range(4,x,2):
        p[i]=0
        
    return p
        
def segmentedSieve(a,b):
    if a>b: return segmentedSieve(b,a)

    x = int(math.sqrt(b)+1)
    ar = sieve(x)
    print(ar)
    seg_ar = [1]*(b-a+1)

    for i in range(2,x):
        if ar[i]:
            for j in range(a,b+1,1):
                if j==i: continue
                if j%i==0:
                    seg_ar[j-a]=0
                

    return seg_ar
    

print(segmentedSieve(25,36))
