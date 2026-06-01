#linear queue using list
class queue:
    def __init__(self,size):
        self.size=size
        self.queue=[None]*size
        self.front=-1
        self.rear=-1
    def isFull(self):
        return self.rear==self.size-1
    def isEmpty(self):
        return self.front==-1
    def enQueue(self,x):
        if self.isFull():
            print("Queue is full")
            return
        if self.rear==-1:
            self.front=self.rear=0
            self.queue[self.rear]=x
            return
        self.rear+=1
        self.queue[self.rear]=x
    def deQueue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        if self.rear==self.front:
            x=self.queue[self.front]
            self.rear=self.front=-1
            return x
        x=self.queue[self.front]
        self.front+=1
        return x
    def peek(self):
        if self.isEmpty(self):
            return None
        return self.queue[self.front]