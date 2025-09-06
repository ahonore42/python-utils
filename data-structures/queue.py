class Queue:
    def __init__(self):
        self._items = []
    
    def enqueue(self, item):
        """Add item to rear of queue - O(1)"""
        self._items.append(item)
    
    def dequeue(self):
        """Remove item from front of queue - O(1)"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._items.pop(0)
    
    def peek(self):
        """Get front item without removing - O(1)"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._items[0]
    
    def is_empty(self):
        """Check if queue is empty - O(1)"""
        return len(self._items) == 0
    
    def size(self):
        """Get queue size - O(1)"""
        return len(self._items)