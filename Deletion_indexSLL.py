class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
        self.last_node=None 
    def append(self,data):
        if self.head is None:
            self.head=node(data)
            self.last_node=self.head
        else:
            self.last_node.next=node(data)
            self.last_node=self.last_node.next
    def display(self):
        current=self.head
        while current is not None:
            print(current.data,end=" ")
            current=current.next
    def delete(self,position):
        temp=self.head
        if temp==None:
            return 
        if position==0:
            self.head=temp.next
            temp=None  
            return
        for i in range(position-1):
            temp=temp.next
            if temp==None:
                return
        nextNode=temp.next.next
        temp.next=None
        temp.next=nextNode
a_llist=Linkedlist()
num=int(input("How many elements :"))
for i in range(num):
    data=int(input("enter  the numbers :"))
    a_llist.append(data)
print("The linked list is :\n",end=" ")
a_llist.display()
j=int(input("\nenter the element to delete :"))
a_llist.delete(j)
a_llist.display()




