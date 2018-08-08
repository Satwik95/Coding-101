def transpose(a,N,M):
    for i in range(N):
        for j in range(i+1,M):
            a[i][j],a[j][i]=a[j][i],a[i][j]
    return a

def rot_clock(org,N,M):
    # to rotate clock wise
    #transpose original matrix and reverse the rows of transpose
    a = transpose(org,N,M)
    for i in range(N):
        j=0
        k=M-1
        while j<k:
            a[i][j],a[i][k]=a[i][k],a[i][j]
            j+=1
            k-=1

    return a

def rot_antiClock(org,N,M):
    # to rotate anti clock wise
    #transpose original matrix and reverse the cols of transpose
    #a = transpose(org,N,M)
    for j in range(M):
        i=0
        k=N-1
        while i<k:
            a[i][j],a[k][j]=a[k][j],a[i][j]
            i+=1
            k-=1
    return a

if __name__=="__main__":
    N = int(input())#rows
    M = int(input())#cols
    org = [[int(input()) for x in range(M)]for y in range(N)]
    print(org)
    a = rot_clock(org,N,M)
    print(a)
    a = rot_antiClock(org,N,M)
    print(a)
    

    
    
