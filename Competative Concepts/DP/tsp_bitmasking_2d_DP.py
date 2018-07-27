import sys
n=4
all_visited = (1<<n) -1
dp=[[-1 for x in range(n)]for y in range(pow(2,n))]
def f(mask,pos):
    if mask==all_visited:
        return dist[pos][0]
    if dp[mask][pos]!=-1:
        return dp[mask][pos]
    best = sys.maxsize
    for city in range(0,n):
        if (mask & 1<<city) == 0:
            res = dist[pos][city]+f((mask | 1<<city),city)
            #mask = mask | 1<<city  ----------important
            #we dont need to store the val of mask, bceause of the for loop, we know that the
            #particualr next city has been visited, so for that we dont have to check again
            #when in the first branch , d se c ko wapas ata hai, toh n is already =3, so the loops ends, and it goes back to
            #b ka functional call, now c, ke liye call hua tha idhar, matlab 2 ho chuka, ab city++3 ko jaega
            #to next b se D pe jaega, and then we will have overlapping sub problems
            best=min(best,res)
    print(pos)
    dp[mask][pos]=best
    return dp[mask][pos]

#dist = [[0,20,42,25],[20,0,30,34],[42,30,0,10],[25,34,10,0]]
dist = [[0,10,1,4],[10,0,12,1],[1,12,0,3],[4,1,3,0]]
print(f(1,0))
