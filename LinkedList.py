class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None
    def set_data(self,data):
        self.__data=data
    def get_data(self):
        return self.__data
    def set_next(self,newnode):
        self.__next=newnode
    def get_next(self):
        return self.__next

class Linkedlist:
    def __init__(self):
        self.__head=None
        self.__tail=None
    def length(self):
        len=0
        if(self.__head==None):
            return len
        else:
            lastnode=self.__head
            while lastnode is not None:
                len+=1
                lastnode=lastnode.get_next()
            return len
    def addNodeLast(self,data):
        newnode=Node(data)
        if(self.__head is None):
            self.__head=self.__tail=newnode
        else:
            self.__tail.set_next(newnode)
            self.__tail=newnode
    def addNodeAt(self, position, data):
        newnode = Node(data)
        p=0
        if(position == 0):
            self.addNodeFirst(data)
            return
        elif (position == self.() - 1):
            self.addNodeLast(data)
        elif(position < 0 or position > self.() - 1):
            print("Invalid Position")
            return
        lastnode = self.__head
        while True:
            if (position == p):
                prevnode.set_next(newnode)
                newnode.set_next(lastnode)
                return
            else:
                prevnode=lastnode
                lastnode=lastnode.get_next()
                p+=1
    def addNodeFirst(self,data):
        newnode=Node(data)
        if self.__head is None:
            self.__head=self.__tail=newnode
        else:
            temp=self.__head
            self.__head=newnode
            self.__head.set_next(temp)
    def deleteNodeLast(self):
        if(self.__head is None):
            print("The Linkedlist is Empty")
        elif(self.__head==self.__tail):
            self.__head=self.__tail=None
        else:
            lastnode=self.__head
            while lastnode.get_next() is not None:
                prevnode=lastnode
                lastnode=lastnode.get_next()
            prevnode.set_next(None)
    def deleteNodeAt(self,position):
        if(position<0 or position>self.()-1):
            print("Invalid Position")
            return
        elif(position==0):
            self.deleteNodeFirst()
            return
        elif(position==self.()):
            self.deleteNodeLast()
            return
        lastnode=self.__head
        p=0
        while lastnode is not None:
            if p==position:
                prevnode.set_next(lastnode.get_next())
                lastnode.set_next(None)
                return
            else:
                prevnode=lastnode
                lastnode=lastnode.get_next()
                p+=1
    def deleteNodeFirst(self):
        if self.__head is None:
            print("The Linkedlist is Empty")
        elif(self.__head==self.__tail):
            self.__head=self.__tail=None
        else:
            temp=self.__head
            self.__head=self.__head.get_next()
            temp.set_next(None)
    def displayLinkedList(self):
        if(self.__head is None):
            print("The Linkedlist is Empty")
        else:
            lastnode=self.__head
            while lastnode is not None:
                print(lastnode.get_data())
                lastnode=lastnode.get_next()
    def searchNode(self,data):
        if(self.__head is None):
            print("The Linkedlist is Empty")
        else:
            m=0
            lastnode=self.__head
            while lastnode is not None:
                if(lastnode.get_data()==data):
                    print("Found")
                    return
                lastnode=lastnode.get_next()
            print("Not Found")

    def sum_of_even_node(self):
        if (self.__head is None or self.__head.get_next() is None):
            print("The Linkedlist is Empty")
        else:
            sum=0
            temp=self.__head
            temp=temp.get_next()
            while temp is not None:
                sum=sum+temp.get_data()
                if(temp.get_next() is not None and temp.get_next().get_next() is not None):
                    temp=temp.get_next().get_next()
                else:
                    print(sum)
                    break
    def sum_of_odd_node(self):
        if (self.__head is None or self.__head.get_next() is None):
            print("The Linkedlist is Empty")
        else:
            sum=0
            temp=self.__head
            while temp is not None:
                sum=sum+temp.get_data()
                if(temp.get_next() is not None and temp.get_next().get_next() is not None):
                    temp=temp.get_next().get_next()
                else:
                    print(sum)
                    break

    def sum_of_even_data(self):
        if (self.__head is None or self.__head.get_next() is None):
            print("The Linkedlist is Empty")
        else:
            temp = self.__head
            sum = 0
            while temp is not None:
                if (temp.get_data() % 2 == 0):
                    sum=sum+temp.get_data()
                temp=temp.get_next()
            print(sum)

    def sum_of_odd_data(self):
        if (self.__head is None or self.__head.get_next() is None):
            print("The Linkedlist is Empty")
        else:
            temp = self.__head
            sum = 0
            while temp is not None:
                if (temp.get_data() % 2 != 0):
                    sum = sum + temp.get_data()
                temp = temp.get_next()
            print(sum)



l1=Linkedlist()
l1.addNodeFirst(2)
l1.addNodeLast(4)
l1.addNodeLast(6)
l1.addNodeLast(8)
l1.addNodeLast(10)
l1.addNodeFirst(0)
l1.displayLinkedList()
l1.deleteNodeLast()
l1.deleteNodeFirst()
l1.searchNode(6)
l1.sum_of_even_node()
l1.sum_of_odd_node()
l1.addNodeAt(4,10)
l1.displayLinkedList()
l1.sum_of_even_data()
l1.sum_of_odd_data()
print(l1.())
l1.deleteNodeAt(2)
l1.displayLinkedList()
