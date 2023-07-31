class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class Circuler_DLL:
    def __init__(self):
        self.head=None


    def add_node_at_start(self,data):
        new_node=Node(data)
        if self.head:
            new_node.next=self.head
            new_node.prev=self.head.prev
            new_node.prev.next=new_node
            self.head=new_node
            return
        new_node.next=new_node
        new_node.prev=new_node
        self.head=new_node

    def add_node_at_end(self,data):
        if self.head:
            new_node=Node(data)
            self.head.prev.next=new_node
            new_node.prev=self.head.prev
            self.head.prev=new_node
            new_node.next=self.head
            return
        self.add_node_at_start(data)

    def Print(self):
        temp=self.head
        while temp.next!=self.head:
            print(temp.data)
            temp=temp.next
        print(temp.data)
        


d=Circuler_DLL()
d.add_node_at_start(1)
d.add_node_at_end(2)
d.add_node_at_start(0)
d.Print()
d.add_node_at_end(3)
d.Print()
        
        