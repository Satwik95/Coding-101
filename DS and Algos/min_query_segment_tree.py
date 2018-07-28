import sys

def buildTree(tree,a,index,s,e):
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
    
def query(tree,index,s,e,qs,qe):
    #no overlap
    if qs>e or s>qe:
        return sys.maxsize
    #complete overlap
    if s>=qs and e<=qe:
        return tree[index]
    #partial overlap
    mid = int((s+e)/2)
    leftans = query(tree,2*index,s,mid,qs,qe)
    rightans = query(tree,2*index+1,mid+1,e,qs,qe)
    return min(leftans,rightans)

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
    a = [1,-2,0,3,-2,5]
    tree = [None]*(4*len(a)+1)
    buildTree(tree,a,1,0,len(a)-1)
    qs=0
    qe=5
    print(query(tree,1,0,len(a)-1,qs,qe))
    node_update(tree,1,0,len(a)-1,4,4)
    print("after node update",query(tree,1,0,len(a)-1,qs,qe))
    range_update(tree,a,1,0,len(a)-1,2,4,3)
    print("after range update",a)
    
