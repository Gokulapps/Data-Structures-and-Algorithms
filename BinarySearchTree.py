class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert a node
    def insert(self, key, current=None):
        if self.root is None:
            self.root = Node(key)
        else:
            if current is None:
                current = self.root

            if key < current.key:
                if current.left is None:
                    current.left = Node(key)
                else:
                    self.insert(key, current.left)
            elif key > current.key:
                if current.right is None:
                    current.right = Node(key)
                else:
                    self.insert(key, current.right)

    # Search for a node
    def search(self, key, current=None):
        if current is None:
            current = self.root

        while current is not None:
            if current.key == key:
                return current
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None

    # Delete a node
    def delete(self, key, current=None):
        if current is None:
            current = self.root

        if current is None:
            return current

        if key < current.key:
            current.left = self.delete(key, current.left)
        elif key > current.key:
            current.right = self.delete(key, current.right)
        else:
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left

            # Node with two children: Get the inorder successor
            successor = self._min_value_node(current.right)
            current.key = successor.key
            current.right = self.delete(successor.key, current.right)

        if current == self.root:
            self.root = current
        return current

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Breadth-First Search (BFS)
    def bfs(self):
        if self.root is None:
            return []

        queue = [self.root]
        result = []
        while queue:
            current = queue.pop(0)
            result.append(current.key)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result

    # Depth-First Search: In-Order
    def inorder(self, current=None, result=None):
        if result is None:
            result = []
        if current is None:
            current = self.root

        if current:
            self.inorder(current.left, result)
            result.append(current.key)
            self.inorder(current.right, result)
        return result

    # Depth-First Search: Pre-Order
    def preorder(self, current=None, result=None):
        if result is None:
            result = []
        if current is None:
            current = self.root

        if current:
            result.append(current.key)
            self.preorder(current.left, result)
            self.preorder(current.right, result)
        return result

    # Depth-First Search: Post-Order
    def postorder(self, current=None, result=None):
        if result is None:
            result = []
        if current is None:
            current = self.root

        if current:
            self.postorder(current.left, result)
            self.postorder(current.right, result)
            result.append(current.key)
        return result

# Example Usage
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)

    print("BFS:", bst.bfs())
    print("In-Order:", bst.inorder())
    print("Pre-Order:", bst.preorder())
    print("Post-Order:", bst.postorder())

    bst.delete(20)
    print("After deleting 20 (In-Order):", bst.inorder())

    bst.delete(30)
    print("After deleting 30 (In-Order):", bst.inorder())

    bst.delete(50)
    print("After deleting 50 (In-Order):", bst.inorder())
