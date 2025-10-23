from BST_l import treeNode

class AVLNode(treeNode):
    def __init__(self, value):
        super().__init__(value)
        self.height = 1
    
class AVLTree:

    def get_height(self,node) -> int:
        """Get height of node 
            return int 
        """
        return node.height if node else 0
    
    def get_balance(self, node):
        """Get balance factor of node"""
        return self.get_height(node.left) - self.get_height(node.right) if node else 0
    
    def update_height(self, node):
        """Update height of node"""
        if node:
            node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def rotate_right(self, y):
        """Right rotation"""
        print(f"Right rotation {y.key}")
        x = y.left
        T = x.right
        
        x.right = y
        y.left = T
        
        self.update_height(y)
        self.update_height(x)
        
        return x
    
    def rotate_left(self, x):
        """Left rotation"""
        print(f"Left rotation {x.key}")
        y = x.right
        T = y.left
        
        y.left = x
        x.right = T
        
        self.update_height(x)
        self.update_height(y)
        
        return y
    def insert(self, root, key):
        """Insert a key into AVL tree"""
        # Step 1: Normal BST insertion
        if not root:
            return AVLNode(key)
        
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            # Duplicate keys not allowed
            return root
        
        # Step 2: Update height
        self.update_height(root)
        
        # Step 3: Get balance factor
        balance = self.get_balance(root)
        
        # Step 4: Balance the tree
        # Left Left Case
        if balance > 1 and key < root.left.key:
            print(f"Left Left Case {key},{root.key}")
            return self.rotate_right(root)
        
        # Right Right Case
        if balance < -1 and key > root.right.key:
            print(f"Right Right Case {key},{root.key}")
            return self.rotate_left(root)
        
        # Left Right Case
        if balance > 1 and key > root.left.key:
            print(f"Left Right Case {key},{root.key}")
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        
        # Right Left Case
        if balance < -1 and key < root.right.key:
            print(f"Right Left Case {key},{root.key}")
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
        
        return root
    
    def get_min_value_node(self, node):
        """Get node with minimum value"""
        current = node
        while current.left:
            current = current.left
        return current
    
    def search(self, root, key):
        """Search for a key in AVL tree"""
        if not root:
            return None
        
        if key == root.key:
            return root
        elif key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)
    
    def search_iterative(self, root, key):
        """Search for a key iteratively (more efficient)"""
        current = root
        while current:
            if key == current.key:
                return current
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None
    
    def delete(self, root, key):
        """Delete a key from AVL tree"""
        # Step 1: Normal BST deletion
        if not root:
            return root
        
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Node with one child or no child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # Node with two children
            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        
        # If tree had only one node
        if not root:
            return root
        
        # Step 2: Update height
        self.update_height(root)
        
        # Step 3: Get balance factor
        balance = self.get_balance(root)
        
        # Step 4: Balance the tree
        # Left Left Case
        if balance > 1 and self.get_balance(root.left) >= 0:
            print(f"Left Left Case {key},{root.key}")
            return self.rotate_right(root)
        
        # Left Right Case
        if balance > 1 and self.get_balance(root.left) < 0:
            print(f"Left Right Case {key},{root.key}")
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        
        # Right Right Case
        if balance < -1 and self.get_balance(root.right) <= 0:
            print(f"Right Right Case {key},{root.key}")
            return self.rotate_left(root)
        
        # Right Left Case
        if balance < -1 and self.get_balance(root.right) > 0:
            print(f"Right Left Case {key},{root.key}")
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
        
        return root
    
    def print_inorder(self, root):
        """Print tree in inorder (sorted)"""
        if root:
            self.print_inorder(root.left)
            print(root.key, end=' ')
            self.print_inorder(root.right)
    
    def print_preorder(self, root):
        """Print tree in preorder"""
        if root:
            print(root.key, end=' ')
            self.print_preorder(root.left)
            self.print_preorder(root.right)
    
    def print_tree(self, root, level=0, prefix="Root: "):
        """Print tree structure visually"""
        if root:
            print(" " * (level * 4) + prefix + str(root.key) + f" (h={root.height}, b={self.get_balance(root)})")
            if root.left or root.right:
                if root.left:
                    self.print_tree(root.left, level + 1, "L--- ")
                else:
                    print(" " * ((level + 1) * 4) + "L--- None")
                if root.right:
                    self.print_tree(root.right, level + 1, "R--- ")
                else:
                    print(" " * ((level + 1) * 4) + "R--- None")



if __name__ == "__main__":
    avl = AVLTree()

    root = avl.insert(None, 6)
    print(root.key)
    root = avl.insert(root, 3)
    root = avl.insert(root, 1)
    root = avl.insert(root, 10)
    root = avl.insert(root, 8)
    avl.print_tree(root)
    
