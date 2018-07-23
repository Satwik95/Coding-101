def towerOfHanoi(n,src,dest,helper):
    if n==0:
        return
    towerOfHanoi(n-1,src,helper,dest)
    print("moving",n,"from",src,"to",dest)
    towerOfHanoi(n-1,helper,dest,src)
    
if __name__=="__main__":
    n=int(input())
    towerOfHanoi(n,"A","C","B")
