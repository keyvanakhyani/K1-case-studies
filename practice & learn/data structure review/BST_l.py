

#Binary Search Tree


class treeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self, key = None):
        self.root = None
        if key is not None:
            self.root = treeNode(key)
    
    def insert(self, key):
        if self.root is None:
            self.root = treeNode(key)
        else:
            self._insert(self.root, key)
    
    def _insert(self,current, key):
        if key < current.key:
            if current.left is None:
                current.left = treeNode(key)
            else:
                self._insert(current.left, key)
        else:
            if current.right is None:
                current.right = treeNode(key)
            else:
                self._insert(current.right, key)

    def inorder_traversal(self):
        self.ــinorder_traversal(self.root)

    def ــinorder_traversal(self,root):
        if root:
          self.ــinorder_traversal(root.left)
          print(root.key, end=" ")
          self.ــinorder_traversal(root.right)
        

if __name__ == "__main__":

    tree = BST()
    tree.insert(5)
    tree.insert(15)
    tree.insert(10)
    tree.insert(20)



    tree.inorder_traversal()
    print()

