class BPlusTreeNode:  
    def __init__(self, t, leaf=False):  
        self.t = t  # Minimum degree  
        self.keys = []  # List of keys  
        self.children = []  # List of children nodes  
        self.leaf = leaf  # Is true when node is leaf. Otherwise false.  
        self.next = None  # Pointer to next leaf node  
  
    def search(self, key):  
        i = 0  
        while i < len(self.keys) and key > self.keys[i]:  
            i += 1  
  
        if self.leaf:  
            return key in self.keys  
  
        return self.children[i].search(key)  
  
    def insert_non_full(self, key):  
        i = len(self.keys) - 1  
  
        if self.leaf:  
            # Insert the new key at the correct position  
            self.keys.append(None)  
            while i >= 0 and key < self.keys[i]:  
                self.keys[i + 1] = self.keys[i]  
                i -= 1  
            self.keys[i + 1] = key  
            print(f"Inserted key {key} in leaf node with keys {self.keys}")  
        else:  
            while i >= 0 and key < self.keys[i]:  
                i -= 1  
            i += 1  
            if len(self.children[i].keys) == 2 * self.t - 1:  
                self.split_child(i, self.children[i])  
                if key > self.keys[i]:  
                    i += 1  
            self.children[i].insert_non_full(key)  
  
    def split_child(self, i, y):  
        t = self.t  
        z = BPlusTreeNode(t, y.leaf)  
        # For B+ Trees, internal node promotions differ  
        z.keys = y.keys[t:]  # Right half keys  
        y.keys = y.keys[:t]  # Left half keys (inclusive to ensure all data is in leaves)  
  
        if not y.leaf:  
            z.children = y.children[t:]  
            y.children = y.children[:t]  
  
        self.children.insert(i + 1, z)  
        self.keys.insert(i, z.keys[0])  # Promote the first key of the new node  
  
        if y.leaf:  
            z.next = y.next  
            y.next = z  
  
        print(f"Split child node. Parent keys now {self.keys}")  
        print(f"Left child keys {y.keys}, Right child keys {z.keys}")  
  
    def traverse(self):  
        if self.leaf:  
            return self.keys  
        return self.children[0].traverse()  


if __name__ == "__main__":  
    # B+ Tree Example  
    print("\n=== B+ Tree Example ===")  
    t = 3  # Minimum degree  
    bplustree = BPlusTreeNode(t, leaf=True)  
  
    keys_to_insert = [10, 20, 5, 6, 12, 30, 7, 17]  
  
    for key in keys_to_insert:  
        if len(bplustree.keys) == (2 * t) - 1:  
            new_root = BPlusTreeNode(t, leaf=False)  
            new_root.children.append(bplustree)  
            new_root.split_child(0, bplustree)  
            i = 0  
            if new_root.keys[0] < key:  
                i += 1  
            new_root.children[i].insert_non_full(key)  
            bplustree = new_root  
        else:  
            bplustree.insert_non_full(key)  
  
    print(f"Traversal of B+ Tree: {bplustree.traverse()}")  
  
    # Search for keys  
    search_keys = [6, 15]  
    for key in search_keys:  
        result = bplustree.search(key)  
        if result:  
            print(f"Key {key} found in the B+ Tree.")  
        else:  
            print(f"Key {key} not found in the B+ Tree.")  
