class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Sll:
    def __init__(self):
        self.head=None
    def traversal(self):
        if self.head is None:
            print("empty list")
        else:
            a=self.head
            while a is not None:
                print(a.data,end=" ")
                a=a.next
        print()
    def beg(self,data):
        new=Node(data)
        new.next=self.head
        self.head=new
        print()

    def end(self,data):
        new1=Node(data)
        a=self.head
        if self.head is None:
            self.head=new1
            return

        while a.next is not None:
            a=a.next
        a.next=new1
    print()

    def middle(self,data,pos):
        new2=Node(data)
        a=self.head
        # c-1
        if self.head is None:
            if pos==1:
                self.head=new2
                return
            else:
                print("position out of range")
            return
        
        # c-2
        if pos==1:
            new2.next=self.head
            self.head=new2
            return

        # c-3
        for i in range(1,pos-1):
            if a is None:
                print("position out of range")
                return
            a=a.next
        if a is None:
            print("position out of range")
            return
        new2.next=a.next
        a.next=new2

    def delbeg(self):
        if self.head is None:
            print("List is empty,deletion not possible")
            return
        self.head=self.head.next

    def delend(self):
        if self.head is None:
            print("list is empty , deletion not possible")
            return

        if self.head.next is None:
            self.head=None
            return
        
        a=self.head
        while a.next.next is not None:
            a=a.next
        a.next=None

    def delmid(self,pos):
        # c-1
        if self.head is None:
            print("list is empty , deletion not possible")
            return
        
        # c-2
        if pos==1:
            self.head=self.head.next
            return
        
        # c-3
        a=self.head
        for i in range(1,pos-1):
            if a is None or a.next is None:
                print("position out of range")
                return
            a=a.next
        if a.next is None:
                print("position out of range")
                return
        a.next=a.next.next

n1=Node(10)
sll=Sll()
sll.head=n1
n2=Node(20)
n1.next=n2
n3=Node(30)
n2.next=n3
sll.traversal()
sll.beg(1)
sll.traversal()
sll.end(40)
sll.traversal()
sll.middle(1,1)
sll.traversal()
sll.middle(2,2)
sll.traversal()
sll.middle(3,2)
sll.traversal()
sll.middle(0,2)
sll.traversal()
sll.delbeg()
sll.traversal()
sll.delend()
sll.traversal()
sll.delmid(3)
sll.traversal()
