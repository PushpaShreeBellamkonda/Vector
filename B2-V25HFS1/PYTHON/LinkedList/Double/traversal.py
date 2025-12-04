class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class Dll:
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
    def btraversal(self):
        if self.head is None:
            print("List is empty")
            return
        a=self.head
        while a.next is not  None:
            a=a.next
        while a is not None:
            print(a.data,end=" ")
            a=a.prev

n1=Node(1)
dll=Dll()
dll.head=n1
n2=Node(2)
n1.next=n2
n2.prev=n1
n3=Node(3)
n2.next=n3
n3.prev=n2
dll.ftraversal()
dll.btraversal()
        


