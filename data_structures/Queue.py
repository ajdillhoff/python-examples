class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        
    def is_empty(self):
        return len(self.items) == 0
    
    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)

    
if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q)