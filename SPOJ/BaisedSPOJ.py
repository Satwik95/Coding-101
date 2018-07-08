import sys
def calc_badness(N,h):
    freq = [0]*(N+1)
    for x in h:
        freq[h[x]]+=1
    badness = pos = 0
    for i in range(1,N+1):
        while freq[i]:
            pos+=1
            badness += abs(i-pos)
            freq[i]-=1
    return badness
    
if __name__ == "__main__":
    T = int(input())
    while T:
        h = {}
        _ = input()
        N = int(input())
        for i in range(0,N):
            name,pref_rank = input().split(" ")
            pref_rank = int(pref_rank)
            h[name]=pref_rank
        print(calc_badness(N,h))
        T-=1
        
