class CircularQueue:  
    def __init__(self, capacity):  
        """  
        Initializes the circular queue with a fixed capacity.  
          
        :param capacity: Maximum number of elements the queue can hold  
        """  
        self.capacity = capacity  
        self.queue = [None] * capacity  # Fixed-size list  
        self.front = -1  # Points to the front element  
        self.rear = -1   # Points to the last element  
        self.size = 0    # Current number of elements in the queue  
      
    def enqueue(self, item):  
        """  
        Inserts an item into the circular queue.  
          
        :param item: The item to be inserted  
        :return: None  
        """  
        if self.is_full():  
            print("Queue is full. Cannot enqueue.")  
            return  
          
        if self.is_empty():  
            self.front = 0  
          
        self.rear = (self.rear + 1) % self.capacity  
        self.queue[self.rear] = item  
        self.size += 1  
        print(f"Enqueued: {item}")  
      
    def dequeue(self):  
        """  
        Removes and returns the front item from the circular queue.  
          
        :return: The dequeued item, or None if the queue is empty  
        """  
        if self.is_empty():  
            print("Queue is empty. Cannot dequeue.")  
            return None  
          
        item = self.queue[self.front]  
        self.queue[self.front] = None  # Optional: Clear the slot  
        self.front = (self.front + 1) % self.capacity  
        self.size -= 1  
        print(f"Dequeued: {item}")  
          
        if self.is_empty():  
            self.front = -1  
            self.rear = -1  
          
        return item  
      
    def peek(self):  
        """  
        Returns the front item without removing it.  
          
        :return: The front item, or None if the queue is empty  
        """  
        if self.is_empty():  
            print("Queue is empty. Nothing to peek.")  
            return None  
        return self.queue[self.front]  
      
    def is_empty(self):  
        """  
        Checks if the circular queue is empty.  
          
        :return: Boolean indicating if the queue is empty  
        """  
        return self.size == 0  
      
    def is_full(self):  
        """  
        Checks if the circular queue is full.  
          
        :return: Boolean indicating if the queue is full  
        """  
        return self.size == self.capacity  
      
    def __str__(self):  
        """  
        Returns a string representation of the queue.  
        """  
        if self.is_empty():  
            return "CircularQueue is empty."  
          
        index = self.front  
        elements = []  
        for _ in range(self.size):  
            elements.append(str(self.queue[index]))  
            index = (index + 1) % self.capacity  
        return "CircularQueue: " + " <- ".join(elements)  
  
  
def circular_queue_example():  
    print("=== Circular Queue Example ===")  
    capacity = 5  
    cq = CircularQueue(capacity)  
      
    print("\nInitial Queue State:")  
    print(cq)  
      
    # Enqueue elements  
    print("\nEnqueuing elements:")  
    cq.enqueue(10)  
    print(cq)  
    cq.enqueue(20)  
    print(cq)  
    cq.enqueue(30)  
    print(cq)  
    cq.enqueue(40)  
    print(cq)  
    cq.enqueue(50)  # Should fill the queue  
    print(cq)  
    cq.enqueue(60)  # Should indicate that the queue is full  
      
    # Dequeue elements  
    print("\nDequeuing elements:")  
    cq.dequeue()  
    print(cq)  
    cq.dequeue()  
    print(cq)  
      
    # Enqueue more elements to test wrap-around  
    print("\nEnqueuing more elements after dequeue:")  
    cq.enqueue(60)  
    print(cq)  
    cq.enqueue(70)  
    print(cq)  
      
    # Peek at the front element  
    print("\nPeeking at the front element:")  
    front_item = cq.peek()  
    print(f"Front item: {front_item}")  
      
    # Dequeue remaining elements  
    print("\nDequeuing remaining elements:")  
    while not cq.is_empty():  
        cq.dequeue()  
        print(cq)  
      
    # Attempt to dequeue from empty queue  
    print("\nAttempting to dequeue from an empty queue:")  
    cq.dequeue()  
  
  
if __name__ == "__main__":  
    circular_queue_example()  
