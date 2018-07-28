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
    
def query_lazy(tree,index,s,e,qs,qe):
    #resolve the node
    if lazy[index]!=0:
        tree[index]+=lazy[index]
        #if not a leaf node
        if s!=e:
            lazy[2*index]+=lazy[index]
            lazy[2*index+1]+=lazu[index]
        lazy[index]=0
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

def range_update_lp(tree,lazy,index,s,e,qs,qe,inc):
    #resolve the node
    if lazy[index]!=0:
        tree[index]+=lazy[index]
        #if not a leaf node
        if s!=e:
            lazy[2*index]+=lazy[index]
            lazy[2*index+1]+=lazy[index]
        lazy[index]=0
    #no overlap
    if qs>e or s>qe:
        return
    #complete overlap
    if s>=qs and e<=qe:
        tree[index]+=inc
        #if noon leaf node then pass the increment value
        if s!=e:
            lazy[2*index]+=inc
            lazy[2*index+1]+=inc
        return
    #if partial overlap
    mid = int((s+e)/2)
    range_update_lp(tree,lazy,2*index,s,mid,qs,qe,inc)
    range_update_lp(tree,lazy,2*index+1,mid+1,e,qs,qe,inc)
    tree[index]=min(tree[2*index],tree[2*index+1])
    return

if __name__=="__main__":        
    a = [1,-2,0,-3,2,5]
    tree = [0]*(4*len(a)+1)
    lazy = [0]*(4*len(a)+1)
    buildTree(tree,a,1,0,len(a)-1)
    qs=0
    qe=5
    print(query_lazy(tree,1,0,len(a)-1,qs,qe))
    range_update_lp(tree,lazy,1,0,len(a)-1,1,3,4)
    # after range update, a will ve 1,2,4,1,2,5, min=1
    print(query_lazy(tree,1,0,len(a)-1,qs,qe))
    
