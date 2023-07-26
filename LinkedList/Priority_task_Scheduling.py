#i want execute task first having high priority (high priority means 1 is higher proirity than 2)

class Task:
    def __init__(self,name,priority):
        self.name=name
        self.priority=priority
        self.next=None

class TaskScheduler:
    def __init__(self):
        self.head=None
    
    def add_task(self,name,priority):
        new_task=Task(name,priority)
        if self.head:
            if self.head.priority>=new_task.priority:
                new_task.next=self.head
                self.head=new_task
                return
            current_task=self.head
            temp=current_task
            while current_task.next!=None and new_task.priority>=current_task.priority:
                temp=current_task
                current_task=current_task.next
            if new_task.priority<=current_task.priority:
                new_task.next=current_task
                temp.next=new_task
                return
            current_task.next=new_task
            return
        else:
            self.head=new_task
        
    def Print(self):
        t=self.head

        while t!=None:
            print(t.name,t.priority)
            t=t.next
        
t1=TaskScheduler()
t1.add_task('task A',3)
t1.add_task('task B',1)
#t1.Print()
t1.add_task('task C',4)
#t1.Print()
t1.add_task('task D',2)
t1.Print()


