class NaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

class NaryTree:
    def __init__(self, root_val=None):
        self.root = NaryTreeNode(root_val) if root_val is not None else None
    
    def add_child(self, parent_val, child_val):
        """Add child to parent node"""
        parent = self.find(parent_val)
        if parent:
            parent.children.append(NaryTreeNode(child_val))
            return True
        return False
    
    def find(self, val, node=None):
        """Find node with given value"""
        if node is None:
            node = self.root
        
        if not node:
            return None
        
        if node.val == val:
            return node
        
        for child in node.children:
            result = self.find(val, child)
            if result:
                return result
        
        return None
    
    def preorder_traversal(self, node=None):
        """Preorder traversal"""
        if node is None:
            node = self.root
        
        if not node:
            return []
        
        result = [node.val]
        for child in node.children:
            result.extend(self.preorder_traversal(child))
        
        return result
    
    def level_order_traversal(self):
        """Level order traversal"""
        if not self.root:
            return []
        
        result = []
        queue = [self.root]
        
        while queue:
            node = queue.pop(0)
            result.append(node.val)
            queue.extend(node.children)
        
        return result