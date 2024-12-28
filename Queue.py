class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*max_size
        self.__front=0
        self.__rear=-1
    def get_max_size(self):
        return self.__max_size
    def is_full(self):
        if(self.__rear==self.__max_size-1):
            return True
        return False
    def enqueue(self,data):
        if(self.is_full()):
            print("The Stack is Full")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data
    def is_empty(self):
        if(self.__rear==-1):
            return True
        return False
    def dequeue(self):
        if(self.is_empty()):
            print("The Stack is Empty")
        else:
            data=self.__elements[self.__front]
            self.__front += 1
            return data
    def display_queue(self):
        if(self.is_empty()):
            print("The Stack is Empty")
        else:
            for index in range(self.__front,self.__rear+1):
                print(self.__elements[index])

queue1=Queue(10)
queue1.enqueue("Error")
queue1.enqueue("Tom")
queue1.enqueue("And")
queue1.enqueue("Jerry")
queue1.enqueue("Show")
queue1.display_queue()
print("Poped Element:",queue1.dequeue())
queue1.display_queue()
print("Max Size:",queue1.get_max_size())
