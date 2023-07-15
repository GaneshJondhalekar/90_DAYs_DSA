
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def add_node_at_start(self,data):
        node=Node(data)
        if self.head:
            node.next=self.head
            self.head=node
            return
        self.head=node
    
    def add_node_at_end(self,data):
        node=Node(data)
        if self.head:
            t=self.head
            while t.next!=None:
                t=t.next
            t.next=node
            return
        self.head=node
    
    def add_node_at_position(self,data,pos):
        node=Node(data)
        if self.length()+1<pos:
            print("OUT OF POSITION")
            return
        if self.head:
            t1=self.head
            t2=self.head
           
            pos-=1 #t1 points to first node
            while pos!=0 and t1.next!=None:
                t2=t1
                t1=t1.next
                pos-=1
            if pos==0:
                node.next=t2.next
                t2.next=node
            elif pos==1:
                t1.next=node
           
            return
        if pos==1:
            self.head=node
    
    def Print(self):
        t=self.head
        while t!=None:
            print(t.data)
            t=t.next

    def length(self):
        if self.head:
            n=1
            t=self.head
            while t.next!=None:
                n+=1
                t=t.next
            return n
        return 0


l=LinkedList()
print(f'length={l.length()}')
l.add_node_at_start(1)
l.add_node_at_start(2)
l.add_node_at_position(3,4)
l.add_node_at_end(4)
print(f'length={l.length()}')
l.add_node_at_position(2,2)
l.add_node_at_position(3,4)
print(f'length={l.length()}')
l.Print()


