#returning the highest val
def highestPivot(a,start,end):
    while start<=end:
        mid = int((start+end)/2)
        #find the pivot point
        if mid<end and a[mid]>a[mid+1]:
            return mid,a[mid]
        if mid>start and a[mid]<a[mid-1]:
            return mid-1,a[mid-1]
        #find the unsorted part
        if a[mid]<=a[start]:
            end = mid-1
        elif a[mid]>=a[end]:
            start = mid+1
    
ar = [8,10,4,5,6]
print("index,val:",highestPivot(ar,0,len(ar)-1))
            
