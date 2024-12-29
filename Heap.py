class MinHeap:  
    def __init__(self):  
        self.heap = []  
  
    def insert(self, key):  
        """  
        Inserts a new key into the heap.  
        """  
        self.heap.append(key)  
        print(f"Inserted {key}: {self.heap}")  
        self._heapify_up(len(self.heap) - 1)  
  
    def extract_min(self):  
        """  
        Removes and returns the smallest element from the heap.  
        """  
        if not self.heap:  
            raise IndexError("extract_min from an empty heap")  
  
        min_elem = self.heap[0]  
        last_elem = self.heap.pop()  
  
        if self.heap:  
            self.heap[0] = last_elem  
            print(f"Moved {last_elem} to root")  
            self._heapify_down(0)  
  
        print(f"Extracted min {min_elem}: {self.heap}")  
        return min_elem  
  
    def peek_min(self):  
        """  
        Returns the smallest element without removing it.  
        """  
        if not self.heap:  
            raise IndexError("peek_min from an empty heap")  
        return self.heap[0]  
  
    def delete(self, key):  
        """  
        Removes a specific key from the heap.  
        """  
        try:  
            index = self.heap.index(key)  
        except ValueError:  
            print(f"Key {key} not found in the heap.")  
            return  
  
        last_elem = self.heap.pop()  
        if index < len(self.heap):  
            self.heap[index] = last_elem  
            print(f"Moved {last_elem} to index {index}")  
            # Heapify at the index where we placed the last element  
            self._heapify_down(index)  
            self._heapify_up(index)  
        print(f"Deleted key {key}: {self.heap}")  
  
    def _heapify_up(self, index):  
        """  
        Heapifies the element at index upwards to maintain heap property.  
        """  
        parent_index = (index - 1) // 2  
        if index > 0 and self.heap[index] < self.heap[parent_index]:  
            # Swap the current element with its parent  
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]  
            print(f"Swapped {self.heap[index]} with parent {self.heap[parent_index]}")  
            self._heapify_up(parent_index)  
  
    def _heapify_down(self, index):  
        """  
        Heapifies the element at index downwards to maintain heap property.  
        """  
        smallest = index  
        left = 2 * index + 1  
        right = 2 * index + 2  
  
        # Check if left child exists and is smaller than current smallest  
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:  
            smallest = left  
  
        # Check if right child exists and is smaller than current smallest  
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:  
            smallest = right  
  
        if smallest != index:  
            # Swap the current element with the smallest child  
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]  
            print(f"Swapped {self.heap[index]} with child {self.heap[smallest]}")  
            self._heapify_down(smallest)  
  
    def build_heap(self, elements):  
        """  
        Builds a heap from a list of elements.  
        """  
        self.heap = elements[:]  
        start_idx = len(self.heap) // 2 - 1  # Start from the last non-leaf node  
        for i in range(start_idx, -1, -1):  
            self._heapify_down(i)  
        print(f"Built MinHeap: {self.heap}")  
  
    def __str__(self):  
        """  
        Returns the string representation of the heap.  
        """  
        return str(self.heap)  
  
  
class MaxHeap:  
    def __init__(self):  
        self.heap = []  
  
    def insert(self, key):  
        """  
        Inserts a new key into the heap.  
        """  
        self.heap.append(key)  
        print(f"Inserted {key}: {self.heap}")  
        self._heapify_up(len(self.heap) - 1)  
  
    def extract_max(self):  
        """  
        Removes and returns the largest element from the heap.  
        """  
        if not self.heap:  
            raise IndexError("extract_max from an empty heap")  
  
        max_elem = self.heap[0]  
        last_elem = self.heap.pop()  
  
        if self.heap:  
            self.heap[0] = last_elem  
            print(f"Moved {last_elem} to root")  
            self._heapify_down(0)  
  
        print(f"Extracted max {max_elem}: {self.heap}")  
        return max_elem  
  
    def peek_max(self):  
        """  
        Returns the largest element without removing it.  
        """  
        if not self.heap:  
            raise IndexError("peek_max from an empty heap")  
        return self.heap[0]  
  
    def delete(self, key):  
        """  
        Removes a specific key from the heap.  
        """  
        try:  
            index = self.heap.index(key)  
        except ValueError:  
            print(f"Key {key} not found in the heap.")  
            return  
  
        last_elem = self.heap.pop()  
        if index < len(self.heap):  
            self.heap[index] = last_elem  
            print(f"Moved {last_elem} to index {index}")  
            # Heapify at the index where we placed the last element  
            self._heapify_down(index)  
            self._heapify_up(index)  
        print(f"Deleted key {key}: {self.heap}")  
  
    def _heapify_up(self, index):  
        """  
        Heapifies the element at index upwards to maintain heap property.  
        """  
        parent_index = (index - 1) // 2  
        if index > 0 and self.heap[index] > self.heap[parent_index]:  
            # Swap the current element with its parent  
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]  
            print(f"Swapped {self.heap[index]} with parent {self.heap[parent_index]}")  
            self._heapify_up(parent_index)  
  
    def _heapify_down(self, index):  
        """  
        Heapifies the element at index downwards to maintain heap property.  
        """  
        largest = index  
        left = 2 * index + 1  
        right = 2 * index + 2  
  
        # Check if left child exists and is larger than current largest  
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:  
            largest = left  
  
        # Check if right child exists and is larger than current largest  
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:  
            largest = right  
  
        if largest != index:  
            # Swap the current element with the largest child  
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]  
            print(f"Swapped {self.heap[index]} with child {self.heap[largest]}")  
            self._heapify_down(largest)  
  
    def build_heap(self, elements):  
        """  
        Builds a heap from a list of elements.  
        """  
        self.heap = elements[:]  
        start_idx = len(self.heap) // 2 - 1  # Start from the last non-leaf node  
        for i in range(start_idx, -1, -1):  
            self._heapify_down(i)  
        print(f"Built MaxHeap: {self.heap}")  
  
    def __str__(self):  
        """  
        Returns the string representation of the heap.  
        """  
        return str(self.heap)  
  
  
if __name__ == "__main__":  
    # Example usage for MinHeap  
    print("=== Min Heap Example ===")  
    min_heap = MinHeap()  
  
    # Insert elements  
    print("\nInserting elements:")  
    elements = [15, 10, 20, 17, 8]  
    for elem in elements:  
        min_heap.insert(elem)  
  
    print(f"\nCurrent Min Heap: {min_heap}")  
  
    # Peek min  
    print(f"\nPeek Min: {min_heap.peek_min()}")  
  
    # Extract min  
    print("\nExtracting min:")  
    min_heap.extract_min()  
    print(f"Min Heap after extraction: {min_heap}")  
  
    # Delete a specific key  
    print("\nDeleting key 17:")  
    min_heap.delete(17)  
    print(f"Min Heap after deletion: {min_heap}")  
  
    # Build heap from a list  
    print("\nBuilding heap from [3, 19, 1, 14, 8, 7]:")  
    min_heap.build_heap([3, 19, 1, 14, 8, 7])  
    print(f"Final Min Heap: {min_heap}")  
  
    # Example usage for MaxHeap  
    print("\n=== Max Heap Example ===")  
    max_heap = MaxHeap()  
  
    # Insert elements  
    print("\nInserting elements:")  
    elements = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]  
    for elem in elements:  
        max_heap.insert(elem)  
  
    print(f"\nCurrent Max Heap: {max_heap}")  
  
    # Peek max  
    print(f"\nPeek Max: {max_heap.peek_max()}")  
  
    # Extract max  
    print("\nExtracting max:")  
    max_heap.extract_max()  
    print(f"Max Heap after extraction: {max_heap}")  
  
    # Delete a specific key  
    print("\nDeleting key 14:")  
    max_heap.delete(14)  
    print(f"Max Heap after deletion: {max_heap}")  
  
    # Build heap from a list  
    print("\nBuilding heap from [5, 3, 17, 10, 84, 19, 6, 22, 9]:")  
    max_heap.build_heap([5, 3, 17, 10, 84, 19, 6, 22, 9])  
    print(f"Final Max Heap: {max_heap}")  
