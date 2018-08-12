def max_heapify(a,i,n):
    largest=i
    left=2*i+1
    right=2*i+2
    if left<n and a[left]>a[largest]:
        largest=left
    if right<n and a[right]>a[largest]:
        largest=right
    if largest!=i:
        a[largest],a[i]=a[i],a[largest]
        max_heapify(a,largest,n)

def heap_sort(a):
    #build max heap
    for i in range(len(a),-1,-1):
        max_heapify(a,i,len(a))
    #extract the largest vals
    for i in range(len(a)-1,0,-1):
        #till 1, because only the smallest will be left automatically
        a[i],a[0]=a[0],a[i]
        max_heapify(a,0,i)
    return a

if __name__=="__main__":
    a = [5,6,3,4,2,1,55,677,88,99,1000,10,10,111111,-345,-2,2343]
    print(heap_sort(a))
        
        
