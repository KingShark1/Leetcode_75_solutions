class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [-1 for _ in range(k)]
        self.rear = -1
        self.front = 0
        self.size = 0
        self.k = k
        
    def enQueue(self, value: int) -> bool:
        
        if self.queue[(self.rear + 1) % self.k] == -1:
            self.rear = (self.rear + 1) % self.k
            self.queue[self.rear] = value
            self.size += 1
            return True
        else:
            return False
        
    def deQueue(self) -> bool:
        
        if self.queue[self.front] != -1:
            self.queue[self.front] = -1
            self.front = (self.front + 1) % self.k
            self.size -= 1
            return True
        else:
            return False
        
    def Front(self) -> int:
        return self.queue[self.front] if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.queue[self.rear] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        return False
    
    def isFull(self) -> bool:
        if self.size == self.k:
            return True
        return False

