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
    def find(self,key):
        current=self.head
        index=0
        while current:
            if index==key:
                return current.data
            index= index+1
            current=current.next
a_llist=Linkedlist()
num=int(input("How many elements :"))
for i in range(num):
    data=int(input("enter  the numbers :"))
    a_llist.append(data)
print("The linked list is :\n",end=" ")
a_llist.display()
find_num=(input("\nIndex to find :"))
print("The index is :",a_llist.find(find_num))
