import sys
sys.setrecursionlimit(3000)
class node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self,root,data):
        if self.root==None:
            self.root = node(data)
            return 
        else:
            if root.data>data:
                if root.left==None:
                    root.left = node(data)
                else:
                    self.insert(root.left,data)
            if root.data<data:
                if root.right==None:
                    root.right = node(data)
                else:
                    self.insert(root.right,data)

    def preorder(self,root):
        if root==None: return
        print(root.data)
        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self,root):
        if root==None: return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data)

    def inorder(self,root):
        if root==None: return
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)

    def findMin(self,root):
        if root==None: return
        else:
            if root.left==None:
                return root.data
            else:
                self.findMin(root.left)
        


if __name__ == '__main__':

    t = Tree()
    x = [5,4,1,6,9,3,2,7]
    for i in x:
        t.insert(t.root,i)
    print("Preorder Traversal")
    t.preorder(t.root)
    print("Inorder Traversal")
    t.inorder(t.root)
    print("Postorder Traversal")
    t.postorder(t.root)
    print("Min Val in the BST is:", t.findMin(t.root))
    #t.levelorder()
