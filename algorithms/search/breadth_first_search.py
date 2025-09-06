from collections import deque

def bfs_by_queue(root, target):
    queue = deque([root]) # at least one element in the queue to kick start bfs
    while len(queue) > 0: # as long as there is an element in the queue
        node = queue.popleft() # dequeue
        for child in node.children: # enqueue children
            if child.val == target: # early return if problem condition met
                return child # FOUND
            queue.append(child)
    return None # NOT_FOUND