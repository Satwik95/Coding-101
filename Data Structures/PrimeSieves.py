def primeNos(n):
    
    p = [1]*(n+1)

    for i in range(3,n+1,2):
        if p[i]:
            for j in range(i*i,n+1,i):
                p[j] = 0

    print(2,"\n")
    for i in range(3,n+1):
        if i%2!=0 and p[i]==1:
            print(i,"\n")
