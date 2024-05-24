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
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        