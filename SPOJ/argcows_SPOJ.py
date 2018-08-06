def canPlace(stal_loc,min_dist,c):
    no_cows=1
    start = stal_loc[0]
    for j in range(1,len(stal_loc)):
        end = stal_loc[j]
        cur_dist = end-start
        if cur_dist>=min_dist:
            no_cows+=1
            if no_cows==c:
                return True
            start = stal_loc[j]
    return False
            
def argcows(stal_loc,s,e):
    dist = -1
    while s<=e:
        mid = int((s+e)/2)
        if canPlace(stal_loc,mid,c):
            dist=max(dist,mid)
            #max min dist
            s=mid+1
        else:
            e=mid-1
    return dist
        
if __name__=="__main__":
    t = int(input())
    res = []
    while t>0:
        n,c = input().split(" ")
        n = int(n)
        c = int(c)
        stal_loc = []
        for i in range(n):
            stal_loc.append(int(input()))
        res.append(argcows(stal_loc,0,stal_loc[n-1]))
        t-=1
    for x in res:
        print(x)
    
