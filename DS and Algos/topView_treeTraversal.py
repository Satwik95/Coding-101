"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def topView(root):
    if root==None:
      return
    q = []
    lot = []
    h = {}
    hd = 0
    q.append(root)
    h[root]=hd
    while q:
      temp = q.pop(0)
      lot.append(temp)
      print(temp.info,end=" ")
      if temp.left!=None:
        if h[temp]-1 not in list(h.values()):
          q.append(temp.left)
          h[temp.left]=h[temp]-1
      if temp.right!=None:
        if h[temp]+1 not in list(h.values()):
          q.append(temp.right)
          h[temp.right]=h[temp]+1
