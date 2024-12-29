class Node:  
    """  
    Node class for Separate Chaining in HashMap.  
    """  
    def __init__(self, key, value):  
        self.key = key  
        self.value = value  
        self.next = None  
  
  
class HashMapChaining:  
    """  
    Hash Map implementation using Separate Chaining for collision handling.  
    """  
    def __init__(self, initial_capacity=8):  
        self.capacity = initial_capacity  # Size of the hash table  
        self.size = 0  # Number of key-value pairs in the hash map  
        self.buckets = [None] * self.capacity  # Initialize buckets  
      
    def hash_function(self, key):  
        """  
        Computes the hash index for a given key.  
        """  
        return hash(key) % self.capacity  
      
    def put(self, key, value):  
        """  
        Inserts a key-value pair into the hash map.  
        If the key already exists, updates its value.  
        """  
        index = self.hash_function(key)  
        print(f"Putting key={key}, value={value} at index={index}")  
        head = self.buckets[index]  
        current = head  
      
        while current:  
            if current.key == key:  
                print(f"Key {key} found, updating value to {value}")  
                current.value = value  
                return  
            current = current.next  
      
        new_node = Node(key, value)  
        new_node.next = head  
        self.buckets[index] = new_node  
        self.size += 1  
        print(f"Inserted key={key}, value={value} at index={index}")  
      
        if self.size / self.capacity > 0.7:  
            print("Load factor exceeded 0.7, resizing hash map.")  
            self.resize()  
      
    def get(self, key):  
        """  
        Retrieves the value associated with the given key.  
        Returns None if the key is not found.  
        """  
        index = self.hash_function(key)  
        print(f"Getting value for key={key} from index={index}")  
        current = self.buckets[index]  
      
        while current:  
            if current.key == key:  
                print(f"Key {key} found, value={current.value}")  
                return current.value  
            current = current.next  
      
        print(f"Key {key} not found.")  
        return None  
      
    def remove(self, key):  
        """  
        Removes the key-value pair associated with the given key.  
        """  
        index = self.hash_function(key)  
        print(f"Removing key={key} from index={index}")  
        current = self.buckets[index]  
        prev = None  
      
        while current:  
            if current.key == key:  
                if prev:  
                    prev.next = current.next  
                else:  
                    self.buckets[index] = current.next  
                self.size -= 1  
                print(f"Key {key} removed.")  
                return  
            prev = current  
            current = current.next  
      
        print(f"Key {key} not found, cannot remove.")  
      
    def resize(self):  
        """  
        Resizes the hash table when load factor exceeds threshold.  
        """  
        old_buckets = self.buckets  
        self.capacity *= 2  
        self.buckets = [None] * self.capacity  
        self.size = 0  
        print(f"Resizing hash map to capacity={self.capacity}")  
      
        for head in old_buckets:  
            current = head  
            while current:  
                self.put(current.key, current.value)  
                current = current.next  
      
    def __str__(self):  
        """  
        Returns a string representation of the hash map.  
        """  
        elements = []  
        for i, head in enumerate(self.buckets):  
            current = head  
            chain = []  
            while current:  
                chain.append(f"{current.key}: {current.value}")  
                current = current.next  
            if chain:  
                elements.append(f"Bucket {i}: " + " -> ".join(chain))  
        return "\n".join(elements)  
  
  
class HashMapOpenAddressing:  
    """  
    Hash Map implementation using Open Addressing with Double Hashing for collision handling.  
    """  
    def __init__(self, initial_capacity=8):  
        self.capacity = initial_capacity  # Size of the hash table  
        self.size = 0  # Number of key-value pairs in the hash map  
        self.keys = [None] * self.capacity  
        self.values = [None] * self.capacity  
        self.tombstone = object()  # Unique object to represent deleted entries  
      
    def h1(self, key):  
        """  
        Primary hash function.  
        """  
        return hash(key) % self.capacity  
      
    def h2(self, key):  
        """  
        Secondary hash function for double hashing.  
        Ensures step size is never zero and relatively prime to the table size.  
        """  
        return 1 + (hash(key) % (self.capacity - 1))  
      
    def put(self, key, value):  
        """  
        Inserts a key-value pair into the hash map.  
        If the key already exists, updates its value.  
        """  
        if self.size / self.capacity > 0.7:  
            print("Load factor exceeded 0.7, resizing hash map.")  
            self.resize()  
      
        index = self.h1(key)  
        step = self.h2(key)  
        initial_index = index  
        first_tombstone = -1  
      
        while self.keys[index] is not None:  
            if self.keys[index] is self.tombstone:  
                if first_tombstone == -1:  
                    first_tombstone = index  
            elif self.keys[index] == key:  
                print(f"Key {key} found at index={index}, updating value to {value}")  
                self.values[index] = value  
                return  
            index = (index + step) % self.capacity  
            if index == initial_index:  
                raise Exception("HashMap is full!")  
      
        if first_tombstone != -1:  
            index = first_tombstone  
      
        print(f"Inserting key={key}, value={value} at index={index}")  
        self.keys[index] = key  
        self.values[index] = value  
        self.size += 1  
      
    def get(self, key):  
        """  
        Retrieves the value associated with the given key.  
        Returns None if the key is not found.  
        """  
        index = self.h1(key)  
        step = self.h2(key)  
        initial_index = index  
      
        while self.keys[index] is not None:  
            if self.keys[index] != self.tombstone and self.keys[index] == key:  
                print(f"Key {key} found at index={index}, value={self.values[index]}")  
                return self.values[index]  
            index = (index + step) % self.capacity  
            if index == initial_index:  
                break  
      
        print(f"Key {key} not found.")  
        return None  
      
    def remove(self, key):  
        """  
        Removes the key-value pair associated with the given key.  
        """  
        index = self.h1(key)  
        step = self.h2(key)  
        initial_index = index  
      
        while self.keys[index] is not None:  
            if self.keys[index] != self.tombstone and self.keys[index] == key:  
                print(f"Removing key={key} from index={index}")  
                self.keys[index] = self.tombstone  
                self.values[index] = None  
                self.size -= 1  
                return  
            index = (index + step) % self.capacity  
            if index == initial_index:  
                break  
      
        print(f"Key {key} not found, cannot remove.")  
      
    def resize(self):  
        """  
        Resizes the hash table when load factor exceeds threshold.  
        """  
        old_keys = self.keys  
        old_values = self.values  
        old_capacity = self.capacity  
        self.capacity *= 2  
        self.keys = [None] * self.capacity  
        self.values = [None] * self.capacity  
        self.size = 0  
        print(f"Resizing hash map to capacity={self.capacity}")  
      
        for i in range(old_capacity):  
            if old_keys[i] is not None and old_keys[i] != self.tombstone:  
                self.put(old_keys[i], old_values[i])  
      
    def __str__(self):  
        """  
        Returns a string representation of the hash map.  
        """  
        elements = []  
        for i in range(self.capacity):  
            if self.keys[i] is not None and self.keys[i] != self.tombstone:  
                elements.append(f"Index {i}: {self.keys[i]} => {self.values[i]}")  
        return "\n".join(elements)  
  
  
def separate_chaining_example():  
    print("=== HashMap with Separate Chaining Example ===")  
    hash_map = HashMapChaining()  
      
    # Insert elements  
    print("\nInserting key-value pairs:")  
    elements_to_insert = [("apple", 1), ("banana", 2), ("grape", 3), ("orange", 4), ("melon", 5)]  
    for key, value in elements_to_insert:  
        hash_map.put(key, value)  
        print(hash_map)  
        print("-" * 40)  
      
    # Search for elements  
    print("\nSearching for keys:")  
    search_keys = ["apple", "cherry"]  
    for key in search_keys:  
        value = hash_map.get(key)  
        if value is not None:  
            print(f"Found key '{key}' with value {value}.")  
        else:  
            print(f"Key '{key}' not found.")  
      
    # Remove elements  
    print("\nRemoving keys:")  
    remove_keys = ["banana", "grape"]  
    for key in remove_keys:  
        hash_map.remove(key)  
        print(hash_map)  
        print("-" * 40)  
      
    # Final state  
    print("\nFinal HashMap:")  
    print(hash_map)  
  
  
def open_addressing_example():  
    print("\n=== HashMap with Open Addressing (Double Hashing) Example ===")  
    hash_map = HashMapOpenAddressing()  
      
    # Insert elements  
    print("\nInserting key-value pairs:")  
    elements_to_insert = [("apple", 1), ("banana", 2), ("grape", 3), ("orange", 4), ("melon", 5)]  
    for key, value in elements_to_insert:  
        hash_map.put(key, value)  
        print(hash_map)  
        print("-" * 40)  
      
    # Search for elements  
    print("\nSearching for keys:")  
    search_keys = ["apple", "cherry"]  
    for key in search_keys:  
        value = hash_map.get(key)  
        if value is not None:  
            print(f"Found key '{key}' with value {value}.")  
        else:  
            print(f"Key '{key}' not found.")  
      
    # Remove elements  
    print("\nRemoving keys:")  
    remove_keys = ["banana", "grape"]  
    for key in remove_keys:  
        hash_map.remove(key)  
        print(hash_map)  
        print("-" * 40)  
      
    # Final state  
    print("\nFinal HashMap:")  
    print(hash_map)  
  
  
if __name__ == "__main__":  
    separate_chaining_example()  
    open_addressing_example()  
