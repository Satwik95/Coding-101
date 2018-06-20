def f(n):
    count = [0]*64

    for j in range(0,len(n)):
        no = n[j]
        i = 0
        while no>0:
            count[i] += (no&1)
            no = no>>1
            i+=1

    ans = 0

    for i in range(0,len(count)):
        count[i]%=3

        if count[i]==1:
            ans+= 1<<i

    return ans


n = [1,1,1,2,2,2,3]
print(f(n))
