from collections import deque
import queue
#import queue

class Queue:
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
    
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
    
    pq = queue()

    pq.enqueue({
        'Company': 'Wal Mart',
        'Timestamp': '15 Nov, 11.01 AM',
        'Price': 131.10
    })
    pq.enqueue({
        'Company': 'Wal Mart',
        'Timestamp': '15 Nov, 11.02 AM',
        'Price': 132
    })
    pq.enqueue({
        'Company': 'Wal Mart',
        'Timestamp': '15 Nov, 11.03 AM',
        'Price': 135
    })

    print(dequeue())
