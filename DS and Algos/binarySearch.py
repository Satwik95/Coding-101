def binarySearch(a,val):
    start=0
    end=len(a)-1
    while(start<=end):
        mid = int((start+end)/2)
        if a[mid]==val:
            return True
        elif a[mid]>val:
            end=mid-1
        else:
            start = mid+1
    return False

if __name__ == "__main__":
    a = [1,2,4,5,6,7,8]
    if binarySearch(a,3):
        print("Found :)")
    else:
        print("Not found :(")
