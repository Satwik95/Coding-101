import sys

def buildTree_min(tree,a,index,s,e):
    if s>e:
        return
    if s==e:
        tree[index]=a[s]    
        return
    #rec case
    mid = int((s+e)/2)
    buildTree(tree,a,2*index,s,mid)
    buildTree(tree,a,2*index+1,mid+1,e)
    tree[index]=min(tree[2*index],tree[2*index+1])

def buildTree_max_sum(tree,a,index,s,e):
    if s>e:
        return
    if s==e:
        tree[index]=a[s]    
        return
    #rec case
    mid = int((s+e)/2)
    buildTree_max_sum(tree,a,2*index,s,mid)
    buildTree_max_sum(tree,a,2*index+1,mid+1,e)
    #here am just calculating the max possible sum in that array, but not considering the sequence.
    #so I have to use the max sub array wala dp 
    tree[index]= max(tree[2*index],tree[2*index+1],tree[2*index]+tree[2*index+1])
    
def query_min(tree,index,s,e,qs,qe):
    #no overlap
    if qs>e or s>qe:
        return sys.maxsize
    #complete overlap
    if s>=qs and e<=qe:
        return tree[index]
    #partial overlap
    mid = int((s+e)/2)
    leftans = query_min(tree,2*index,s,mid,qs,qe)
    rightans = query_min(tree,2*index+1,mid+1,e,qs,qe)
    return min(leftans,rightans)

def query_max(tree,index,s,e,qs,qe):
    #no overlap
    if qs>e or s>qe:
        return -sys.maxsize
    #complete overlap
    if s>=qs and e<=qe:
        return tree[index]
    #partial overlap
    mid = int((s+e)/2)
    leftans = query_max(tree,2*index,s,mid,qs,qe)
    rightans = query_max(tree,2*index+1,mid+1,e,qs,qe)
    return max(leftans,rightans)

def node_update(tree,index,s,e,i,val):
    #no overlapping
    if i<s or i>e:
        return
    #complete overlapping
    if s==e:
        tree[index]=val
        return
    #partial overlapping
    mid = int((s+e)/2)
    node_update(tree,2*index,s,mid,i,val)
    node_update(tree,2*index+1,mid+1,e,i,val)
    tree[index]=min(tree[2*index],tree[2*index+1])
    return    
def range_update(tree,a,index,s,e,qs,qe,val):
    #no overlapping
    if s>qe or e<qs:
        return
    #complete overlapping
    if s==e:
        a[s]+=val
        return
    #partial overlapping
    mid = int((s+e)/2)
    range_update(tree,a,2*index,s,mid,qs,qe,val)
    range_update(tree,a,2*index+1,mid+1,e,qs,qe,val)
    tree[index] = min(tree[2*index],tree[2*index+1])
    return
    
if __name__=="__main__":        
    a = [0,2,4,-6,7]
    tree = [None]*(4*len(a)+1)
    #buildTree_min(tree,a,1,0,len(a)-1)
    qs=0
    qe=5
    #print(query(tree,1,0,len(a)-1,qs,qe))
    #node_update(tree,1,0,len(a)-1,4,4)
    #print("after node update",query(tree,1,0,len(a)-1,qs,qe))
    #range_update(tree,a,1,0,len(a)-1,2,4,3)
    #print("after range update",a)
    buildTree_max_sum(tree,a,1,0,len(a)-1)
    print(query_max(tree,1,0,len(a)-1,qs,qe))
