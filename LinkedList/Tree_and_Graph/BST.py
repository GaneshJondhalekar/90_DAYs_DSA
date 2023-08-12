class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None
    
    def insert(self,data):
        if self.root==None:
            self.root=Node(data)
            return
        self.insert_recursively(self.root,data)

    def insert_recursively(self,root,data):
        if data<=root.data:
            if root.left:
                self.insert_recursively(root.left,data)
            else:
                root.left=Node(data)
        else:
            if root.right:
                self.insert_recursively(root.right,data)
            else:
                 root.right=Node(data)
    
    def search(self,root,data):
        if root:
            if data==root.data:
                return True
            if data<root.data:
                return self.search(root.left,data)
            else:
                return self.search(root.right,data)
        else:
            return False

    def delete(self,root,parent,data):
        if root:
            if data==root.data:
                #check node has one child or two or zero child
                if root.left==None and root.right==None:#check child has zero child then we can directly delete 
                    if parent.left.data==data:
                        parent.left=None
                    else:
                        parent.right=None

                elif root.left and root.right:#check child has two nodes
                    pass
                else:
                    if parent.left==data:
                        parent.left=root.left
                    else:
                        parent.right=root.left
               

            elif data<root.data:
                self.delete(root.left,root,data)
            else:
                self.delete(root.right,root,data)

        else:
            print("No data found")
    #Tree travalsing 
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)

    def preorder(self,root):
        if root:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)
    
    
t=BST()
t.insert(10)
t.insert(5)
t.insert(6)
t.insert(3)
t.insert(25)
t.insert(20)
t.delete(t.root,t.root,6)
t.delete(t.root,t.root,20)
print(t.search(t.root,6))
print(t.search(t.root,21))
print('Inorder : ',end='')
t.inorder(t.root)
print('Preorder : ',end='')
t.preorder(t.root)
print('Postorder : ',end='')
t.postorder(t.root)