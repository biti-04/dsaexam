class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,element):
        self.queue.append(element)
    def dequeue (self):
        return self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            return "queue is empty"
        return self.queue[0]
#creating a queue
numbers = Queue()
numbers.enqueue(1)
numbers.enqueue(2)
numbers.enqueue(3)
numbers.enqueue(4)
print("Inserted Numbers: ",numbers.queue)
print("dequeue: ", numbers.dequeue())