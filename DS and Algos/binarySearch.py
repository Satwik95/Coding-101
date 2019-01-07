def binarySearch(a,val):
    start=0
    end=len(a)-1
    while(start<=end):
        mid = int((start+end)/2)
        print(a[mid])
        if a[mid]==val:
            return True
        elif a[mid]>val:
            end=mid-1
        else:
            start = mid+1
    return False

def f(nums,val,start,end):
    if len(n):
        return False
    else:
        mid = int(len(nums)/2)
        if nums[mid]==val:
            return mid
        elif val<nums[mid]:
            return f(nums,val,start,mid-1)
        else:
            return f(nums,val,mid+1,end)


def binS(alist, item):
    first = 0
    last = len(alist)-1
    found = False
    while first<=last and not found:
        midpoint = (first + last)//2
        print(alist[midpoint])
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found
           
if __name__ == "__main__":
    a = [3, 5, 6, 8, 11, 12, 14, 15, 17, 18]
    
    if binarySearch(a,8):
        print("Found :)")
    else:
        print("Not found :(")
