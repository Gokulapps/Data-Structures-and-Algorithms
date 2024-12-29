class BTreeNode:  
    def __init__(self, t, leaf=False):  
        self.t = t  # Minimum degree  
        self.keys = []  # List of keys  
        self.children = []  # List of child nodes  
        self.leaf = leaf  # Is true when node is leaf. Otherwise false.  
  
    def search(self, key):  
        i = 0  
        while i < len(self.keys) and key > self.keys[i]:  
            i += 1  
  
        if i < len(self.keys) and self.keys[i] == key:  
            return self, i  
  
        if self.leaf:  
            return None  
  
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
            # If the child is full, split it  
            if len(self.children[i].keys) == 2 * self.t - 1:  
                self.split_child(i, self.children[i])  
                if key > self.keys[i]:  
                    i += 1  
            self.children[i].insert_non_full(key)  
  
    def split_child(self, i, y):  
        t = self.t  
        z = BTreeNode(t, y.leaf)  
        z.keys = y.keys[t:]  # Right half keys  
        y.keys = y.keys[:t - 1]  # Left half keys  
  
        if not y.leaf:  
            z.children = y.children[t:]  # Right half children  
            y.children = y.children[:t]  
  
        self.children.insert(i + 1, z)  
        self.keys.insert(i, y.keys[t - 1])  
  
        print(f"Split child node. Parent keys now {self.keys}")  
        print(f"Left child keys {y.keys}, Right child keys {z.keys}")  
  
    def traverse(self):  
        result = []  
        for i in range(len(self.keys)):  
            if not self.leaf:  
                result.extend(self.children[i].traverse())  
            result.append(self.keys[i])  
        if not self.leaf:  
            result.extend(self.children[-1].traverse())  
        return result  

if __name__ == "__main__":  
    # B-Tree Example  
    print("=== B-Tree Example ===")  
    t = 3  # Minimum degree  
    btree = BTreeNode(t, leaf=True)  
  
    keys_to_insert = [10, 20, 5, 6, 12, 30, 7, 17]  
  
    for key in keys_to_insert:  
        if len(btree.keys) == (2 * t) - 1:  
            new_root = BTreeNode(t, leaf=False)  
            new_root.children.append(btree)  
            new_root.split_child(0, btree)  
            i = 0  
            if new_root.keys[0] < key:  
                i += 1  
            new_root.children[i].insert_non_full(key)  
            btree = new_root  
        else:  
            btree.insert_non_full(key)  
  
    print(f"Traversal of B-Tree: {btree.traverse()}")  
  
    # Search for keys  
    search_keys = [6, 15]  
    for key in search_keys:  
        result = btree.search(key)  
        if result:  
            print(f"Key {key} found in the B-Tree.")  
        else:  
            print(f"Key {key} not found in the B-Tree.")  
