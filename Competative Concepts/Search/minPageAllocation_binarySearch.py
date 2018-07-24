def util(n,m,mid):
    pages = 0
    count = 1
    for i in range(0,len(n)):
        if n[i]>mid:
            return False
        if pages+n[i]>mid:
            #set value for the cur book and increment the student count
            pages=n[i]
            count+=1
            if count>m:
                return False               
        else:
            pages+=n[i]
    return True

def allocatePage(n,m):
    start = n[len(n)-1] #ans can't be less than the max pages in last book since in sorted order
    end = sum(n)
    finalAns = start
    while start<=end:
        mid = int((start+end)/2)
        if util(n,m,mid):
            finalAns = mid
            end=mid-1
        else:
            start=mid+1
    return finalAns
    
if __name__ == "__main__":
    n = [ 73, 58, 30, 72, 44, 78, 23, 9 ]
    n = sorted(n)
    m = 5
    print(allocatePage(n,m))
