class BSTNode:
    def __init__(self,data):
        self.right = None
        self.left = None
        self.data = data
        self.height = 1
        
class AVL_Tree:
    def __init__(self):
        self.root=None
    def height(self,root):
        if root==None:
            return -1
        return root.height
    
    def insert(self,root,data):
        if self.root==None:
            self.root = BSTNode(data)
            return self.root
        else:            
            if data>root.data:
                if root.right==None:
                    root.right = BSTNode(data)
                else:
                    root.right = self.insert(root.right,data)
            if root.data>data:
                if root.left==None:
                    root.left = BSTNode(data)
                else:
                    root.left = self.insert(root.left,data)

        root.height = 1 + max(self.height(root.left),
                             self.height(root.right))
        balance = self.height(root.left) - self.height(root.right)
        #check the kind of error
        #left-left
        if balance>1 and data<root.left.data:
            return self.rotRight(root)
        #left-right
        if balance>1 and data>root.left.data:
            root.left = self.rotLeft(root.left)
            return self.rotRight(root)
        #right-right
        if balance<-1 and data>root.right.data:
            return self.rotLeft(root)
        #right-left
        if balance<-1 and data<root.right.data:
            root.right = self.rotRight(root.right)
            return self.rotLeft(root)
        return root
        
    def rotRight(self,root):
        y = root.left
        x = y.right
        y.right = root
        root.left = x
        root.height = 1 +max(self.height(root.left),self.height(root.right))
        y.height = 1 +max(self.height(y.left),self.height(y.right))
        return y
    
    def rotLeft(self,root):
        y = root.right
        x = y.left
        y.left = root
        root.right = x
        root.height = 1 +max(self.height(root.left),self.height(root.right))
        y.height = 1 +max(self.height(y.left),self.height(y.right))
        return y
    
    def preOrder(self,root):
        if root==None: return
        print(root.data)
        self.preOrder(root.left)
        self.preOrder(root.right)

if __name__=="__main__":
    myTree = AVL_Tree()
    root = None
    root = myTree.insert(root,10)
    root = myTree.insert(root,20)
    root = myTree.insert(root,30)
    root = myTree.insert(root,40)
    root = myTree.insert(root,50)
    root = myTree.insert(root,25)
    nodes = [10,20,30,40,50,25]
    myTree.preOrder(root)
        
        
        
