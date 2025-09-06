class LinkedListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, val):
        """Add element to end - O(N)"""
        new_node = LinkedListNode(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def find(self, val):
        """Find element - O(N)"""
        current = self.head
        while current:
            if current.val == val:
                return current
            current = current.next
        return None
    
    def reverse(self):
        """Reverse the linked list - O(N)"""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
    def get_middle(self):
        """Get middle node using slow/fast pointers - O(N)"""
        if not self.head:
            return None
        
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def has_cycle(self):
        """Detect cycle using Floyd's algorithm - O(N)"""
        if not self.head:
            return False
        
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False