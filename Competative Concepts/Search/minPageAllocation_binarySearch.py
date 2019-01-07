def util(n,m,mid):
    pages = 0
    count = 1
    for i in range(0,len(n)):
        if n[i]>mid:
            return False
        if pages+n[i]>mid:
            #set value for the cur book and increment the student count!!
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
        #assuming that mid becomes the upper bound, and no student is reading more than that many no of pages
        # example the pages are: 2 students,search space is (10-100), 100 = sum of pages of all the books,
        #so the no of pages in the give array be say 10 20 30 40
        # let s1 = 10+20<=50, s2 = 30, s3 = 40
        #no we have only 2 students, but to assign for max 50, we are needing one more student, hence this can't be the answer
        #so we logically have to increase the mid val in this case, start=mid+1
        mid = int((start+end)/2)
        if util(n,m,mid):
            finalAns = mid
            #to minimize the maximum pages
            end=mid-1
        else:
            start=mid+1
    return finalAns
    
if __name__ == "__main__":
    _ = int(input())
    m=int(input())#no of students
    n = [int(x) for x in input().split(" ")]
    n = sorted(n)
    m = 2
    print(allocatePage(n,m))
