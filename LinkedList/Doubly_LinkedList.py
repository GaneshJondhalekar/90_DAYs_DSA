
class Node:
    def __init__(self,data):
        self.data=data
        self.pre=None
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None
    
    def add_node_at_start(self,data):
        node=Node(data)
        if self.head:
            node.next=self.head
            self.head.pre=node
            self.head=node
            return
        self.head=node
    
    def add_node_at_end(self,data):
        if self.head:
            node=Node(data)
            t=self.head
            while t.next!=None:
                t=t.next
            t.next=node
            node.prev=t
            return
        self.add_node_at_start(data)
        
    def add_node_at_pos(self,data,pos):
        if pos==1:
            self.add_node_at_start(data)
            return
        if self.head:
            node=Node(data)
            t2=self.head
            t1=t2
            pos-=1
            while t2.next!=None and pos!=0:
                t1=t2
                t2=t2.next
                pos-=1
            if pos==0:
                node.next=t1.next
                t1.next=node
                node.pre=t1
                return
            if pos==1:
                t2.next=node
                node.pre=t2
                return
            print("Postion not found")
            return
    

    
    def Print(self):
        t=self.head
        while t!=None:
            print(t.data)
            t=t.next
        
l=DoublyLinkedList()
l.add_node_at_end(0)
l.add_node_at_start(1)
l.add_node_at_end(5)
l.add_node_at_pos(6,3)
l.add_node_at_pos(3,2)
l.add_node_at_pos(7,6)

l.Print()
        
