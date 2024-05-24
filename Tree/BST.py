class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class BstTree:
    def __init__(self):
        self.root=None
        
    def insert(self,data):
        if self.root:
            self.insert_recursively(data,self.root)
            return
        self.root=Node(data)
        
    def insert_recursively(self,data,root):
        if root:
            if data<=root.data:
                if root.left:
                    self.insert_recursively(data,root.left)
                else:
                    root.left=Node(data)
            else:
                if root.right:
                    self.insert_recursively(data,root.right)
                else:
                    root.right=Node(data)
            return
        root=Node(data)
        
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)
            return
        
    def preorder(self,root):
        if root:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)
            return
    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)
            return
    def search(self,target,root):
        if root:
            if target==root.data:
                print("Target found")
            elif target<root.data:
                if root.left:
                    self.search(target,root.left)
                else:
                    print("Target not found")
            else:
                if root.right:
                    self.search(target,root.right)
                else:
                    print("Target not found")
            return
        print("Target not found")
        
        
        
        
        
        
t=BstTree()
t.insert(10)
t.insert(2)
t.insert(16)
t.insert(20)
t.insert(23)
t.insert(1) 
t.insert(100)
t.insert(0)
t.inorder(t.root)
t.preorder(t.root)        
t.postorder(t.root)     
t.search(23,t.root)
t.search(30,t.root)   
t.search(0,t.root)
        
        
        
        
        
        
        
        
        
        
        
        
        