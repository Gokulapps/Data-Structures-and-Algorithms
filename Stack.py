class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*max_size
        self.__top=-1
    def get_max_size(self):
        return self.__max_size
    def is_full(self):
        if(self.__top==self.__max_size-1):
            return True
        return False
    def push(self,data):
        if(self.is_full()):
            print("The Stack is Full")
        else:
            self.__top+=1
            self.__elements[self.__top]=data
    def is_empty(self):
        if(self.__top==-1):
            return True
        return False
    def pop(self):
        if(self.is_empty()):
            print("The Stack is Empty")
        else:
            data=self.__elements[self.__top]
            self.__top -= 1
            return data
    def display_stack(self):
        if(self.is_empty()):
            print("The Stack is Empty")
        else:
            for index in range(self.__top+1):
                print(self.__elements[index])

stack1=Stack(10)
stack1.push("Tom")
stack1.push("And")
stack1.push("Jerry")
stack1.push("Show")
stack1.push("Error")
stack1.display_stack()
print("Poped Element:",stack1.pop())
stack1.display_stack()
print("Max Size:",stack1.get_max_size())
