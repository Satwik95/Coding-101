import sys

def f(a):
    sum=0
    best = -sys.maxsize
    for i in range(len(a)):
        sum+=a[i]      
        best = max(best,sum)
        if sum<0:
            sum=0
    return best
        
if __name__=="__main__":
    a = [-2,-1,-2,6]
    print(f(a))
    
