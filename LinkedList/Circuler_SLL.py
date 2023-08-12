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

    def delete_first_node(self):
        if self.head:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            self.head=self.head.next
            temp.next.next=None
            temp.next=self.head

    def delete_last_node(self):
         if self.head:
            temp=self.head
            t1=temp
            while temp.next!=self.head:
                t1=temp
                temp=temp.next
            
            t1.next=self.head
    
    def Print(self):
        temp=self.head
       
        while temp.next!=self.head:
            print(temp.data)
            temp=temp.next
        print(temp.data)

s=CirculerSLL()
s.add_node_at_start(1)
s.add_node_at_end(2)
s.delete_last_node()
s.Print()
s.add_node_at_start(0)
s.delete_first_node()
s.Print()
s.add_node_at_end(3)
s.add_node_at_end(4)
s.delete_last_node()
s.delete_first_node()
s.Print()
