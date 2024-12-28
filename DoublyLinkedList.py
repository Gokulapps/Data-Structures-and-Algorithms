class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None
        self.__before=None
    def set_data(self,data):
        self.__data=data
    def get_data(self):
        return self.__data
    def set_next(self,newnode):
        self.__next=newnode
    def get_next(self):
        return self.__next
    def set_before(self,newnode):
        self.__before = newnode
    def get_before(self):
        return self.__before
class Linkedlist:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def length(self):
        len = 0
        if (self.__head == None):
            return len
        else:
            lastnode = self.__head
            while lastnode is not None:
                len += 1
                lastnode = lastnode.get_next()
            return len
    def addNode(self,data):
        newnode=Node(data)
        if(self.__head==None):
            self.__head=self.__tail=newnode
        else:
            self.__tail.set_next(newnode)
            temp=self.__tail
            self.__tail=self.__tail.get_next()
            self.__tail.set_before(temp)
    def addNodeFirst(self,data):
        newnode=Node(data)
        if self.__head is None:
            self.__head=self.__tail=newnode
        else:
            newnode.set_next(self.__head)
            self.__head.set_before(newnode)
            self.__head=self.__head.get_before()
    def deleteNode(self):
        if(self.__head==None):
            print("No Elements Present to Delete")
        elif(self.__head==self.__tail):
            self.__head=self.__tail
        lastnode=self.__head
        while lastnode.get_next() is not None:
            prevnode=lastnode
            lastnode=lastnode.get_next()
        lastnode.set_before(None)
        prevnode.set_next(None)
        self.__tail=prevnode
    def deleteNodeFirst(self):
        if self.__head is None:
            print("No Elements Present to Delete")
        elif(self.__head==self.__tail):
            self.__head=self.__tail=None
        temp=self.__head
        self.__head=self.__head.get_next()
        self.__head.set_before(None)
        temp.set_next(None)
    def deleteNodeMiddle(self,data):
        if(self.__head is None or self.__head==self.__tail or self.__head.get_data()==data):
            print("No Elements to Delete")
            return
        currentnode=self.__head
        while currentnode is not None:
            if(currentnode.get_data()==data):
                temp=prevnode.get_before()
                if temp!=None:
                    temp.set_next(currentnode)
                    currentnode.set_before(temp)
                    prevnode.set_before(None)
                    prevnode.set_before(None)
                else:
                    self.__head=self.__head.get_next()
                    prevnode.set_next(None)
                    currentnode.set_before(None)
                return
            prevnode=currentnode
            currentnode=currentnode.get_next()
        print("No Node Found")
    def displayNodeForward(self):
        if(self.__head is None):
            print("The Linkedlist is Empty")
        else:
            lastnode=self.__head
            while lastnode is not None:
                print(lastnode.get_data())
                lastnode=lastnode.get_next()

    def displayNodeReverse(self):
        if(self.__head==None):
            print("No Elements to Print")
        else:
            lastnode=self.__tail
            while lastnode is not None:
                print(lastnode.get_data())
                lastnode=lastnode.get_before()

c=Linkedlist()
c.addNode(1)
c.addNode(2)
c.addNode(3)
c.addNode(4)
c.addNode(5)
c.addNode(6)
c.addNode(7)
c.addNodeFirst(0)
c.displayNodeReverse()
c.deleteNodeFirst()
c.deleteNode()
c.deleteNodeMiddle(1)
c.displayNodeForward()
