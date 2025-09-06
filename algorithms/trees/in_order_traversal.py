# In-order traversal visits the left branch first, then the current node, 
# and finally the right branch.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def in_order_traversal(root: Node) -> None:
    if root is not None:
        in_order_traversal(root.left)
        print(root.val)
        in_order_traversal(root.right)

# this function builds a tree from input; you don't have to modify it
def build_tree(nodes, f):
    val = next(nodes)
    if val == "x":
        return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == "__main__":
    root = build_tree(iter(input().split()), int)
    in_order_traversal(root)
