class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class CirculerSLL:
    def __init__(self):
        self.head=None

    def add_node_at_start(self,data):
        new_node=Node(data)
        if self.head:
            new_node.next=self.head
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            temp.next=new_node
            self.head=new_node
            return
        new_node.next=new_node
        self.head=new_node

    def add_node_at_end(self,data):
        if self.head:
            new_node=Node(data)
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            temp.next=new_node
            new_node.next=self.head
            return
        self.add_node_at_start(data)
    
    def Print(self):
        temp=self.head
       
        while temp.next!=self.head:
            print(temp.data)
            temp=temp.next
        print(temp.data)

s=CirculerSLL()
s.add_node_at_start(1)
s.add_node_at_end(2)
s.Print()
s.add_node_at_start(0)
s.add_node_at_end(3)
s.add_node_at_end(4)
s.Print()
