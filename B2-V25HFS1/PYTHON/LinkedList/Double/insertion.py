class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class insertion:
    def __init__(self):
        self.head=None
    def ftraversal(self):
        if self.head is None:
            print("List is empty")
            return
        a=self.head
        while a is not None:
            print(a.data,end=" ")
            a=a.next
        print()
    def insbeg(self,data):
        new=Node(data)
        a=self.head
        if self.head is None:
            self.head=new
            return
        a.prev=new
        new.next=a
        self.head=new
    def insend(self,data):
        new=Node(data)
        a=self.head
        if self.head is None:
            self.head=new
            return
        while a.next is not None:
            a=a.next
        a.next=new
        new.prev=a
    def insmid(self,data,pos):
        new=Node(data)
        a=self.head
        if self.head is None:
            if pos==1:
                self.head=new
                return
            else:
                print("Position out of range")
                return
        if pos==1:
            self.head.prev=new
            new.next=self.head
            self.head=new
            return
        for i in range(1,pos-1):
            if a.next is None:
                print("Position out of range")
                return
            a=a.next
        new.prev=a
        new.next=a.next
        if a.next is not None:
            a.next.prev=new
        a.next=new

    def delbeg(self):
        # zero nodes
        if self.head is None:
            print('deletion not possible,empty list')
            return
        # only 1 node
        if self.head.next is None:
            self.head=None
            return
        # morethan 1 node
        self.head=self.head.next
        self.head.prev=None

    def delend(self):
        # zero nodes
        if self.head is None:
            print('deletion not possible,empty list')
            return
        # only 1 node
        if self.head.next is None:
            self.head=None
            return
        # morethan 1 node
        a=self.head
        while a.next is not None:
            a=a.next
        a.prev.next=None

    def delmid(self,pos):
        a=self.head
        # zero nodes
        if self.head is None:
            print('deletion not possible,empty list')
            return
        # only 1 node and pos==1
        if pos==1:
            if self.head.next is None:
                self.head=None
            else:
                self.head=self.head.next
                self.head.prev=None
            return
        for i in range(1,pos):
            if a is None:
                print("Position out of range")
                return
            a=a.next
        if a is None:
            print("Position out of range")
            return
        if a.prev is not None:
            a.prev.next=a.next
        if a.next is not None:
            a.next.prev=a.prev

n1=Node(1)
ins=insertion()
ins.head=n1
n2=Node(2)
n2.prev=n1
n1.next=n2
n3=Node(3)
n2.next=n3
n3.prev=n2
ins.ftraversal()

ins.insbeg(0)
ins.ftraversal()

ins.insend(4)
ins.ftraversal()

# ins.insmid(1,1)
# ins.ftraversal()
# ins.insmid(2,2)
# ins.ftraversal()
# ins.insmid(3,3)
# ins.ftraversal()

# ins.delbeg()
# ins.ftraversal()

# ins.delend()
# ins.ftraversal()

ins.delmid(3)
ins.ftraversal()
