
class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority


class Queue:
    def __init__(self):
        self.tasks = []

    def enqueue(self, task):
        self.tasks.append(task)

    def dequeue(self):
        if self.is_empty():
            return None

        highest_priority_index = 0
        for i in range(1, len(self.tasks)):
            if self.tasks[i].priority < self.tasks[highest_priority_index].priority:
                highest_priority_index = i

        return self.tasks.pop(highest_priority_index)

    def is_empty(self):
        return len(self.tasks) == 0

queue = Queue()

# Add tasks to the queue
task1 = Task("Task 1", 2)
task2 = Task("Task 2", 1)
task3 = Task("Task 3", 3)

queue.enqueue(task1)
queue.enqueue(task2)
queue.enqueue(task3)

print(queue.dequeue().name)
print(queue.dequeue().name)
