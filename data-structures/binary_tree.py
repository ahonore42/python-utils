class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_val=None):
        self.root = TreeNode(root_val) if root_val is not None else None
    
    def insert(self, val):
        """Insert value in level order"""
        if not self.root:
            self.root = TreeNode(val)
            return
        
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if not node.left:
                node.left = TreeNode(val)
                return
            elif not node.right:
                node.right = TreeNode(val)
                return
            else:
                queue.extend([node.left, node.right])
    
    def inorder_traversal(self, node=None):
        """Inorder traversal: left, root, right"""
        if node is None:
            node = self.root
        
        if not node:
            return []
        
        result = []
        result.extend(self.inorder_traversal(node.left))
        result.append(node.val)
        result.extend(self.inorder_traversal(node.right))
        return result
    
    def preorder_traversal(self, node=None):
        """Preorder traversal: root, left, right"""
        if node is None:
            node = self.root
        
        if not node:
            return []
        
        result = [node.val]
        result.extend(self.preorder_traversal(node.left))
        result.extend(self.preorder_traversal(node.right))
        return result
    
    def postorder_traversal(self, node=None):
        """Postorder traversal: left, right, root"""
        if node is None:
            node = self.root
        
        if not node:
            return []
        
        result = []
        result.extend(self.postorder_traversal(node.left))
        result.extend(self.postorder_traversal(node.right))
        result.append(node.val)
        return result
    
    def level_order_traversal(self):
        """Level order traversal (BFS)"""
        if not self.root:
            return []
        
        result = []
        queue = [self.root]
        
        while queue:
            node = queue.pop(0)
            result.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return result
    
    def height(self, node=None):
        """Get height of tree"""
        if node is None:
            node = self.root
        
        if not node:
            return 0
        
        return 1 + max(self.height(node.left), self.height(node.right))
    
    def find(self, val, node=None):
        """Find node with given value"""
        if node is None:
            node = self.root
        
        if not node:
            return None
        
        if node.val == val:
            return node
        
        left_result = self.find(val, node.left)
        if left_result:
            return left_result
        
        return self.find(val, node.right)